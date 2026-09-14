# -*- coding: utf-8 -*-
"""G03/T3：查看/详情/预览/编辑类 alert 死端 → 真弹窗（页面侧：骨架＋函数＋alert 替换）"""
import os, re
ROOT = "/Users/bailey/Desktop/xiaohei-workplace/FundFlow/P3-R01-原型"
P = lambda rel: os.path.join(ROOT, rel)
MENU = '<script>\n/* ===== 菜单折叠 / 左下角系统切换（统一脚本） ===== */'

def load(rel): return open(P(rel), encoding="utf-8").read()
def save(rel, src): open(P(rel), "w", encoding="utf-8").write(src)
def must(src, sub, n=1, what=""):
    c = src.count(sub)
    assert c == n, f"[{what}] 期望 {n}，实测 {c}：{sub[:80]}"
    return src

def modal(mid, title_id, body_id, title):
    return f"""
<!-- ===== G03/T3 弹窗：查看类真弹窗（dm- 前缀，复用 .modal 骨架） ===== -->
<div class="modal-overlay" id="{mid}">
  <div class="modal">
    <div class="modal-header">
      <h3 class="modal-title" id="{title_id}">{title}</h3>
      <span class="modal-close" onclick="document.getElementById('{mid}').classList.remove('show')">×</span>
    </div>
    <div class="modal-body" id="{body_id}"></div>
    <div class="modal-footer">
      <button class="btn btn-primary" onclick="document.getElementById('{mid}').classList.remove('show')">关 闭</button>
    </div>
  </div>
</div>
"""

def row(k, v):
    return f'<div class="f-row"><label>{k}</label><div class="f-readonly">{{{v}}}</div></div>'

def sub_re(src, pattern, repl, n_expect, what):
    src2, n = re.subn(pattern, repl, src)
    assert n == n_expect, f"[{what}] 替换 {n}≠{n_expect}"
    return src2

# ================= F20 审批中心 =================
def f20():
    rel = '审批中心/P3-R01-F20-审批中心.html'
    src = load(rel)
    # apModal 附件预览按钮 → dmApAttach
    must(src, "onclick=\"alert('附件预览：投决包（3 件）')\"", 1, 'F20.attach')
    src = src.replace("onclick=\"alert('附件预览：投决包（3 件）')\"", 'onclick="dmApAttach()"', 1)
    # 详情弹窗 ×2（审批单详情 + 附件预览）
    anchor = '<script>\n/* ===== 业务脚本：三个页签面板切换'
    must(src, anchor, 1, 'F20.anchor')
    src = src.replace(anchor, modal('dmApDetailModal', 'dmApDTitle', 'dmApDBody', '审批单详情')
                      + modal('dmApAttachModal', 'dmApATitle', 'dmApABody', '附件预览') + '\n' + anchor, 1)
    tail = "    alert(no + ' 已撤回：审批终止，可修改后重新发起');\n  };\n})();"
    must(src, tail, 1, 'F20.tail')
    fn = """    alert(no + ' 已撤回：审批终止，可修改后重新发起');
  };
  /* ===== T3 审批单详情 / 附件预览 → 真弹窗（取值自单源 store） ===== */
  window.dmApDetail = function (id) {
    var S = DM.store, row = null, view = '';
    ['todo', 'cc', 'mine', 'done'].forEach(function (v) {
      if (!row) { var r = DM.byId(S.approvals[v], id); if (r) { row = r; view = v; } }
    });
    if (!row) { return; }
    document.getElementById('dmApDTitle').textContent = '审批单详情 · ' + id;
    var isDone = view === 'done';
    document.getElementById('dmApDBody').innerHTML =
      '<div class="f-row"><label>审批编号 / 类型</label><div class="f-readonly">' + id + ' · ' + row.type + '</div></div>'
      + '<div class="f-row"><label>关联业务</label><div class="f-readonly">' + row.biz + '</div></div>'
      + '<div style="display:flex;gap:12px;">'
      + '<div class="f-row" style="flex:1;"><label>发起人</label><div class="f-readonly">' + row.owner + '</div></div>'
      + '<div class="f-row" style="flex:1;"><label>发起时间</label><div class="f-readonly">' + row.time + '</div></div>'
      + '</div>'
      + '<div class="f-row"><label>当前节点</label><div class="f-readonly">' + (isDone ? '已完成' : row.node) + '</div></div>'
      + (isDone
        ? '<div class="f-row"><label>意见摘要</label><div class="f-readonly" style="white-space:normal;line-height:1.6;">' + (row.opinion || row.desc || '—') + '</div></div>'
        : (row.desc ? '<div class="f-row"><label>申请说明</label><div class="f-readonly" style="white-space:normal;line-height:1.6;">' + row.desc + '</div></div>' : ''));
    document.getElementById('dmApDetailModal').classList.add('show');
  };
  window.dmApAttach = function () {
    document.getElementById('dmApABody').innerHTML =
      '<div class="f-row"><label>附件清单 · 投决包（3 件）</label><div class="f-readonly" style="white-space:normal;line-height:1.8;">投决会议材料 · 尽调报告 · 估值建议</div></div>'
      + '<div class="f-hint">演示原型：附件在线预览为占位说明，正式版支持 PDF 在线翻阅</div>';
    document.getElementById('dmApAttachModal').classList.add('show');
  };
})();"""
    src = src.replace(tail, fn, 1)
    save(rel, src)
    print("OK F20（附件预览1处＋详情弹窗）")

