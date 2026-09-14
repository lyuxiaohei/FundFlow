# -*- coding: utf-8 -*-
"""G03/T1 数据零丢失门：逐接入页 Playwright 断言（行数＋首列集合 vs 基线；window.DM；0 JS 错误）"""
import json, re
from pathlib import Path
from playwright.sync_api import sync_playwright

WORK = "/Users/bailey/Desktop/xiaohei-workplace/FundFlow/agent-handoff/_g03_work"
ROOT = Path("/Users/bailey/Desktop/xiaohei-workplace/FundFlow/P3-R01-原型")
base = json.load(open(f"{WORK}/gate_base.json", encoding="utf-8"))

PAGES = {
 'F00': '工作台/P3-R01-F00-工作台.html', 'F01': '项目库/P3-R01-F01-项目列表.html',
 'F07': '基金管理/P3-R01-F07-基金列表.html', 'F10': 'LP 管理/P3-R01-F10-LP出资.html',
 'F12': '投后管理/P3-R01-F12-报告归档.html', 'F13': '投后管理/P3-R01-F13-风险预警.html',
 'F14': '投后管理/P3-R01-F14-提醒中心.html', 'F15': '退出管理/P3-R01-F15-项目退出.html',
 'F16': '退出管理/P3-R01-F16-收益分配.html', 'F17': '退出管理/P3-R01-F17-清算注销.html',
 'F18': '统计报表/P3-R01-F18-阶段漏斗.html', 'F19': '统计报表/P3-R01-F19-放弃原因分布.html',
 'F20': '审批中心/P3-R01-F20-审批中心.html', 'F22': '投后管理/P3-R01-F22-投后项目.html',
 'F23': '退出管理/P3-R01-F23-退出项目.html',
}

JS_COLLECT = """() => {
  const norm = s => s.replace(/\\s+/g, ' ').trim();
  const firstCells = (sel, idx) => Array.from(document.querySelectorAll(sel + ' tr')).map(tr => {
    const tds = tr.querySelectorAll(':scope > td');
    if (!tds.length) return null;
    const i = (tds[0].querySelector('input[type=checkbox]') && idx === undefined) ? 1 : (idx || 0);
    return norm(tds[Math.min(i, tds.length - 1)].textContent);
  }).filter(Boolean);
  return {
    dm: !!window.DM,
    rows: (sel) => document.querySelectorAll(sel + ' tr').length,
    first: firstCells
  };
}"""

def collect(pg, key):
    """按页收集门指标"""
    if key == 'F00':
        todo = pg.eval_on_selector_all('#dmTodoList > .todo-item', 'els => els.length')
        stall = pg.eval_on_selector_all('#dmStallList > .stall-item', 'els => els.length')
        mine = pg.eval_on_selector_all('#dmMineList > .todo-item', 'els => els.length')
        names = pg.eval_on_selector_all('#dmTodoList .t-name, #dmStallList .t-name, #dmMineList .t-name', 'els => els.map(e => e.textContent.trim())')
        return {'todo': todo + mine, 'stall': stall, 'names': names}
    if key == 'F13':
        cards = pg.eval_on_selector_all('#dmWarnList > .alert-card', 'els => els.length')
        titles = pg.eval_on_selector_all('#dmWarnList .al-title b', 'els => els.map(e => e.textContent.trim())')
        return {'cards': cards, 'titles': titles}
    if key == 'F17':
        steps = pg.eval_on_selector_all('#stepsBar .step', 'els => els.length')
        docs = pg.eval_on_selector_all('#docList .doc-row', 'els => els.length')
        feed = pg.eval_on_selector_all('#feedList .feed-item', 'els => els.length')
        tag = pg.eval_on_selector('#fundTag', 'el => el.textContent.trim()')
        return {'steps': steps, 'docs': docs, 'feed': feed, 'tag': tag}
    if key == 'F20':
        out = {}
        for v, sel in [('todo', '#dmBodyTodo'), ('cc', '#dmBodyCc'), ('mine', '#dmBodyMine'), ('done', '#dmBodyDone')]:
            rows = pg.eval_on_selector_all(sel + ' > tr', 'els => els.length')
            first = pg.eval_on_selector_all(sel + ' > tr', 'els => els.map(e => e.querySelector("td span.lk") ? e.querySelector("td span.lk").textContent.trim() : e.textContent.trim().slice(0,20))')
            out[v] = {'rows': rows, 'first': first}
        return out
    if key == 'F19':
        rows = pg.eval_on_selector_all('#dmBody > tr', 'els => els.length')
        first = pg.eval_on_selector_all('#dmBody > tr', '''els => els.map(e => {
            if (e.classList.contains('group-row')) { return e.textContent.replace(/GP \\· \\d+ 条|LP \\· \\d+ 条/, '').trim(); }
            return e.querySelector('td .tag') ? e.querySelector('td .tag').textContent.trim() : '';
        })''')
        return {'rows': rows, 'first': first}
    if key == 'F16':
        rows = pg.eval_on_selector_all('#dmBody > tr.main-row', 'els => els.length')
        sub = pg.eval_on_selector_all('#dmBody > tr.sub-row', 'els => els.length')
        lp = pg.eval_on_selector_all('#dmBody .lp-table tbody tr', 'els => els.length')
        first = pg.eval_on_selector_all('#dmBody > tr.main-row', 'els => els.map(e => e.querySelector("td span.lk").textContent.trim())')
        return {'rows': rows + sub, 'lp_rows': lp, 'first': first}
    if key == 'F15':
        rows = pg.eval_on_selector_all('#rowsData > tr', 'els => els.length')
        first = pg.eval_on_selector_all('#rowsData > tr', 'els => els.map(e => e.querySelector("td span.lk").textContent.trim())')
        return {'rows': rows, 'first': first}
    if key == 'F18':
        rows = pg.eval_on_selector_all('#dmFunnelBody > tr', 'els => els.length')
        first = pg.eval_on_selector_all('#dmFunnelBody > tr', 'els => els.map(e => e.querySelector("td .stage-cell").textContent.trim())')
        foot = pg.eval_on_selector_all('#dmFunnelFoot > tr', 'els => els.length')
        return {'rows': rows, 'first': first, 'foot': foot}
    if key == 'F01':
        rows = pg.eval_on_selector_all('#dmBody > tr', 'els => els.length')
        first = pg.eval_on_selector_all('#dmBody > tr', 'els => els.map(e => e.querySelectorAll("td")[1].textContent.trim())')
        kbcards = pg.eval_on_selector_all('#dmKbCols .kb-card', 'els => els.length')
        kbcols = pg.eval_on_selector_all('#dmKbCols .kb-col', 'els => els.length')
        return {'rows': rows, 'first': first, 'kb_cards': kbcards, 'kb_cols': kbcols}
    # 通用单 tbody（F07/F12/F14/F15/F18/F22/F23/F10）
    rows = pg.eval_on_selector_all('#dmBody > tr' if key != 'F10' else '#capBody > tr', 'els => els.length')
    first = pg.eval_on_selector_all('#dmBody > tr' if key != 'F10' else '#capBody > tr',
        'els => els.map(e => { const tds = e.querySelectorAll("td"); const i = (tds[0] && tds[0].querySelector("input[type=checkbox]")) ? 1 : 0; return tds[i].textContent.trim(); })')
    out = {'rows': rows, 'first': first}
    if key == 'F18':
        foot = pg.eval_on_selector_all('#dmFunnelFoot > tr', 'els => els.length')
        out['foot'] = foot
    return out

