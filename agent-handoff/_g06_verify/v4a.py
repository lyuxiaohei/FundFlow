# -*- coding: utf-8 -*-
"""复核4a：F09 LP台账 / F15 项目退出 / F08 基金详情"""
import sys, json
sys.path.insert(0, '/Users/bailey/Desktop/xiaohei-workplace/FundFlow/agent-handoff/_g06_verify')
from pw_common import Harness

def attach_dialogs(page, logs):
    def on_dialog(d):
        logs.append({'type': d.type, 'message': d.message})
        if d.type == 'prompt':
            d.accept('复核取消原因')
        else:
            d.accept()
    page.on('dialog', on_dialog)

h = Harness()
out = {}
try:
    # ============ F09 ============
    ctx, page, errs = h.open('P3-R01-原型/LP 管理/P3-R01-F09-LP台账.html')
    dialogs = []
    attach_dialogs(page, dialogs)
    page.evaluate("openVerify('宁波梅山远见投资有限公司')")
    page.wait_for_timeout(150)
    out['F09 dmQualValid'] = page.eval_on_selector('#dmQualValid', 'e=>e.textContent')
    out['F09 主按钮'] = page.evaluate("()=>[...document.querySelectorAll('#verifyModal .btn-primary')].map(b=>b.textContent.trim())")
    page.evaluate('confirmVerify()')
    page.wait_for_timeout(150)
    out['F09 confirmVerify alert'] = dialogs
    out['F09 JS错误'] = errs
    ctx.close()

    # ============ F15 ============
    ctx, page, errs = h.open('P3-R01-原型/退出管理/P3-R01-F15-项目退出.html')
    dialogs = []
    attach_dialogs(page, dialogs)
    out['F15 dmStRemainS'] = page.eval_on_selector('#dmStRemainS', 'e=>e.textContent')
    page.evaluate('openBatModal()')
    page.wait_for_timeout(100)
    page.select_option('#exType', label='IPO 减持')
    page.wait_for_timeout(100)
    out['F15 IPO可见'] = page.evaluate("()=>{const b=document.getElementById('dmCompBlock');return {cls:b.className, display:getComputedStyle(b).display, visible:!!b.offsetParent||getComputedStyle(b).display!=='none'}}")
    page.select_option('#exType', label='股权转让')
    page.wait_for_timeout(100)
    out['F15 转让隐藏'] = page.evaluate("()=>{const b=document.getElementById('dmCompBlock');return {display:getComputedStyle(b).display, visible:!!b.offsetParent}}")
    out['F15 元素在位'] = page.evaluate("()=>['dmCkLock','dmCkDisc','dmCkQuota','dmReviewer'].map(id=>({id, tag:document.getElementById(id).tagName}))")
    # IPO 未全勾 → dmCompCheck false + 从严拦截
    page.select_option('#exType', label='IPO 减持')
    page.evaluate("()=>{['dmCkLock','dmCkDisc','dmCkQuota'].forEach(id=>document.getElementById(id).checked=false); document.getElementById('dmReviewer').value='';}")
    ret = page.evaluate('dmCompCheck()')
    page.wait_for_timeout(100)
    out['F15 dmCompCheck返回'] = ret
    out['F15 compCheck alert'] = [d['message'] for d in dialogs]
    # BAT-2026-002 行操作列
    out['F15 BAT-2026-002 操作列'] = page.evaluate("""()=>{
      const tr=[...document.querySelectorAll('tr')].find(t=>t.textContent.includes('BAT-2026-002'));
      return tr? [...tr.cells].map(c=>c.textContent.trim()) : null;
    }""")
    # dmDeferBat
    dialogs.clear()
    page.evaluate("dmDeferBat('BAT-2026-002')")
    page.wait_for_timeout(100)
    out['F15 defer alert'] = [d['message'] for d in dialogs]
    # dmCancelBat (prompt)
    dialogs.clear()
    page.evaluate("dmCancelBat('BAT-2026-002')")
    page.wait_for_timeout(150)
    out['F15 cancel alert'] = [d['message'] for d in dialogs]
    out['F15 取消后行'] = page.evaluate("""()=>{
      const tr=[...document.querySelectorAll('tr')].find(t=>t.textContent.includes('BAT-2026-002'));
      if(!tr) return null;
      const c10=tr.cells[9];
      const tag=c10?c10.querySelector('.tag'):null;
      return {cells:tr.cells.length, col10:c10?c10.textContent.trim():null, tagText:tag?tag.textContent:null, tagClass:tag?tag.className:null};
    }""")
    out['F15 JS错误'] = errs
    ctx.close()

    # ============ F08 ============
    ctx, page, errs = h.open('P3-R01-原型/基金管理/P3-R01-F08-基金详情.html')
    dialogs = []
    attach_dialogs(page, dialogs)
    out['F08 水位卡'] = page.evaluate("()=>({commit:document.getElementById('dmWcCommit').textContent, paid:document.getElementById('dmWcPaid').textContent, invested:document.getElementById('dmWcInvested').textContent, remain:document.getElementById('dmWcRemain').textContent})")
    page.evaluate('dmCallRemind()')
    page.wait_for_timeout(150)
    out['F08 modal可见'] = page.evaluate("()=>document.getElementById('dmCallModal').classList.contains('show')")
    out['F08 dmCallBody'] = page.evaluate("()=>({rows:document.querySelectorAll('#dmCallBody tr').length, text:document.getElementById('dmCallBody').innerText.replace(/\\n/g,' | ')})")
    dialogs.clear()
    page.evaluate('dmSendCall()')
    page.wait_for_timeout(100)
    out['F08 sendCall alert'] = [d['message'] for d in dialogs]
    out['F08 JS错误'] = errs
    ctx.close()
finally:
    h.close()

print(json.dumps(out, ensure_ascii=False, indent=1))