# ================= F19 放弃原因分布 =================
def f19():
    rel = '统计报表/P3-R01-F19-放弃原因分布.html'
    src = load(rel)
    anchor = '<script>\n/* ===== 业务脚本：三维过滤'
    must(src, anchor, 1, 'F19.anchor')
    src = src.replace(anchor, modal('dmAbModal', 'dmAbTitle', 'dmAbBody', '未投归档详情') + '\n' + anchor, 1)
    tail = "  DM.renderList('F19.detail');\n})();"
    must(src, tail, 1, 'F19.tail')
    fn = """  DM.renderList('F19.detail');

  /* ===== T3 未投归档详情 → 真弹窗（取值自 abandons 单源） ===== */
  window.dmAbDetail = function (name) {
    var a = DM.byId(DM.store.abandons, name);
    if (!a) { return; }
    var sub = a.subject === 'gp' ? 'GP 放弃（管理人主动）' : 'LP 否决（投决会）';
    document.getElementById('dmAbTitle').textContent = name + ' · 未投归档详情';
    document.getElementById('dmAbBody').innerHTML =
      '<div class="f-row"><label>项目</label><div class="f-readonly">' + name + '</div></div>'
      + '<div class="f-row"><label>放弃主体</label><div class="f-readonly">' + sub + '</div></div>'
      + '<div class="f-row"><label>放弃节点</label><div class="f-readonly">' + a.nodeLabel + '</div></div>'
      + '<div class="f-row"><label>末级原因</label><div class="f-readonly">' + a.reason + '</div></div>'
      + '<div class="f-row"><label>自定义补充</label><div class="f-readonly" style="white-space:normal;line-height:1.6;">' + a.custom + '</div></div>'
      + '<div style="display:flex;gap:12px;">'
      + '<div class="f-row" style="flex:1;"><label>最近发生</label><div class="f-readonly">' + a.date + '</div></div>'
      + '<div class="f-row" style="flex:1;"><label>关联项目编号</label><div class="f-readonly">' + (a.prj || '—') + '</div></div>'
      + '</div>'
      + '<div class="f-hint">未投归档不可回流管道；如再接触需按新项目建档</div>';
    document.getElementById('dmAbModal').classList.add('show');
  };
})();"""
    src = src.replace(tail, fn, 1)
    save(rel, src)
    print("OK F19")

