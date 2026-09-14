# -*- coding: utf-8 -*-
"""G03/T2：页内动作真联动——F20 审批三态迁移/撤回，F01 推进/放弃，F15 登记批次新增行，F12 上传报告新增行"""
import os
ROOT = "/Users/bailey/Desktop/xiaohei-workplace/FundFlow/P3-R01-原型"
P = lambda rel: os.path.join(ROOT, rel)

def load(rel): return open(P(rel), encoding="utf-8").read()
def save(rel, src): open(P(rel), "w", encoding="utf-8").write(src)
def must(src, sub, n=1, what=""):
    c = src.count(sub)
    assert c == n, f"[{what}] 期望 {n}，实测 {c}：{sub[:80]}"
    return src

# ================= F20 审批中心：三态迁移＋撤回 =================
def f20():
    rel = '审批中心/P3-R01-F20-审批中心.html'
    src = load(rel)
    # openApproval 记录当前审批单号（提交时迁移用）
    must(src, "function openApproval(no, type, biz, owner, time, node, desc) {", 1, 'F20.openApproval')
    src = src.replace("function openApproval(no, type, biz, owner, time, node, desc) {",
                      "function openApproval(no, type, biz, owner, time, node, desc) {\n  window.dmCurAp = no;", 1)
    # submitAp 提交时先迁移（徽章/行/页码由 renderList 的 after 联动）
    must(src, "  closeAp();\n  if (kind === 'pass') {", 1, 'F20.submitAp')
    src = src.replace("  closeAp();\n  if (kind === 'pass') {",
                      "  dmMigrateAp(kind);\n  closeAp();\n  if (kind === 'pass') {", 1)
    # G03 接入块尾部追加迁移/撤回函数
    tail = "    DM.renderList('F20.' + v[0]);\n  });\n})();"
    must(src, tail, 1, 'F20.config')
    fn = """    DM.renderList('F20.' + v[0]);
  });
  /* ===== T2 审批三态迁移：待我审批 → 我已审批（徽章计数与页码随 renderList 联动） ===== */
  window.dmMigrateAp = function (kind) {
    var no = window.dmCurAp;
    if (!no) { return; }
    window.dmCurAp = null;
    var S = DM.store;
    var idx = -1;
    for (var i = 0; i < S.approvals.todo.length; i++) { if (S.approvals.todo[i].id === no) { idx = i; break; } }
    if (idx < 0) { return; }
    var ap = S.approvals.todo.splice(idx, 1)[0];
    var ACT = { pass: ['通过', 'tag-blue'], return: ['退回', 'tag-orange'], veto: ['否决', 'tag-red'] }[kind] || ['通过', 'tag-blue'];
    var opinion = document.getElementById('apOpinion').value.trim() || (kind === 'pass' ? '同意' : '—');
    var done = { id: ap.id, type: ap.type, biz: ap.biz, owner: ap.owner, action: ACT[0], time2: '2026-08-27', opinion: opinion };
    done.tr = '<tr>'
      + '<td><span class="lk">' + ap.id + '</span></td>'
      + '<td><span class="tag tag-blue">' + ap.type + '</span></td>'
      + '<td class="biz-cell">' + (ap.bizHtml || DM.esc(ap.biz)) + '</td>'
      + '<td>' + ap.owner + '</td>'
      + '<td><span class="tag ' + ACT[1] + '">' + ACT[0] + '</span></td>'
      + '<td>2026-08-27</td>'
      + '<td>' + DM.esc(opinion) + '</td>'
      + '</tr>';
    S.approvals.done.unshift(done);
    DM.renderList('F20.todo');
    DM.renderList('F20.done');
  };
  /* ===== T2 撤回：该审批单自「待我审批/我发起的」移除，计数联动 ===== */
  window.dmWithdraw = function (no) {
    var S = DM.store;
    ['todo', 'mine'].forEach(function (v) {
      S.approvals[v] = S.approvals[v].filter(function (r) { return r.id !== no; });
    });
    DM.renderList('F20.todo'); DM.renderList('F20.mine');
    alert(no + ' 已撤回：审批终止，可修改后重新发起');
  };
})();"""
    src = src.replace(tail, fn, 1)
    save(rel, src)
    print("OK F20")

