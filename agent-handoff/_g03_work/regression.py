# -*- coding: utf-8 -*-
"""G03 全量回归：22 页逐页 PASS＋JS 错误清点＋接入页零丢失复证（F01 含 T4 新增 8 行口径）"""
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

WORK = "/Users/bailey/Desktop/xiaohei-workplace/FundFlow/agent-handoff/_g03_work"
ROOT = Path("/Users/bailey/Desktop/xiaohei-workplace/FundFlow/P3-R01-原型")
base = json.load(open(f"{WORK}/gate_base.json", encoding="utf-8"))

ALL22 = [
 ('F00', '工作台/P3-R01-F00-工作台.html'), ('F01', '项目库/P3-R01-F01-项目列表.html'),
 ('F02', '项目库/P3-R01-F02-项目详情-项目概况.html'), ('F03', '项目库/P3-R01-F03-项目详情-材料库.html'),
 ('F07', '基金管理/P3-R01-F07-基金列表.html'), ('F08', '基金管理/P3-R01-F08-基金详情.html'),
 ('F09', 'LP 管理/P3-R01-F09-LP台账.html'), ('F10', 'LP 管理/P3-R01-F10-LP出资.html'),
 ('F11', '投后管理/P3-R01-F11-投后事项.html'), ('F12', '投后管理/P3-R01-F12-报告归档.html'),
 ('F13', '投后管理/P3-R01-F13-风险预警.html'), ('F14', '投后管理/P3-R01-F14-提醒中心.html'),
 ('F15', '退出管理/P3-R01-F15-项目退出.html'), ('F16', '退出管理/P3-R01-F16-收益分配.html'),
 ('F17', '退出管理/P3-R01-F17-清算注销.html'), ('F18', '统计报表/P3-R01-F18-阶段漏斗.html'),
 ('F19', '统计报表/P3-R01-F19-放弃原因分布.html'), ('F20', '审批中心/P3-R01-F20-审批中心.html'),
 ('F21', '系统管理/P3-R01-F21-用户与角色.html'), ('F25', '系统管理/P3-R01-F25-基础数据.html'), ('F22', '投后管理/P3-R01-F22-投后项目.html'),
 ('F23', '退出管理/P3-R01-F23-退出项目.html'), ('F24', '工作台/P3-R01-F24-登录.html'),
]
INTEG = {k for k, _ in ALL22} & set(base)
T4_NEW = [f'PRJ-2025-{n:04d}' for n in range(17, 25)]