# ================= F15 项目退出 =================
def f15():
    rel = '退出管理/P3-R01-F15-项目退出.html'
    src = load(rel)
    anchor = '<script>\n/* ===== 业务脚本：项目切换 + 自动计算'
    must(src, anchor, 1, 'F15.anchor')
    src = src.replace(anchor, modal('dmBatModal', 'dmBatTitle', 'dmBatBody', '批次详情') + '\n' + anchor, 1)
    # openBatModal 重置编辑态
    must(src, 'function openBatModal() {', 1, 'F15.openBat')
    src = src.replace('function openBatModal() {',
                      "function openBatModal() {\n  window.dmEditId = null;\n  document.querySelector('#batModal .modal-title').textContent = '登记退出批次';\n  document.querySelector('#batModal .modal-footer .btn-primary').textContent = '确认登记';", 1)
    # dmSubmitBatch 分流编辑态
    must(src, 'window.dmSubmitBatch = function () {', 1, 'F15.submit')
    src = src.replace('window.dmSubmitBatch = function () {',
                      'window.dmSubmitBatch = function () {\n    if (window.dmEditId) { dmSaveBatEdit(); return; }', 1)
    tail = "    closeBatModal();\n    alert('已登记退出批次');\n  };\n})();"
    must(src, tail, 1, 'F15.tail')
    fn = """    closeBatModal();
    alert('已登记退出批次');
  };
  /* ===== T3 批次详情 → 真弹窗；编辑批次 → 复用登记弹窗预填该行 ===== */
  window.dmBatDetail = function (id) {
    var b = DM.byId(DM.store.batches, id);
    if (!b) { return; }
    document.getElementById('dmBatTitle').textContent = '批次详情 · ' + id;
    document.getElementById('dmBatBody').innerHTML =
      '<div class="f-row"><label>批次编号 / 类型</label><div class="f-readonly">' + id + ' · ' + b.type + '</div></div>'
      + '<div style="display:flex;gap:12px;">'
      + '<div class="f-row" style="flex:1;"><label>退出价格（元/份）</label><div class="f-readonly">' + b.price + '</div></div>'
      + '<div class="f-row" style="flex:1;"><label>数量（万份）</label><div class="f-readonly">' + b.qty + '</div></div>'
      + '</div>'
      + '<div class="f-row"><label>退出金额 / 退出日期</label><div class="f-readonly">' + b.amount + ' 万元 · ' + b.date + '</div></div>'
      + '<div class="f-row"><label>分摊本金 / 批次收益 / 收益率</label><div class="f-readonly">' + b.principal + ' 万 · ' + b.gain + ' 万 · ' + b.rate + '</div></div>'
      + '<div class="f-row"><label>状态</label><div class="f-readonly">' + b.status + '</div></div>'
      + '<div class="f-hint" style="white-space:normal;line-height:1.6;">' + b.detail + '</div>';
    document.getElementById('dmBatModal').classList.add('show');
  };
  window.dmEditBat = function (id) {
    var b = DM.byId(DM.store.batches, id);
    if (!b) { return; }
    window.dmEditId = id;
    document.querySelector('#batModal .modal-title').textContent = '编辑批次 · ' + id;
    document.querySelector('#batModal .modal-footer .btn-primary').textContent = '保存修改';
    var sel = document.getElementById('exType');
    for (var i = 0; i < sel.options.length; i++) {
      if (sel.options[i].text === b.type) { sel.selectedIndex = i; break; }
    }
    document.getElementById('exPrice').value = String(parseFloat(String(b.price).replace('预计', '')) || 0);
    document.getElementById('exQty').value = String(parseFloat(String(b.qty).replace('预计', '')) || 0);
    var d = String(b.date).match(/\\d{4}-\\d{2}-\\d{2}/);
    document.getElementById('exDate').value = d ? d[0] : '2026-08-27';
    calcExit();
    document.getElementById('batModal').classList.add('show');
  };
  window.dmSaveBatEdit = function () {
    var b = DM.byId(DM.store.batches, window.dmEditId);
    var price = parseFloat(document.getElementById('exPrice').value) || 0;
    var qty = parseFloat(document.getElementById('exQty').value) || 0;
    if (!(price > 0 && qty > 0)) { alert('请填写退出价格与数量'); return; }
    var typeSel = document.getElementById('exType');
    var date = document.getElementById('exDate').value || '2026-08-27';
    if (b) {
      b.type = typeSel.options[typeSel.selectedIndex].text;
      b.typeCls = b.type === 'IPO 减持' ? 'tag-orange' : 'tag-blue';
      b.price = dmFmtNum(price); b.qty = dmFmtNum(qty);
      b.amount = dmFmtNum(price * qty); b.principal = dmFmtNum(qty * 2);
      b.gain = dmFmtNum(price * qty - qty * 2); b.date = date;
      b.rate = qty * 2 > 0 ? ((price * qty - qty * 2) / (qty * 2) * 100).toFixed(1) + '%' : '—';
      b.detail = b.type + ' ' + b.qty + ' 万份 × ' + b.price + ' 元/份 = ' + b.amount + ' 万元，' + date + ' 修改（待执行）';
      b.tr = '<tr>'
        + '<td><span class="lk" onclick="dmBatDetail(\\'' + b.id + '\\')">' + b.id + '</span></td>'
        + '<td><span class="tag ' + b.typeCls + '">' + b.type + '</span></td>'
        + '<td>' + b.price + '</td><td>' + b.qty + '</td><td>' + b.amount + '</td><td>' + b.date + '</td>'
        + '<td>' + b.principal + '</td><td class="' + b.gainCls + '">' + b.gain + '</td><td>' + b.rate + '</td>'
        + '<td><span class="tag tag-orange">待执行</span></td>'
        + '<td class="sticky-op ops"><a onclick="dmBatDetail(\\'' + b.id + '\\')">查看</a><a onclick="dmEditBat(\\'' + b.id + '\\')">编辑</a></td>'
        + '</tr>';
      DM.renderList('F15.bat');
    }
    window.dmEditId = null;
    document.querySelector('#batModal .modal-title').textContent = '登记退出批次';
    document.querySelector('#batModal .modal-footer .btn-primary').textContent = '确认登记';
    closeBatModal();
    alert('批次已保存');
  };
})();"""
    src = src.replace(tail, fn, 1)
    # T2 新增行（未带弹窗函数）补挂 T3 处理：查看/编辑
    old_ops = "'<td class=\"sticky-op ops\"><a>查看</a><a>编辑</a></td>'"
    must(src, old_ops, 1, 'F15.newRowOps')
    src = src.replace(old_ops,
                      "'<td class=\"sticky-op ops\"><a onclick=\"dmBatDetail(\\\\'' + b.id + '\\\\')\">查看</a><a onclick=\"dmEditBat(\\\\'' + b.id + '\\\\')\">编辑</a></td>'", 1)
    save(rel, src)
    print("OK F15")