# ================= F01 项目列表：推进弹窗＋放弃归档 =================
ADV_MODAL = """
<!-- ===== G03 弹窗3：推进确认（dm- 前缀，T2 页内真联动） ===== -->
<div class="modal-overlay" id="dmAdvModal">
  <div class="modal">
    <div class="modal-header">
      <h3 class="modal-title">推进确认</h3>
      <span class="modal-close" onclick="dmCloseAdv()">×</span>
    </div>
    <div class="modal-body">
      <div class="f-row"><label>项目 / 当前阶段（自动带出）</label>
        <div class="f-readonly"><span id="dmAdvPrj">—</span><span style="color:#d9d9d9">|</span><span id="dmAdvStage">—</span></div>
      </div>
      <div class="f-row"><label>推进至</label>
        <div class="f-readonly" id="dmAdvNext">—</div>
      </div>
      <div class="f-hint" style="margin-top:2px;">确认后阶段徽章与状态同步更新（演示为页内联动，跨页数据不变）</div>
    </div>
    <div class="modal-footer">
      <button class="btn btn-default" onclick="dmCloseAdv()">取 消</button>
      <button class="btn btn-primary" onclick="dmConfirmAdvance()">确认推进</button>
    </div>
  </div>
</div>
"""

def f01():
    rel = '项目库/P3-R01-F01-项目列表.html'
    src = load(rel)
    # 推进确认弹窗：插在业务脚本前
    anchor = '<script>\n/* ===== 业务脚本：筛选折叠 ===== */'
    must(src, anchor, 1, 'F01.bizAnchor')
    src = src.replace(anchor, ADV_MODAL + '\n' + anchor, 1)
    # 放弃登记确认 → dmConfirmAbandon（登记未投归档态＋入 abandons 单源）
    must(src, 'onclick="closeAbandon();alert(\'已登记并转入「未投归档」\')"', 1, 'F01.abandonBtn')
    src = src.replace('onclick="closeAbandon();alert(\'已登记并转入「未投归档」\')"', 'onclick="dmConfirmAbandon()"', 1)
    # Esc 关闭推进弹窗
    must(src, 'if (e.key === \'Escape\') { closeAbandon(); closeNewModal(); }', 1, 'F01.esc')
    src = src.replace("if (e.key === 'Escape') { closeAbandon(); closeNewModal(); }",
                      "if (e.key === 'Escape') { closeAbandon(); closeNewModal(); dmCloseAdv(); }", 1)
    # G03 接入块追加 T2 函数
    tail = "  ['F01.list', 'F01.kb'].forEach(DM.renderList);\n})();"
    must(src, tail, 1, 'F01.config')
    fn = """  ['F01.list', 'F01.kb'].forEach(DM.renderList);

  /* ===== T2 页内真联动：推进 / 放弃归档（字段驱动重建行，单源同步） ===== */
  var DM_NEXT = {
    1: ['② 线上路演', 2, '路演排期中'], 2: ['③ 保密协议签署', 3, 'NDA 准备中'],
    3: ['④ 尽调/访谈', 4, '尽调准备中'], 4: ['⑤ 立项', 5, '立项准备中'],
    5: ['⑥ 投资人路演', 6, '路演安排中'], 6: ['⑦ 投决', 7, '待上会'],
    7: ['⑧ 基金设立', 8, '基金设立中'], 8: ['⑨ 出资', 9, '出资流程中'],
    9: ['⑩ 投后管理', 10, '投后管理中'], 10: ['⑪ 项目退出', 11, '退出流程中']
  };
  var DM_F19_NODE = { 1: '① 看 BP 后不看', 2: '② 线上路演后', 3: '③ 保密协议签署', 4: '④ 访谈/尽调后', 5: '⑤ 立项时', 6: '⑥ 投资人路演后' };
  window.dmCurPrj = null;
  /* 行重建器：按 projects 字段生成与原行同构的 tr */
  window.dmPrjRow = function (p) {
    var ops = ['<a onclick="go(\\'P3-R01-F02-项目详情-项目概况.html\\')">详情</a>'];
    if (p.ops.indexOf('adv') > -1) { ops.push('<a onclick="dmAdvance(\\'' + p.id + '\\')">推进</a>'); }
    if (p.ops.indexOf('stall') > -1) {
      ops.push(p.id === 'PRJ-2026-0002'
        ? '<a onclick="dmStallNote(\\'' + p.id + '\\')">停滞处置</a>'
        : '<a onclick="alert(\\'已推送停滞提醒给负责人\\')">停滞处置</a>');
    }
    if (p.ops.indexOf('abandon') > -1) { ops.push('<a class="danger-op" onclick="openAbandon(\\'' + p.id + '\\',\\'' + p.stage + '\\')">放弃</a>'); }
    if (p.ops.indexOf('post') > -1) { ops.push('<a>转入投后</a>'); }
    if (p.ops === 'arch' || p.stage === '未投归档') { ops = ['<a>归档详情</a>']; }
    return '<tr>'
      + '<td><input type="checkbox" class="cb"></td>'
      + '<td><span class="lk">' + p.id + '</span></td>'
      + '<td><span class="lk">' + p.name + '</span></td>'
      + '<td>' + p.industry + '</td>'
      + '<td>' + p.round + '</td>'
      + '<td><span class="stage-cell">' + p.stage + '</span></td>'
      + '<td><span class="tag ' + p.stCls + '">' + p.status + '</span></td>'
      + '<td>' + p.days + '</td>'
      + '<td>' + p.owner + '</td>'
      + '<td>' + p.updated + '</td>'
      + '<td class="sticky-op ops">' + ops.join('') + '</td>'
      + '</tr>';
  };
  window.dmAdvance = function (id) {
    var p = DM.byId(DM.store.projects, id);
    if (!p) { return; }
    var nx = DM_NEXT[p.stageNo];
    if (!nx) { alert('当前阶段暂不支持继续推进'); return; }
    window.dmCurPrj = id;
    document.getElementById('dmAdvPrj').textContent = p.id;
    document.getElementById('dmAdvStage').textContent = p.stage;
    document.getElementById('dmAdvNext').textContent = nx[0] + ' · 状态将更新为「' + nx[2] + '」';
    document.getElementById('dmAdvModal').classList.add('show');
  };
  window.dmCloseAdv = function () { document.getElementById('dmAdvModal').classList.remove('show'); };
  document.getElementById('dmAdvModal').addEventListener('click', function (e) { if (e.target === this) dmCloseAdv(); });
  window.dmConfirmAdvance = function () {
    var p = DM.byId(DM.store.projects, window.dmCurPrj);
    if (!p) { dmCloseAdv(); return; }
    var nx = DM_NEXT[p.stageNo];
    p.stage = nx[0]; p.stageNo = nx[1]; p.status = nx[2]; p.stCls = 'tag-blue';
    p.days = '0 天'; p.updated = '2026-08-27';
    if (p.kb && p.kb.col === nx[1] - 1) { p.kb.col = nx[1]; p.kb.next = '待更新'; p.kb.warn = false; }
    p.tr = dmPrjRow(p);
    dmCloseAdv();
    DM.renderList('F01.list'); DM.renderList('F01.kb');
  };
  window.dmConfirmAbandon = function () {
    var p = DM.byId(DM.store.projects, document.getElementById('abPrj').textContent);
    var isGp = document.querySelector('input[name="subject"]:checked').dataset.kind === 'gp';
    var reason = document.getElementById('leafReason').value;
    var custom = document.getElementById('reasonCustom').value;
    if (p) {
      var short = p.name.replace(/（.*?）/, '');
      p.stage = '未投归档'; p.stageNo = 0;
      p.status = (isGp ? 'GP·' : 'LP·') + (reason || '放弃');
      p.stCls = isGp ? 'tag-gray' : 'tag-red';
      p.days = '—'; p.updated = '2026-08-27'; p.kb = null; p.ops = 'arch';
      p.tr = dmPrjRow(p);
      var nodeLabel = p.stageNo === 0 ? (isGp ? DM_F19_NODE[p.stageNo] : '⑦ 投决会否决') : '';
      var prevStage = DM_NEXT[p.stageNo]; /* 占位，实际节点按归档前阶段 */
      DM.store.abandons.push({
        name: short, subject: isGp ? 'gp' : 'lp', node: 7,
        nodeLabel: isGp ? '⑦ 投决前主动撤回' : '⑦ 投决会否决',
        reason: reason || '—', custom: custom || '—', date: '2026-08-27', prj: p.id,
        tr: '<tr data-subject="' + (isGp ? 'gp' : 'lp') + '" data-node="7">'
          + '<td><span class="tag ' + (isGp ? 'tag-blue">GP' : 'tag-red">LP') + '</span></td>'
          + '<td>' + (isGp ? '⑦ 投决前主动撤回' : '⑦ 投决会否决') + '</td>'
          + '<td>' + (reason || '—') + '</td>'
          + '<td class="dim">' + (custom || '—') + '</td>'
          + '<td>1</td>'
          + '<td><span class="lk">' + short + '</span></td>'
          + '<td>2026-08-27</td></tr>'
      });
      DM.renderList('F01.list'); DM.renderList('F01.kb');
    }
    closeAbandon();
    alert('已登记并转入「未投归档」');
  };
})();"""
    src = src.replace(tail, fn, 1)
    save(rel, src)
    print("OK F01")

