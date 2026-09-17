# -*- coding: utf-8 -*-
"""复核5：23 页全量回归——逐页 file:// 打开、双监听 0 JS 错误、readyState=complete"""
import sys, json, glob, os, re
sys.path.insert(0, '/Users/bailey/Desktop/xiaohei-workplace/FundFlow/agent-handoff/_g06_verify')
from pw_common import Harness, ROOT

plan = {
 '工作台': ['F00', 'F24'],
 '项目库': ['F01', 'F02', 'F03'],
 '基金管理': ['F07', 'F08'],
 'LP 管理': ['F09', 'F10'],
 '投后管理': ['F11', 'F12', 'F13', 'F14', 'F22'],
 '退出管理': ['F15', 'F16', 'F17', 'F23'],
 '统计报表': ['F18', 'F19'],
 '审批中心': ['F20'],
 '系统管理': ['F21', 'F25'],
}
# 组装 (编号, 相对路径)
pages = []
for folder, nums in plan.items():
    for num in nums:
        hits = glob.glob(os.path.join(ROOT, 'P3-R01-原型', folder, 'P3-R01-%s-*.html' % num))
        assert len(hits) == 1, 'glob %s in %s -> %d hits' % (num, folder, len(hits))
        rel = os.path.relpath(hits[0], ROOT)
        pages.append((num, rel))
print('TOTAL PAGES:', len(pages))

h = Harness()
results = []
try:
    for num, rel in pages:
        ctx, page, errs = h.open(rel, wait_ms=600, label=num)
        ready = page.evaluate('document.readyState')
        ok = (len(errs) == 0) and ready == 'complete'
        results.append((num, rel, ready, errs, ok))
        ctx.close()
finally:
    h.close()

npass = sum(1 for r in results if r[4])
nfail = len(results) - npass
jserr_total = sum(len(r[3]) for r in results)
for num, rel, ready, errs, ok in results:
    print('%s %s readyState=%s errors=%s %s' % (num, rel, ready, errs if errs else 0, 'PASS' if ok else 'FAIL'))
print('PASS %d/%d, FAIL %d, JS错误 %d' % (npass, len(results), nfail, jserr_total))