# ================= F01 项目列表 =================
def f01():
    rel = '项目库/P3-R01-F01-项目列表.html'
    src = load(rel)
    anchor = '      <button class="btn btn-primary" onclick="dmConfirmAdvance()">确认推进</button>\n    </div>\n  </div>\n</div>'
    must(src, anchor, 1, 'F01.anchor')
    src = src.replace(anchor, anchor + '\n' + modal('dmStallModal', 'dmStallTitle', 'dmStallBody', '停滞处置标注'), 1)
    tail = "    closeAbandon();\n    alert('已登记并转入「未投归档」');\n  };\n})();"
    must(src, tail, 1, 'F01.tail')
    fn = """    closeAbandon();
    alert('已登记并转入「未投归档」');
  };
  /* ===== T3 停滞处置标注（点名改造）→ 真弹窗 ===== */
  window.dmStallNote = function (id) {
    var p = DM.byId(DM.store.projects, id);
    if (!p) { return; }
    document.getElementById('dmStallTitle').textContent = '停滞处置 · ' + p.name;
    document.getElementById('dmStallBody').innerHTML =
      '<div class="f-row"><label>项目 / 当前阶段</label><div class="f-readonly">' + p.id + ' · ' + p.stage + '</div></div>'
      + '<div class="f-row"><label>处置标注</label><div class="f-readonly" style="white-space:normal;line-height:1.6;">对方同时对接其他资金方，保持沟通中</div></div>'
      + '<div class="f-hint">停滞≠放弃：项目留在管道；可推送提醒给负责人（原「已推送停滞提醒」入口保留）</div>';
    document.getElementById('dmStallModal').classList.add('show');
  };
})();"""
    src = src.replace(tail, fn, 1)
    save(rel, src)
    print("OK F01")

