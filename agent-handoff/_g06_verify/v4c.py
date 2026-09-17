# -*- coding: utf-8 -*-
"""复核4c：F20 审批中心 / F07 基金列表 / F00 工作台 / F01 项目列表"""
import sys, json
sys.path.insert(0, '/Users/bailey/Desktop/xiaohei-workplace/FundFlow/agent-handoff/_g06_verify')
from pw_common import Harness

def attach_dialogs(page, logs):
    def on_dialog(d):
        logs.append({'type': d.type, 'message': d.message})
        d.accept()
    page.on('dialog', on_dialog)

h = Harness()
out = {}
try:
    # ============ F20 ============
    ctx, page, errs = h.open('P3-R01-原型/审批中心/P3-R01-F20-审批中心.html')
    dialogs = []
    attach_dialogs(page, dialogs)
    page.evaluate("openApproval('APV-2026-0037','投决上会','聚变能源科技 PRJ-2026-0001','吕道远','2026-08-27','投决会','x')")
    page.wait_for_timeout(150)
    out['F20 apOwner'] = page.eval_on_selector('#apOwner', 'e=>e.value!==undefined?e.value:e.textContent')
    out['F20 dmApApprover'] = page.eval_on_selector('#dmApApprover', 'e=>e.value!==undefined?e.value:e.textContent')
    out['F20 todo 0040'] = page.evaluate("()=>DM.store.approvals.todo.filter(a=>a.id==='APV-2026-0040').map(a=>({id:a.id,type:a.type,node:a.node}))")
    out['F20 dmBodyTodo rows'] = page.evaluate("()=>document.querySelectorAll('#dmBodyTodo tr').length")
    out['F20 JS错误'] = errs
    ctx.close()

    # ============ F07 ============
    ctx, page, errs = h.open('P3-R01-原型/基金管理/P3-R01-F07-基金列表.html')
    out['F07 香港远航行'] = page.evaluate("""()=>{
      const tr=[...document.querySelectorAll('tr')].find(t=>t.textContent.includes('香港远航'));
      return tr? tr.innerText.replace(/\\n+/g,' | ') : null;
    }""")
    out['F07 JS错误'] = errs
    ctx.close()

    # ============ F00 ============
    ctx, page, errs = h.open('P3-R01-原型/工作台/P3-R01-F00-工作台.html')
    out['F00 stalls'] = page.evaluate("""()=>{
      const items=[...document.querySelectorAll('.stall-item')];
      return {count:items.length, texts:items.map(i=>i.innerText.replace(/\\n+/g,' | ')), has磐石量子:document.body.innerText.includes('磐石量子')};
    }""")
    out['F00 JS错误'] = errs
    ctx.close()

    # ============ F01 ============
    ctx, page, errs = h.open('P3-R01-原型/项目库/P3-R01-F01-项目列表.html')
    dialogs = []
    attach_dialogs(page, dialogs)
    out['F01 arch数'] = page.evaluate("()=>DM.store.projects.filter(p=>p.ops==='arch').length")
    out['F01 arch行挂接'] = page.evaluate("""()=>{
      const archNames=DM.store.projects.filter(p=>p.ops==='arch').map(p=>p.name);
      const res=[];
      for(const name of archNames){
        const tr=[...document.querySelectorAll('tr')].find(t=>t.textContent.includes(name));
        if(!tr){res.push({name, tr:false}); continue;}
        const abLink=[...tr.querySelectorAll('a')].find(a=>a.textContent.includes('归档详情'));
        const lk=[...tr.querySelectorAll('.lk,a')].find(a=>a.textContent.trim()===name);
        res.push({name, abOnclick:abLink?abLink.getAttribute('onclick'):null, lkOnclick:lk?lk.getAttribute('onclick'):null});
      }
      return res;
    }""")
    page.evaluate("dmAbDetail('晶彩光电')")
    page.wait_for_timeout(150)
    out['F01 dmAbModal'] = page.evaluate("""()=>{
      const m=document.getElementById('dmAbModal');
      if(!m) return null;
      const t=m.querySelector('.modal-title,h3,h4,.m-title,[class*=title]');
      return {show:m.classList.contains('show'), title:t?t.textContent:null, bodyHead:m.innerText.split('\\n').slice(0,6).join(' | ')};
    }""")
    out['F01 JS错误'] = errs
    ctx.close()
finally:
    h.close()

print(json.dumps(out, ensure_ascii=False, indent=1))
