# -*- coding: utf-8 -*-
"""复核4b：F02 项目详情概况 / F16 收益分配 / F13 风险预警 / F12 报告归档"""
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
    # ============ F02 ============
    ctx, page, errs = h.open('P3-R01-原型/项目库/P3-R01-F02-项目详情-项目概况.html')
    out['F02 条款卡'] = page.evaluate("""()=>{
      const card=document.getElementById('dmSpecTermCard');
      if(!card) return null;
      let grid=card.nextElementSibling;
      while(grid && !(grid.classList && grid.classList.contains('fgrid2'))) grid=grid.nextElementSibling;
      return {cardHead: card.innerText.replace(/\\n+/g,' | ').slice(0,120),
              nextIsFgrid2: !!grid,
              gridText: grid? grid.innerText.replace(/\\n+/g,' | ') : null};
    }""")
    out['F02 JS错误'] = errs
    ctx.close()

    # ============ F16 ============
    ctx, page, errs = h.open('P3-R01-原型/退出管理/P3-R01-F16-收益分配.html')
    out['F16 瀑布卡'] = page.evaluate("""()=>{
      const c=document.getElementById('dmWaterfallCard');
      if(!c) return null;
      const t=c.innerText.replace(/\\n+/g,' | ');
      const g=s=>t.includes(s);
      return {has800:g('800 万'), has160:g('160'), has128:g('128'), has512:g('512'), has60:g('60'), has40:g('40'), hasNote:g('静态演示顺序，BS 版按合伙协议计算'),
              text:t.slice(0,600)};
    }""")
    out['F16 JS错误'] = errs
    ctx.close()

    # ============ F13 ============
    ctx, page, errs = h.open('P3-R01-原型/投后管理/P3-R01-F13-风险预警.html')
    dialogs = []
    attach_dialogs(page, dialogs)
    before = page.evaluate("()=>({all:document.getElementById('dmCntAll').textContent, unread:document.getElementById('cntUnread').textContent, ru:document.getElementById('cntReadUntreated').textContent, done:document.getElementById('dmCntDone').textContent})")
    page.evaluate("dmOpenHandle('al2','alFoot2','alState2')")
    page.wait_for_timeout(100)
    out['F13 modal打开'] = page.evaluate("()=>document.getElementById('dmHandleModal').classList.contains('show')")
    # 空说明提交
    page.evaluate("()=>{document.getElementById('dmHandleNote').value='';}")
    page.evaluate('dmSubmitHandle()')
    page.wait_for_timeout(100)
    out['F13 空提交 alert'] = [d['message'] for d in dialogs]
    out['F13 空提交后modal仍开'] = page.evaluate("()=>document.getElementById('dmHandleModal').classList.contains('show')")
    # 填写后提交
    NOTE = 'G06复核：已联系企业补齐年报'
    page.evaluate("n=>{document.getElementById('dmHandleNote').value=n; dmSubmitHandle();}", NOTE)
    page.wait_for_timeout(150)
    out['F13 提交后'] = page.evaluate("""()=>{
      const card=document.getElementById('al2');
      const head=card.querySelector('.al-head');
      const foot=document.getElementById('alFoot2');
      const tag=head.querySelector('.tag');
      const note=foot.querySelector('.al-note');
      return {headTagText:tag?tag.textContent:null, headTagClass:tag?tag.className:null,
              headHTML:head.innerHTML.replace(/\\s+/g,' ').slice(0,300),
              footHTML:foot.innerHTML.replace(/\\s+/g,' ').slice(0,300),
              footNoteText:note?note.textContent:null, footHasAlNote:!!note,
              counts:{all:document.getElementById('dmCntAll').textContent, unread:document.getElementById('cntUnread').textContent, ru:document.getElementById('cntReadUntreated').textContent, done:document.getElementById('dmCntDone').textContent}};
    }""")
    out['F13 counts before'] = before
    out['F13 JS错误'] = errs
    ctx.close()

    # ============ F12 ============
    ctx, page, errs = h.open('P3-R01-原型/投后管理/P3-R01-F12-报告归档.html')
    out['F12 RPT-2026-021 行'] = page.evaluate("""()=>{
      const tr=[...document.querySelectorAll('tr')].find(t=>t.textContent.includes('RPT-2026-021'));
      return tr? tr.innerText.replace(/\\n+/g,' | ') : null;
    }""")
    out['F12 JS错误'] = errs
    ctx.close()
finally:
    h.close()

print(json.dumps(out, ensure_ascii=False, indent=1))