# ================= F12 报告归档 =================
def f12():
    rel = '投后管理/P3-R01-F12-报告归档.html'
    src = load(rel)
    anchor = '<script>\n/* ===== 业务脚本：上传报告'
    must(src, anchor, 1, 'F12.anchor')
    src = src.replace(anchor, modal('dmRptModal', 'dmRptTitle', 'dmRptBody', '报告预览') + '\n' + anchor, 1)
    # dmSubmitReport 新增行/消解行的 预览 → dmViewReport
    old_nr = "'<td class=\"sticky-op ops\"><a onclick=\"alert(\\'打开报告预览\\')\">预览</a><a onclick=\"alert(\\'已开始下载\\')\">下载</a></td>'"
    must(src, old_nr, 1, 'F12.newRow')
    src = src.replace(old_nr,
                      "'<td class=\"sticky-op ops\"><a onclick=\"dmViewReport(\\\\'' + id + '\\\\')\">预览</a><a onclick=\"alert(\\'已开始下载\\')\">下载</a></td>'", 1)
    old_st = ".replace(/<a onclick=\"openUpload\\([^)]*\\)\">上传<\\/a>/, '<a onclick=\"alert(\\'打开报告预览\\')\">预览</a><a onclick=\"alert(\\'已开始下载\\')\">下载</a>')"
    must(src, old_st, 1, 'F12.settle')
    src = src.replace(old_st,
                      ".replace(/<a onclick=\"openUpload\\([^)]*\\)\">上传<\\/a>/, '<a onclick=\"dmViewReport(\\\\'' + r.id + '\\\\')\">预览</a><a onclick=\"alert(\\'已开始下载\\')\">下载</a>')", 1)
    tail = "    closeUpload();\n    alert('已归档');\n  };\n})();"
    must(src, tail, 1, 'F12.tail')
    fn = """    closeUpload();
    alert('已归档');
  };
  /* ===== T3 报告预览 → 真弹窗（取值自 reports 单源 / 行 DOM） ===== */
  window.dmViewReport = function (id) {
    var r = DM.byId(DM.store.reports, id);
    if (!r) {
      var tds = null;
      document.querySelectorAll('#dmBody tr').forEach(function (tr) {
        if (tr.textContent.indexOf(id) > -1) { tds = tr.querySelectorAll('td'); }
      });
      if (!tds) { return; }
      r = { id: id, prj: tds[1].textContent.trim(), type: tds[2].textContent.trim(), period: tds[3].textContent.trim(), status: tds[7].textContent.trim() };
    }
    document.getElementById('dmRptTitle').textContent = '报告预览 · ' + id;
    document.getElementById('dmRptBody').innerHTML =
      '<div class="f-row"><label>报告编号 / 类型</label><div class="f-readonly">' + r.id + ' · ' + r.type + '</div></div>'
      + '<div class="f-row"><label>项目 / 报告期</label><div class="f-readonly">' + r.prj + ' · ' + r.period + '</div></div>'
      + '<div class="f-row"><label>状态</label><div class="f-readonly">' + r.status + '</div></div>'
      + '<div class="f-hint">演示原型：报告在线预览为占位说明，正式版支持 PDF 翻阅与下载</div>';
    document.getElementById('dmRptModal').classList.add('show');
  };
})();"""
    src = src.replace(tail, fn, 1)
    save(rel, src)
    print("OK F12")

# ================= F16 收益分配 =================
def f16():
    rel = '退出管理/P3-R01-F16-收益分配.html'
    src = load(rel)
    anchor = '<script>\n/* ===== 业务脚本：子行展开'
    must(src, anchor, 1, 'F16.anchor')
    src = src.replace(anchor, modal('dmDstModal', 'dmDstTitle', 'dmDstBody', '分配单详情') + '\n' + anchor, 1)
    tail = "  DM.renderList('F16.dst');\n})();"
    must(src, tail, 1, 'F16.tail')
    fn = """  DM.renderList('F16.dst');

  /* ===== T3 分配单详情 / 付款凭证 → 真弹窗（取值自 distributions 单源） ===== */
  window.dmDstDetail = function () {
    var d = DM.store.distributions[0];
    if (!d) { return; }
    document.getElementById('dmDstTitle').textContent = '分配单详情 · ' + d.id;
    document.getElementById('dmDstBody').innerHTML =
      '<div class="f-row"><label>分配单编号</label><div class="f-readonly">' + d.id + ' · 分配中</div></div>'
      + '<div class="f-row"><label>来源批次</label><div class="f-readonly" style="white-space:normal;line-height:1.6;">' + d.src + '</div></div>'
      + '<div class="f-row"><label>分配明细</label><div class="f-readonly" style="white-space:normal;line-height:1.6;">' + d.detail + '</div></div>'
      + '<div class="f-hint">分配金额按 LP 出资比例预填，合计须与可分配金额一致</div>';
    document.getElementById('dmDstModal').classList.add('show');
  };
  window.dmVoucher = function () {
    var d = DM.store.distributions[0];
    document.getElementById('dmDstTitle').textContent = '付款凭证';
    document.getElementById('dmDstBody').innerHTML =
      '<div class="f-row"><label>凭证文件</label><div class="f-readonly">' + (d ? d.voucher : '—') + '</div></div>'
      + '<div class="f-hint">演示原型：凭证在线预览为占位说明，正式版支持图片 / PDF 查验</div>';
    document.getElementById('dmDstModal').classList.add('show');
  };
})();"""
    src = src.replace(tail, fn, 1)
    save(rel, src)
    print("OK F16")

