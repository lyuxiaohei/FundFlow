# -*- coding: utf-8 -*-
"""复核2：字典 v2 —— F25 数据字典页 Playwright 实测"""
import sys, json
sys.path.insert(0, '/Users/bailey/Desktop/xiaohei-workplace/FundFlow/agent-handoff/_g06_verify')
from pw_common import Harness, page_uri

h = Harness()
try:
    ctx, page, errs = h.open('P3-R01-原型/系统管理/P3-R01-F25-数据字典.html')
    checks = {}
    checks['DM truthy'] = page.evaluate('!!window.DM')
    checks['dictionaries.length'] = page.evaluate('DM.store.dictionaries.length')
    checks['side items count'] = page.evaluate("document.querySelectorAll('.dict-side .dict-item').length")
    ap = page.evaluate("DM.dict('apType').items")
    checks['apType items'] = [i.get('name') for i in ap]
    checks['apType last'] = ap[-1].get('name') if ap else None
    checks['apType slaHours all number'] = all(isinstance(i.get('slaHours'), (int, float)) for i in ap)
    checks['apType slaHours values'] = [i.get('slaHours') for i in ap]
    rt = page.evaluate("DM.dict('ruleType').items")
    checks['ruleType items'] = [i.get('name') for i in rt]
    checks['dp-apType rows'] = page.evaluate("document.querySelectorAll('#dp-apType tbody tr').length")
    checks['dp-ruleType rows'] = page.evaluate("document.querySelectorAll('#dp-ruleType tbody tr').length")
    ready = page.evaluate('document.readyState')
    print('readyState:', ready)
    for k, v in checks.items():
        print(k, '=', json.dumps(v, ensure_ascii=False))
    print('JS errors:', errs)
finally:
    h.close()