# ================= F15 项目退出：登记批次 → 新增行入单源 =================
def f15():
    rel = '退出管理/P3-R01-F15-项目退出.html'
    src = load(rel)
    must(src, 'onclick="closeBatModal();alert(\'已登记退出批次\')"', 1, 'F15.btn')
    src = src.replace('onclick="closeBatModal();alert(\'已登记退出批次\')"', 'onclick="dmSubmitBatch()"', 1)
    tail = "  DM.renderList('F15.bat');\n})();"
    must(src, tail, 1, 'F15.config')
    fn = """  DM.renderList('F15.bat');

  /* ===== T2 登记退出批次：提交即新增一行（数据入 store.batches，行/页码联动） ===== */
  window.dmFmtNum = function (n) {
    var v = Math.round(n * 100) / 100;
    return v.toLocaleString('zh-CN', { maximumFractionDigits: 2 });
  };
  window.dmSubmitBatch = function () {
    var price = parseFloat(document.getElementById('exPrice').value) || 0;
    var qty = parseFloat(document.getElementById('exQty').value) || 0;
    if (!(price > 0 && qty > 0)) { alert('请填写退出价格与数量'); return; }
    var typeSel = document.getElementById('exType');
    var type = typeSel.options[typeSel.selectedIndex].text;
    var typeCls = type === 'IPO 减持' ? 'tag-orange' : 'tag-blue';
    var amount = price * qty, principal = qty * 2, gain = amount - principal;
    var rate = principal > 0 ? (gain / principal * 100).toFixed(1) + '%' : '—';
    var date = document.getElementById('exDate').value || '2026-08-27';
    var seq = 0;
    DM.store.batches.forEach(function (b) {
      var m = b.id.match(/BAT-\\d{4}-(\\d+)/); if (m) { seq = Math.max(seq, +m[1]); }
    });
    var id = 'BAT-2026-' + ('00' + (seq + 1)).slice(-3);
    var b = { id: id, type: type, typeCls: typeCls, price: dmFmtNum(price), qty: dmFmtNum(qty),
      amount: dmFmtNum(amount), date: date, principal: dmFmtNum(principal), gain: dmFmtNum(gain),
      gainCls: gain < 0 ? 'num-neg' : 'num-pos', rate: rate, status: '待执行', stCls: 'tag-orange',
      detail: type + ' ' + dmFmtNum(qty) + ' 万份 × ' + dmFmtNum(price) + ' 元/份 = ' + dmFmtNum(amount) + ' 万元，' + date + ' 登记（待执行）' };
    b.tr = '<tr>'
      + '<td><span class="lk">' + b.id + '</span></td>'
      + '<td><span class="tag ' + b.typeCls + '">' + b.type + '</span></td>'
      + '<td>' + b.price + '</td>'
      + '<td>' + b.qty + '</td>'
      + '<td>' + b.amount + '</td>'
      + '<td>' + b.date + '</td>'
      + '<td>' + b.principal + '</td>'
      + '<td class="' + b.gainCls + '">' + b.gain + '</td>'
      + '<td>' + b.rate + '</td>'
      + '<td><span class="tag tag-orange">待执行</span></td>'
      + '<td class="sticky-op ops"><a>查看</a><a>编辑</a></td>'
      + '</tr>';
    DM.store.batches.push(b);
    DM.renderList('F15.bat');
    closeBatModal();
    alert('已登记退出批次');
  };
})();"""
    src = src.replace(tail, fn, 1)
    save(rel, src)
    print("OK F15")