# ================= F17 清算注销（无既有弹窗骨架 → dm- 迷你骨架） =================
F17_CSS = """
/* ===== G03/T3 弹窗（F17 无既有弹窗骨架，dm- 迷你骨架，样式对齐全站 modal 体系） ===== */
.dm-overlay { position:fixed; inset:0; background:rgba(15,23,42,.5); backdrop-filter:blur(2px); display:none; align-items:center; justify-content:center; z-index:1000; }
.dm-overlay.show { display:flex; }
.dm-box { background:#fff; border-radius:12px; width:440px; max-height:80vh; overflow-y:auto; box-shadow:0 12px 36px -8px rgba(16,24,40,.2); }
.dm-head { padding:16px 24px; border-bottom:1px solid #f0f0f0; display:flex; justify-content:space-between; align-items:center; }
.dm-head h3 { position:relative; padding-left:11px; font-size:16px; font-weight:600; color:#1a1a1a; margin:0; }
.dm-head h3::before { content:''; position:absolute; left:0; top:3px; bottom:3px; width:3px; border-radius:2px; background:#1677ff; }
.dm-x { cursor:pointer; font-size:20px; color:#8c8c8c; line-height:1; }
.dm-body { padding:20px 24px; font-size:13px; color:#262626; line-height:1.7; }
.dm-foot { padding:12px 24px; border-top:1px solid #f0f0f0; display:flex; justify-content:flex-end; }
.dm-btn { height:30px; padding:0 15px; border-radius:6px; font-size:12px; cursor:pointer; border:1px solid #1677ff; background:#1677ff; color:#fff; }
"""

def f17():
    rel = '退出管理/P3-R01-F17-清算注销.html'
    src = load(rel)
    i = src.index('</style>')
    src = src[:i] + F17_CSS + src[i:]
    anchor = '<script>\n/* ===== 业务脚本：基金三态联动'
    must(src, anchor, 1, 'F17.anchor')
    mhtml = """
<!-- ===== G03/T3 弹窗：材料预览（dm- 迷你骨架） ===== -->
<div class="dm-overlay" id="dmDocModal">
  <div class="dm-box">
    <div class="dm-head"><h3 id="dmDocTitle">材料预览</h3><span class="dm-x" onclick="document.getElementById('dmDocModal').classList.remove('show')">×</span></div>
    <div class="dm-body" id="dmDocBody"></div>
    <div class="dm-foot"><button class="dm-btn" onclick="document.getElementById('dmDocModal').classList.remove('show')">关 闭</button></div>
  </div>
</div>

"""
    src = src.replace(anchor, mhtml + anchor, 1)
    # renderFund 模板内 alert(\'材料预览：'+d.name+'\') → dmFileView
    old_al = "alert(\\'材料预览：' + d.name + '\\')"
    must(src, old_al, 1, 'F17.alert')
    src = src.replace(old_al, "dmFileView(\\'材料预览\\', ' + d.name + ')")
    script = """<script>
/* ===== G03/T3 材料预览真弹窗（dm- 前缀） ===== */
function dmFileView(title, name) {
  document.getElementById('dmDocTitle').textContent = title + ' · ' + name;
  document.getElementById('dmDocBody').innerHTML =
    '<div style="margin-bottom:10px;color:#595959;">文件：' + name + '</div>'
    + '<div style="color:#8c8c8c;font-size:12px;">演示原型：材料在线预览为占位说明，正式版支持 PDF 翻阅</div>';
  document.getElementById('dmDocModal').classList.add('show');
}
</script>

"""
    must(src, MENU, 1, 'F17.menu')
    src = src.replace(MENU, script + MENU, 1)
    save(rel, src)
    print("OK F17")