def check(key, got):
    b = base[key]
    ok, msgs = True, []
    def eq(name, g, e):
        nonlocal ok
        if isinstance(e, list):
            good = sorted(g) == sorted(e)
        else:
            good = g == e
        if not good:
            ok = False
            msgs.append(f"{name}: 前={e} 后={g}")
    if key == 'F00':
        eq('todo数', got['todo'], b['todo']); eq('stall数', got['stall'], b['stall']); eq('名称集合', got['names'], b['names'])
    elif key == 'F13':
        eq('卡片数', got['cards'], b['cards']); eq('标题集合', got['titles'], b['titles'])
    elif key == 'F17':
        eq('步骤数', got['steps'], b['steps']); eq('材料数', got['docs'], b['docs']); eq('事件数', got['feed'], b['feed']); eq('基金标签', got['tag'], b['tag'])
    elif key == 'F20':
        for v in ['todo', 'cc', 'mine', 'done']:
            eq(f'{v}行数', got[v]['rows'], b[v]['rows']); eq(f'{v}首列', got[v]['first'], b[v]['first'])
    else:
        eq('行数', got['rows'], b['rows'])
        if 'first' in b: eq('首列集合', got['first'], b['first'])
        if key == 'F16': eq('LP子表行数', got['lp_rows'], b['lp_rows'])
        if key == 'F18': eq('合计行', got['foot'], 1)
    return ok, msgs

results, failures, js_errors = {}, [], {}
with sync_playwright() as pw:
    browser = pw.chromium.launch()
    for key, rel in PAGES.items():
        errs = []
        page = browser.new_page()
        page.on('pageerror', lambda e: errs.append('pageerror: ' + str(e)))
        page.on('console', lambda m: errs.append('console.error: ' + m.text) if m.type == 'error' else None)
        try:
            page.goto((ROOT / rel).resolve().as_uri())
            page.wait_for_timeout(120)
            dm = page.evaluate('() => !!window.DM')
            got = collect(page, key)
            ok, msgs = check(key, got)
            line = f"数据零丢失 {key}: 行数 前={json.dumps(base[key], ensure_ascii=False)[:0] or ''}{msgs and ''}"
            # 组织验证门要求的输出格式
            if key in ('F00', 'F13', 'F17'):
                rn = {k: v for k, v in got.items() if k not in ('names', 'titles', 'first', 'tag')}
                detail = f"行数 前={json.dumps(base[key], ensure_ascii=False, default=str)[:60]}"
            else:
                detail = '行数'
            if errs:
                ok = False; msgs = msgs + errs
            results[key] = (ok, got, msgs, dm, errs)
            status = 'PASS' if (ok and dm and not errs) else 'FAIL'
            if status == 'FAIL': failures.append(key)
            js_errors[key] = len(errs)
            print(f"[{status}] {key} dm={dm} {msgs if msgs else ''} errs={errs if errs else 0}")
        except Exception as e:
            failures.append(key); results[key] = (False, None, [str(e)], False, [str(e)])
            print(f"[FAIL] {key} 异常: {e}")
        finally:
            page.close()
    browser.close()

print(f"\n接入 {15 - len(set(failures))}/15（失败页：{sorted(set(failures)) if failures else '无'}）")
json.dump({k: {'ok': v[0], 'msgs': v[2], 'dm': v[3]} for k, v in results.items()},
          open(f"{WORK}/gate_result.json", 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