# ================= F12 报告归档：上传 → 新增行＋消解对应待上传行 =================
def f12():
    rel = '投后管理/P3-R01-F12-报告归档.html'
    src = load(rel)
    must(src, 'onclick="closeUpload();alert(\'已归档\')"', 1, 'F12.btn')
    src = src.replace('onclick="closeUpload();alert(\'已归档\')"', 'onclick="dmSubmitReport()"', 1)
    for old, new in [
        ('全部<span class="cnt">5</span>', '全部<span class="cnt" id="dmCntAll">5</span>'),
        ('季报<span class="cnt">2</span>', '季报<span class="cnt" id="dmCntQ">2</span>'),
        ('年报<span class="cnt">1</span>', '年报<span class="cnt" id="dmCntY">1</span>'),
        ('专项报告<span class="cnt">2</span>', '专项报告<span class="cnt" id="dmCntS">2</span>'),
    ]:
        must(src, old, 1, 'F12.stab')
        src = src.replace(old, new, 1)
    old_cfg = """(function () {
  var S = DM.store;
  DM.pages['F12.list'] = { target: '#dmBody', rows: function () { return S.reports; }, rowHtml: function (r) { return r.tr; } };
  DM.renderList('F12.list');
})();"""
    must(src, old_cfg, 1, 'F12.config')
    new_cfg = """(function () {
  var S = DM.store;
  DM.pages['F12.list'] = { target: '#dmBody', rows: function () { return S.reports; }, rowHtml: function (r) { return r.tr; },
    after: function () {
      var q = 0, y = 0, s = 0;
      S.reports.forEach(function (r) {
        if (r.type === '季报') { q++; } else if (r.type === '年报') { y++; } else { s++; }
      });
      document.getElementById('dmCntAll').textContent = S.reports.length;
      document.getElementById('dmCntQ').textContent = q;
      document.getElementById('dmCntY').textContent = y;
      document.getElementById('dmCntS').textContent = s;
    } };
  DM.renderList('F12.list');

  /* ===== T2 上传报告：新增一行（已归档，按页面现有枚举）＋对应「待上传」行同步消解 ===== */
  window.dmSubmitReport = function () {
    var PRJ = { yunke: '云雀教育', panshi: '磐石精密制造' };
    var prj = PRJ[document.getElementById('upPrj').value] || '云雀教育';
    var t = document.getElementById('upType').value;
    var typeTag, period;
    if (t === 'q') {
      typeTag = '季报';
      period = document.getElementById('upQuarter').options[document.getElementById('upQuarter').selectedIndex].text;
    } else if (t === 'y') {
      typeTag = '年报';
      period = document.getElementById('upYear').options[document.getElementById('upYear').selectedIndex].text + '年度';
    } else {
      typeTag = '专项报告 · ' + document.getElementById('upSpecial').options[document.getElementById('upSpecial').selectedIndex].text;
      period = '—';
    }
    var seq = 0;
    S.reports.forEach(function (r) {
      var m = r.id.match(/RPT-\\d{4}-(\\d+)/); if (m) { seq = Math.max(seq, +m[1]); }
    });
    var id = 'RPT-2026-0' + ('0' + (seq + 1)).slice(-2);
    var nr = { id: id, prj: prj, type: typeTag, period: period, status: '已归档' };
    nr.tr = '<tr>'
      + '<td><span class="lk">' + id + '</span></td>'
      + '<td><span class="lk" onclick="go(\\'../项目库/P3-R01-F02-项目详情-项目概况.html\\')">' + prj + '</span></td>'
      + '<td><span class="tag tag-blue">' + typeTag + '</span></td>'
      + '<td>' + period + '</td>'
      + '<td>—</td><td>吕道远</td><td>2026-08-27</td>'
      + '<td><span class="tag tag-blue">已归档</span></td>'
      + '<td class="sticky-op ops"><a onclick="alert(\\'打开报告预览\\')">预览</a><a onclick="alert(\\'已开始下载\\')">下载</a></td>'
      + '</tr>';
    S.reports.unshift(nr);
    /* 同项目同类型同报告期的「待上传」行消解为已归档 */
    S.reports.forEach(function (r) {
      if (r !== nr && r.prj === prj && r.type === typeTag && r.period === period && r.status === '待上传') {
        r.status = '已归档';
        r.tr = r.tr
          .replace(/<span class="tag tag-orange">[^<]*<\\/span>/, '<span class="tag tag-blue">已归档</span>')
          .replace(/<a onclick="openUpload\\([^)]*\\)">上传<\\/a>/, '<a onclick="alert(\\'打开报告预览\\')">预览</a><a onclick="alert(\\'已开始下载\\')">下载</a>');
      }
    });
    DM.renderList('F12.list');
    closeUpload();
    alert('已归档');
  };
})();"""
    src = src.replace(old_cfg, new_cfg, 1)
    save(rel, src)
    print("OK F12")

f20(); f01(); f15(); f12()
print("T2 页内联动改造完成")
