# -*- coding: utf-8 -*-
"""G03/T2 验证门：页内真联动 Playwright 编程点击断言"""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path("/Users/bailey/Desktop/xiaohei-workplace/FundFlow/P3-R01-原型")
results = []

def mkpage(browser):
    pg = browser.new_page()
    pg.on('dialog', lambda d: d.accept())
    return pg

with sync_playwright() as pw:
    b = pw.chromium.launch()

    # ---- 1. F20 通过一条 → 待审徽章-1 且行迁移 ----
    pg = mkpage(b)
    pg.goto((ROOT / '审批中心/P3-R01-F20-审批中心.html').resolve().as_uri())
    pg.wait_for_timeout(150)
    assert pg.text_content('#dmCntTodo').strip() == '3'
    pg.click('#dmBodyTodo tr:first-child td.ops a')          # 第一条「审批」
    assert pg.is_visible('#apModal')
    pg.click('#apModal .modal-footer .btn-primary')          # 提交审批意见（默认通过）
    pg.wait_for_timeout(100)
    todo_cnt = pg.text_content('#dmCntTodo').strip()
    todo_has = pg.eval_on_selector_all('#dmBodyTodo tr', 'els => els.some(e => e.textContent.includes("APV-2026-0037"))')
    done_rows = pg.eval_on_selector_all('#dmBodyDone tr', 'els => els.length')
    done_has = pg.eval_on_selector_all('#dmBodyDone tr', 'els => els.some(e => e.textContent.includes("APV-2026-0037"))')
    done_cnt = pg.text_content('#dmCntDone').strip()
    done_first_action = pg.text_content('#dmBodyDone tr:first-child td:nth-child(5)').strip()
    ok1 = (todo_cnt == '2') and (not todo_has) and done_has and (done_rows == 5) and (done_cnt == '5') and (done_first_action == '通过')
    results.append(('F20 通过一条→待审徽章-1 且行迁移至我已审批（徽章3→2/已完成4→5）', ok1,
                    f'徽章todo={todo_cnt} done={done_cnt} done行数={done_rows} 处理={done_first_action}'))
    pg.close()

    # ---- 1b. F20 撤回 ----
    pg = mkpage(b)
    pg.goto((ROOT / '审批中心/P3-R01-F20-审批中心.html').resolve().as_uri())
    pg.wait_for_timeout(150)
    pg.click('.stab[data-view="mine"]')                       # 切「我发起的」
    pg.wait_for_timeout(80)
    pg.click('#dmBodyMine tr:first-child td.ops a:nth-child(2)')  # 撤回
    pg.wait_for_timeout(100)
    mine_cnt = pg.text_content('#dmCntMine').strip()
    mine_has = pg.eval_on_selector_all('#dmBodyMine tr', 'els => els.some(e => e.textContent.includes("APV-2026-0037"))')
    todo_cnt = pg.text_content('#dmCntTodo').strip()
    todo_has = pg.eval_on_selector_all('#dmBodyTodo tr', 'els => els.some(e => e.textContent.includes("APV-2026-0037"))')
    ok = (mine_cnt == '2') and (not mine_has) and (todo_cnt == '2') and (not todo_has)
    results.append(('F20 撤回→「我发起的/待我审批」该单移除且徽章联动（mine3→2/todo3→2）', ok,
                    f'mine={mine_cnt} todo={todo_cnt}'))
    pg.close()

    # ---- 2. F01 推进 → 行内阶段徽章变化 ----
    pg = mkpage(b)
    pg.goto((ROOT / '项目库/P3-R01-F01-项目列表.html').resolve().as_uri())
    pg.wait_for_timeout(150)
    row = 'tr:has-text("PRJ-2026-0001")'
    before_stage = pg.text_content(f'#dmBody {row} .stage-cell').strip()
    pg.click(f'#dmBody {row} a:has-text("推进")')
    assert pg.is_visible('#dmAdvModal')
    pg.click('#dmAdvModal .modal-footer .btn-primary')        # 确认推进
    pg.wait_for_timeout(100)
    after_stage = pg.text_content(f'#dmBody {row} .stage-cell').strip()
    after_status = pg.text_content(f'#dmBody {row} .tag').strip()
    kb8 = pg.eval_on_selector_all('#dmKbCols .kb-col:nth-child(8) .kb-card', 'els => els.some(e => e.textContent.includes("聚变能源科技"))')
    kb7 = pg.eval_on_selector_all('#dmKbCols .kb-col:nth-child(7) .kb-card', 'els => els.length')
    ok = (before_stage == '⑦ 投决') and (after_stage == '⑧ 基金设立') and (after_status == '基金设立中') and kb8 and kb7 == 0
    results.append(('F01 推进→行内阶段徽章 ⑦投决→⑧基金设立、状态更新、泳道卡迁移', ok,
                    f'{before_stage}→{after_stage} 状态={after_status} 泳道⑧含卡={kb8} ⑦余卡={kb7}'))
    pg.close()

    # ---- 2b. F01 放弃登记 → 行迁入未投归档态（不删行） ----
    pg = mkpage(b)
    pg.goto((ROOT / '项目库/P3-R01-F01-项目列表.html').resolve().as_uri())
    pg.wait_for_timeout(150)
    row = 'tr:has-text("PRJ-2026-0006")'
    pg.click(f'#dmBody {row} a:has-text("放弃")')
    assert pg.is_visible('#abandonModal')
    pg.select_option('#leafReason', '明显超出投资范围')
    pg.click('#abandonModal .modal-footer .btn-primary')      # 确认放弃并归档
    pg.wait_for_timeout(100)
    stage = pg.text_content(f'#dmBody {row} .stage-cell').strip()
    status = pg.text_content(f'#dmBody {row} .tag').strip()
    rows_n = pg.eval_on_selector_all('#dmBody tr', 'els => els.length')
    ab_n = pg.evaluate('() => DM.store.abandons.length')
    ok = (stage == '未投归档') and (status == 'GP·明显超出投资范围') and (rows_n == 10) and (ab_n == 11)
    results.append(('F01 放弃登记→该行迁入未投归档态（行数不变 10、abandons 单源 +1）', ok,
                    f'阶段={stage} 状态={status} 行数={rows_n} abandons={ab_n}'))
    pg.close()

    # ---- 3. F15 登记批次 → 行数 +1 ----
    pg = mkpage(b)
    pg.goto((ROOT / '退出管理/P3-R01-F15-项目退出.html').resolve().as_uri())
    pg.wait_for_timeout(150)
    n0 = pg.eval_on_selector_all('#rowsData tr', 'els => els.length')
    pg.click('button:has-text("＋ 登记退出批次")')
    pg.fill('#exPrice', '3.00')
    pg.fill('#exQty', '500')
    pg.click('#batModal .modal-footer .btn-primary')          # 确认登记
    pg.wait_for_timeout(100)
    n1 = pg.eval_on_selector_all('#rowsData tr', 'els => els.length')
    has_new = pg.eval_on_selector_all('#rowsData tr', 'els => els.some(e => e.textContent.includes("BAT-2026-003"))')
    pginfo = pg.text_content('#pgInfo').strip()
    amount = pg.eval_on_selector_all('#rowsData tr', 'els => els.filter(e => e.textContent.includes("BAT-2026-003")).map(e => e.querySelectorAll("td")[4].textContent.trim())[0]')
    ok = (n0 == 3) and (n1 == 4) and has_new and (pginfo == '第 1-4 条/总共 4 条') and (amount == '1,500')
    results.append(('F15 登记批次→批次表行数 3→4、新增 BAT-2026-003、页码联动、金额自动计算', ok,
                    f'{n0}→{n1} 页码={pginfo} 金额={amount}'))
    pg.close()

    # ---- 4. F12 上传报告 → 行数 +1 ----
    pg = mkpage(b)
    pg.goto((ROOT / '投后管理/P3-R01-F12-报告归档.html').resolve().as_uri())
    pg.wait_for_timeout(150)
    n0 = pg.eval_on_selector_all('#dmBody tr', 'els => els.length')
    pg.click('#dmBody tr:first-child a:has-text("上传")')      # RPT-2026-021 云雀 Q2 上传
    assert pg.is_visible('#upModal')
    pg.click('#upModal .modal-footer .btn-primary')           # 确认上传归档
    pg.wait_for_timeout(100)
    n1 = pg.eval_on_selector_all('#dmBody tr', 'els => els.length')
    has_new = pg.eval_on_selector_all('#dmBody tr', 'els => els.some(e => e.textContent.includes("RPT-2026-022"))')
    r21 = pg.eval_on_selector_all('#dmBody tr', 'els => els.filter(e => e.textContent.includes("RPT-2026-021")).map(e => e.querySelector(".tag").textContent.trim())[0]')
    cnt_all = pg.text_content('#dmCntAll').strip(); cnt_q = pg.text_content('#dmCntQ').strip()
    ok = (n0 == 5) and (n1 == 6) and has_new and (r21 == '已归档') and (cnt_all == '6') and (cnt_q == '3')
    results.append(('F12 上传报告→报告表行数 5→6、RPT-2026-022 新增、待上传行消解、计数页签联动', ok,
                    f'{n0}→{n1} 新行={has_new} RPT-2026-021状态={r21} 全部={cnt_all} 季报={cnt_q}'))
    pg.close()
    b.close()

print("\n===== T2 联动断言 =====")
fails = 0
for name, ok, ev in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} ｜ {ev}")
    if not ok: fails += 1
print(f"T2 断言: {'ALL PASS' if fails == 0 else f'{fails} 项 FAIL'}")