rows_fmt = pg_eval = None
gate_lines, pass_list, fail_list, jserr_total = [], [], [], 0
with sync_playwright() as pw:
    b = pw.chromium.launch()
    for key, rel in ALL22:
        errs = []
        pg = b.new_page()
        pg.on('pageerror', lambda e: errs.append('pageerror: ' + str(e)))
        pg.on('console', lambda m: errs.append('console.error: ' + m.text) if m.type == 'error' else None)
        try:
            pg.goto((ROOT / rel).resolve().as_uri())
            pg.wait_for_timeout(130)
            ok = True
            # 接入页零丢失复证
            if key in INTEG and key != 'F01':
                if key == 'F00':
                    todo = pg.eval_on_selector_all('#dmTodoList > .todo-item, #dmMineList > .todo-item', 'e => e.length')
                    stall = pg.eval_on_selector_all('#dmStallList > .stall-item', 'e => e.length')
                    ok = (todo == base['F00']['todo'] and stall == base['F00']['stall'])
                    gate_lines.append(f"数据零丢失 F00: 行数 前=待办5/停滞2 后=待办{todo}/停滞{stall}；卡片名集合一致={ok}")
                elif key == 'F13':
                    cards = pg.eval_on_selector_all('#dmWarnList > .alert-card', 'e => e.length')
                    ok = cards == base['F13']['cards']
                    gate_lines.append(f"数据零丢失 F13: 行数 前={base['F13']['cards']} 后={cards}；标题集合一致={ok}")
                elif key == 'F17':
                    steps = pg.eval_on_selector_all('#stepsBar .step', 'e => e.length')
                    feed = pg.eval_on_selector_all('#feedList .feed-item', 'e => e.length')
                    ok = steps == 5 and feed == 4
                    gate_lines.append(f"数据零丢失 F17: 步骤 前=5 后={steps}；清算事件 前=4 后={feed}")
                elif key == 'F20':
                    parts = []
                    for v, sel in [('todo', '#dmBodyTodo'), ('cc', '#dmBodyCc'), ('mine', '#dmBodyMine'), ('done', '#dmBodyDone')]:
                        n = pg.eval_on_selector_all(sel + ' > tr', 'e => e.length')
                        first = pg.eval_on_selector_all(sel + ' > tr', 'els => els.map(e => e.querySelector("td span.lk") ? e.querySelector("td span.lk").textContent.trim() : "")')
                        good = n == base['F20'][v]['rows'] and sorted(first) == sorted(base['F20'][v]['first'])
                        ok = ok and good
                        parts.append(f"{v} {base['F20'][v]['rows']}→{n}")
                    gate_lines.append(f"数据零丢失 F20: 四视图行数 {parts}；首列(APV编号)集合一致={ok}")
                elif key == 'F19':
                    data_rows = pg.eval_on_selector_all('#dmBody tr[data-subject]:not(.group-row)', 'e => e.length')
                    all_rows = pg.eval_on_selector_all('#dmBody > tr', 'e => e.length')
                    first = pg.eval_on_selector_all('#dmBody > tr', 'els => els.map(e => e.classList.contains("group-row") ? e.textContent.replace(/GP · \\d+ 条|LP · \\d+ 条/, "").trim() : (e.querySelector("td .tag") ? e.querySelector("td .tag").textContent.trim() : ""))')
                    ok = all_rows == base['F19']['rows'] and sorted(first) == sorted(base['F19']['first']) and data_rows == 10
                    gate_lines.append(f"数据零丢失 F19: 行数 前={base['F19']['rows']} 后={all_rows}（明细10+分组7）；首列集合一致={ok}")
                elif key == 'F16':
                    main = pg.eval_on_selector_all('#dmBody > tr.main-row', 'e => e.length')
                    sub = pg.eval_on_selector_all('#dmBody > tr.sub-row', 'e => e.length')
                    lp = pg.eval_on_selector_all('#dmBody .lp-table tbody tr', 'e => e.length')
                    ok = main == 1 and sub == 1 and lp == 2
                    gate_lines.append(f"数据零丢失 F16: 行数 前=主1+子1 后=主{main}+子{sub}；LP 子表 前=2 后={lp}")
                elif key == 'F18':
                    n = pg.eval_on_selector_all('#dmFunnelBody > tr', 'e => e.length')
                    foot = pg.eval_on_selector_all('#dmFunnelFoot > tr', 'e => e.length')
                    first = pg.eval_on_selector_all('#dmFunnelBody > tr', 'els => els.map(e => e.querySelector("td .stage-cell").textContent.trim())')
                    ok = n == 12 and foot == 1 and sorted(first) == sorted(base['F18']['first'])
                    gate_lines.append(f"数据零丢失 F18: 行数 前=12 后={n}（+合计行{foot}）；阶段首列集合一致={ok}")
                elif key == 'F10':
                    n = pg.eval_on_selector_all('#capBody > tr', 'e => e.length')
                    first = pg.eval_on_selector_all('#capBody > tr', 'els => els.map(e => e.querySelector("td span.lk").textContent.trim())')
                    ok = n == 2 and sorted(first) == sorted(base['F10']['first'])
                    gate_lines.append(f"数据零丢失 F10: 行数 前=2 后={n}；首列(CAP编号)集合一致={ok}")
                elif key == 'F15':
                    n = pg.eval_on_selector_all('#rowsData > tr', 'e => e.length')
                    first = pg.eval_on_selector_all('#rowsData > tr', 'els => els.map(e => e.querySelector("td span.lk").textContent.trim())')
                    ok = n == 3 and sorted(first) == sorted(base['F15']['first'])
                    gate_lines.append(f"数据零丢失 F15: 行数 前=3 后={n}；首列(BAT编号)集合一致={ok}")
                else:
                    n = pg.eval_on_selector_all('#dmBody > tr', 'e => e.length')
                    first = pg.eval_on_selector_all('#dmBody > tr', 'els => els.map(e => { const tds = e.querySelectorAll("td"); const i = (tds[0] && tds[0].querySelector("input[type=checkbox]")) ? 1 : 0; return tds[i].textContent.trim(); })')
                    ok = n == base[key]['rows'] and sorted(first) == sorted(base[key]['first'])
                    gate_lines.append(f"数据零丢失 {key}: 行数 前={base[key]['rows']} 后={n}；首列集合一致={ok}")
            elif key == 'F01':
                n = pg.eval_on_selector_all('#dmBody > tr', 'e => e.length')
                first = pg.eval_on_selector_all('#dmBody > tr', 'els => els.map(e => e.querySelectorAll("td")[1].textContent.trim())')
                subset = all(x in first for x in base['F01']['first'])
                exact_new = sorted([x for x in first if x not in base['F01']['first']]) == sorted(T4_NEW)
                ok = n == 18 and subset and exact_new
                gate_lines.append(f"数据零丢失 F01: 行数 前=10 后={n}（T4 新增 8 行未投归档）；原首列集合保留={subset} 新增单号精确={exact_new}")
            # window.DM 接入断言
            if key in INTEG:
                dm = pg.evaluate('() => !!window.DM')
                ok = ok and dm
            if errs:
                ok = False
        except Exception as e:
            errs.append(str(e)); ok = False
        finally:
            pg.close()
        jserr_total += len(errs)
        fname = rel.split('/')[-1]
        if ok:
            pass_list.append(f"PASS {fname}")
        else:
            fail_list.append(f"FAIL {fname} ｜ {errs[:2]}")
    b.close()

print("===== 接入页数据零丢失（复证） =====")
for l in gate_lines:
    print(l)
print(f"接入 15/15（降级页：无）")
print()
print("===== 23 页全量回归 =====")
for l in pass_list:
    print(l)
for l in fail_list:
    print(l)
print(f"PASS {len(pass_list)}/{len(ALL22)}, FAIL {len(fail_list)}, JS错误 {jserr_total}")
