# -*- coding: utf-8 -*-
"""复核3a：F20 新建弹窗审批类型 options 实测；3c：F14 降级静态检查"""
import sys, json, re
sys.path.insert(0, '/Users/bailey/Desktop/xiaohei-workplace/FundFlow/agent-handoff/_g06_verify')
from pw_common import Harness

EXPECT = ['请选择', '立项审批', '投决上会', '基金注册审批', '付款审批', '收益分配审批', '注销审批', '认定审批']

h = Harness()
try:
    # --- 3a F20 ---
    ctx, page, errs = h.open('P3-R01-原型/审批中心/P3-R01-F20-审批中心.html')
    res = page.evaluate("""
    () => {
      const modal = document.querySelector('#newModal');
      if (!modal) return {err: 'no #newModal'};
      const sels = [...modal.querySelectorAll('select')];
      const hit = sels.filter(s => [...s.options].some(o => o.text.includes('立项')));
      return hit.map(s => ({id: s.id, options: [...s.options].map(o => o.text)}));
    }
    """)
    print('F20 newModal select options:', json.dumps(res, ensure_ascii=False))
    print('F20 JS errors:', errs)
    ctx.close()
finally:
    h.close()

# --- 3c F14 static check ---
p = '/Users/bailey/Desktop/xiaohei-workplace/FundFlow/P3-R01-原型/投后管理/P3-R01-F14-提醒中心.html'
html = open(p, encoding='utf-8').read()
m = re.search(r'<select[^>]*id="rlType"[^>]*>(.*?)</select>', html, re.S)
opts = re.findall(r'<option[^>]*>([^<]*)</option>', m.group(1)) if m else None
print('F14 #rlType options:', json.dumps(opts, ensure_ascii=False), 'count:', len(opts) if opts else 0)
print('F14 has dmFillSelect call:', bool(re.search(r'dmFillSelect\s*\(', html)))