# ================= F08 / F11（文件/附件预览，静态页） =================
def file_page(rel, page, pattern, repl, n_expect, title):
    src = load(rel)
    src = sub_re(src, pattern, repl, n_expect, page + '.alerts')
    m = modal('dmFileModal', 'dmFTitle', 'dmFBody', title)
    script = """<script>
/* ===== G03/T3 预览真弹窗（dm- 前缀，静态页无单源，取值取自点击参数） ===== */
function dmFileView(title, name) {
  document.getElementById('dmFTitle').textContent = title + ' · ' + name;
  document.getElementById('dmFBody').innerHTML =
    '<div class="f-row"><label>文件</label><div class="f-readonly">' + name + '</div></div>'
    + '<div class="f-hint">演示原型：文件在线预览为占位说明，正式版支持 PDF / 扫描件翻阅与下载</div>';
  document.getElementById('dmFileModal').classList.add('show');
}
</script>

"""
    must(src, MENU, 1, page + '.menu')
    src = src.replace(MENU, m + '\n' + script + MENU, 1)
    save(rel, src)
    print(f"OK {page}")

def f08():
    file_page('基金管理/P3-R01-F08-基金详情.html', 'F08',
              r"alert\('预览：([^']+)'\)", r"dmFileView('文件预览', '\1')", 4, '文件预览')

def f11():
    file_page('投后管理/P3-R01-F11-投后事项.html', 'F11',
              r"alert\('打开附件：([^']+)'\)", r"dmFileView('附件预览', '\1')", 2, '附件预览')

# ================= F09 资质材料（静态页） =================
def f09():
    rel = 'LP 管理/P3-R01-F09-LP台账.html'
    src = load(rel)
    src = sub_re(src, r"alert\('查看资质材料：([^']+)'\)", r"dmMatView('\1')", 4, 'F09.alerts')
    m = modal('dmMatModal', 'dmMTitle', 'dmMBody', '资质材料')
    script = """<script>
/* ===== G03/T3 查看资质材料 → 真弹窗（dm- 前缀） ===== */
function dmMatView(list) {
  document.getElementById('dmMTitle').textContent = '资质材料';
  var items = list.split('、').map(function (s) { return s.replace(/等 \\d+ 份$/, '').trim(); }).filter(Boolean);
  var lis = items.map(function (t) { return '<div class="f-readonly">📄 ' + t + '</div>'; }).join('<div style="height:8px;"></div>');
  document.getElementById('dmMBody').innerHTML =
    '<div class="f-row"><label>材料清单</label>' + lis + '</div>'
    + '<div class="f-hint">演示原型：材料在线预览为占位说明；资质材料仅认定人与管理员可见</div>';
  document.getElementById('dmMatModal').classList.add('show');
}
</script>

"""
    must(src, MENU, 1, 'F09.menu')
    src = src.replace(MENU, m + '\n' + script + MENU, 1)
    save(rel, src)
    print("OK F09")

# ================= F21 系统管理（45 处 编辑数据项 → 复用 dictItemModal） =================
def f21():
    rel = '系统管理/P3-R01-F21-系统管理.html'
    src = load(rel)
    src = sub_re(src, r"alert\('编辑数据项：([^']+)'\)", r"dmEditDict('\1')", 45, 'F21.alerts')
    script = """<script>
/* ===== G03/T3 编辑数据项 → 复用新增数据项弹窗预填（dm- 前缀） ===== */
function dmEditDict(name) {
  openDictItem();
  document.querySelector('#dictItemModal .modal-title').textContent = '编辑数据项';
  document.getElementById('diName').value = name;
}
</script>

"""
    must(src, MENU, 1, 'F21.menu')
    src = src.replace(MENU, script + MENU, 1)
    save(rel, src)
    print("OK F21")

import sys
ONLY = sys.argv[1].split(',') if len(sys.argv) > 1 else None
for fn in (f20, f19, f15, f01, f12, f16, f17, f08, f11, f09, f21):
    if ONLY and fn.__name__ not in ONLY:
        continue
    try:
        fn()
    except AssertionError as e:
        print(f"FAIL {fn.__name__}: {e}")
        raise
print("T3 页面改造完成")
