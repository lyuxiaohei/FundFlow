# -*- coding: utf-8 -*-
"""G03/T1b：15 页接入 _data/demo-data.js（精确锚点替换＋逐处断言；失败页抛出由外层降级）"""
import os, re, sys, json

ROOT = "/Users/bailey/Desktop/xiaohei-workplace/FundFlow/P3-R01-原型"
P = lambda rel: os.path.join(ROOT, rel)
DM_TAG = '<script src="../_data/demo-data.js"></script>'
MENU_ANCHOR = '<script>\n/* ===== 菜单折叠 / 左下角系统切换（统一脚本） ===== */'
EDIT_LOG = []

def load(rel):
    return open(P(rel), encoding="utf-8").read()

def save(rel, src):
    open(P(rel), "w", encoding="utf-8").write(src)

def must(src, sub, n=1, what=""):
    c = src.count(sub)
    assert c == n, f"[{what}] 期望 {n} 处，实测 {c} 处：{sub[:70]}"
    return src

def add_head_dm(src, page):
    assert DM_TAG not in src, f"{page}: 已接入"
    m = re.search(r'<title>[^<]*</title>', src)
    assert m, f"{page}: 无 title"
    src = src[:m.end()] + '\n' + DM_TAG + src[m.end():]
    EDIT_LOG.append(f"{page}: head+dm")
    return src

def add_config(src, page, cfg):
    assert MENU_ANCHOR in src, f"{page}: 菜单脚本锚点缺失"
    src = src.replace(MENU_ANCHOR, '<script>\n/* ===== G03 单源数据层接入（_data/demo-data.js，A17） ===== */\n' + cfg + '\n</script>\n\n' + MENU_ANCHOR, 1)
    EDIT_LOG.append(f"{page}: config")
    return src

def empty_tbody(src, page, nth=0, new_tag='<tbody id="dmBody"></tbody>', span=None):
    """span: (start,end) 显式替换区（F16 嵌套表用）；否则按第 nth 个 tbody 非贪婪替换"""
    if span:
        s, e = span
        assert src[s:e].lstrip().startswith('<tbody'), f"{page}: span 起点非 tbody"
        return src[:s] + new_tag + src[e:]
    tbs = list(re.finditer(r'<tbody[^>]*>.*?</tbody>', src, re.S))
    assert nth < len(tbs), f"{page}: tbody {nth} 不存在（共 {len(tbs)}）"
    m = tbs[nth]
    return src[:m.start()] + new_tag + src[m.end():]

# ---- html.parser 子块提取（F13 卡片 / F14 到期流 / F00 卡片项） ----
from html.parser import HTMLParser
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
class ChildGrab(HTMLParser):
    def __init__(self, container_class):
        super().__init__(convert_charrefs=False)
        self.cc = container_class; self.in_cont = 0
        self.child_start = None; self.child_depth = 0
        self.kids = []; self.line_starts = [0]
    def feed_text(self, text):
        for i, ch in enumerate(text):
            if ch == '\n': self.line_starts.append(i + 1)
        self.feed(text); self.close(); return self.kids
    def pos(self):
        l, c = self.getpos(); return self.line_starts[l - 1] + c
    def handle_starttag(self, tag, attrs):
        cls = dict(attrs).get('class', '')
        if not self.in_cont:
            if self.cc in cls.split(): self.in_cont = 1
            return
        if tag in VOID: return
        if self.child_start is None:
            self.child_start = self.pos(); self.child_depth = 1
        else:
            self.child_depth += 1
    def handle_endtag(self, tag):
        if not self.in_cont or tag in VOID: return
        if self.child_depth == 1:
            self.kids.append((self.child_start, self.pos() + len('</' + tag + '>')))
            self.child_start = None; self.child_depth = 0
        elif self.child_depth > 1:
            self.child_depth -= 1
        else:
            self.in_cont = 0

def kids_ranges(src, container_class, marker, page, expect):
    p = ChildGrab(container_class)
    kids = [r for r in p.feed_text(src) if marker in src[r[0]:r[0] + 100]]
    assert len(kids) == expect, f"{page}: {container_class} 子块 {len(kids)}≠{expect}"
    return kids

def replace_kids_with(src, kids, container, page):
    s, e = kids[0][0], kids[-1][1]
    assert src[s:e].count(marker_guard := container.split('"')[1]) == 0
    return src[:s] + container + src[e:]

def replace_flat_items(src, cls, count, container, page):
    """无嵌套 div 的连续同类项（todo-item/stall-item）整体替换为容器"""
    starts = [m.start() for m in re.finditer(r'<div class="' + cls + r'"[^>]*>', src)]
    assert len(starts) >= count, f"{page}: {cls} 仅 {len(starts)} 处"
    # 取第一组连续 count 项
    block_start = starts[0]
    end = None
    for i in range(count):
        st = starts[i]
        cl = src.index('</div>', st) + len('</div>')
        end = cl
        if i + 1 < count:
            gap = src[end:starts[i + 1]]
            assert gap.strip() == '', f"{page}: {cls} 第 {i} 项与下一项之间存在非空白：{gap[:50]}"
    return src[:block_start] + container + src[end:]

# ================= F00 工作台 =================
def f00():
    page, rel = 'F00', '工作台/P3-R01-F00-工作台.html'
    src = load(rel)
    src = must(src, '<span class="tag tag-orange">3</span>', 1, page)
    src = src.replace('<span class="tag tag-orange">3</span>', '<span class="tag tag-orange" id="dmTodoCnt">3</span>', 1)
    src = must(src, '停滞提醒<span class="tag tag-orange">2</span>', 1, page)
    src = src.replace('停滞提醒<span class="tag tag-orange">2</span>', '停滞提醒<span class="tag tag-orange" id="dmStallCnt">2</span>', 1)
    src = must(src, '<span class="date">2026-09-03 · 星期四 · 今天有 3 件待审、2 条停滞提醒</span>', 1, page)
    src = src.replace('<span class="date">2026-09-03', '<span class="date" id="dmHelloDate">2026-09-03', 1)
    for old, new in [
        ('<div class="s-num">36</div>', '<div class="s-num" id="dmStatProjects">36</div>'),
        ('<div class="s-num">7<small>只</small></div>', '<div class="s-num" id="dmStatFunds">7<small>只</small></div>'),
        ('<div class="s-num">50<small>%</small></div>', '<div class="s-num" id="dmStatPaid">50<small>%</small></div>'),
        ('<div class="s-num">4<small>条</small></div>', '<div class="s-num" id="dmStatRules">4<small>条</small></div>'),
    ]:
        src = must(src, old, 1, page); src = src.replace(old, new, 1)
    # 三组卡片项 → 渲染容器（我的待办 3 项 / 我发起的 2 项 / 停滞提醒 2 项）
    i_todo = src.index('我的待办')
    i_stall = src.index('停滞提醒', i_todo)
    i_mine = src.index('我发起的', i_stall)
    blk_todo = replace_flat_items(src[i_todo:i_stall], 'todo-item', 3, '<div id="dmTodoList"></div>', page + '.待办')
    src = src[:i_todo] + blk_todo + src[i_stall:]
    i_stall = src.index('停滞提醒'); i_mine = src.index('我发起的', i_stall)
    blk_stall = replace_flat_items(src[i_stall:i_mine], 'stall-item', 2, '<div id="dmStallList"></div>', page + '.停滞')
    src = src[:i_stall] + blk_stall + src[i_mine:]
    i_mine = src.index('我发起的'); i_end = src.index('业务速览', i_mine)
    blk_mine = replace_flat_items(src[i_mine:i_end], 'todo-item', 2, '<div id="dmMineList"></div>', page + '.我发起')
    src = src[:i_mine] + blk_mine + src[i_end:]
    src = add_head_dm(src, page)
    cfg = """(function () {
  var S = DM.store;
  DM.pages['F00.todo'] = { target: '#dmTodoList', rows: function () { return S.todoView.todos; }, rowHtml: function (r) { return r.tr; },
    after: function () {
      var todos = S.todoView.todos.length, stalls = S.todoView.stalls.length;
      document.getElementById('dmTodoCnt').textContent = todos;
      document.getElementById('dmStallCnt').textContent = stalls;
      document.getElementById('dmHelloDate').textContent = '2026-09-03 · 星期四 · 今天有 ' + todos + ' 件待审、' + stalls + ' 条停滞提醒';
      document.getElementById('dmStatProjects').textContent = S.dmFunnel.total;
      document.getElementById('dmStatFunds').innerHTML = S.funds.length + '<small>只</small>';
      document.getElementById('dmStatPaid').innerHTML = S.capCalls.f002.pct + '<small>%</small>';
      document.getElementById('dmStatRules').innerHTML = S.reminders.rules.length + '<small>条</small>';
    } };
  DM.pages['F00.stall'] = { target: '#dmStallList', rows: function () { return S.todoView.stalls; }, rowHtml: function (r) { return r.tr; } };
  DM.pages['F00.mine'] = { target: '#dmMineList', rows: function () { return S.todoView.mines; }, rowHtml: function (r) { return r.tr; } };
  ['F00.todo', 'F00.stall', 'F00.mine'].forEach(DM.renderList);
})();"""
    src = add_config(src, page, cfg)
    save(rel, src)

# ================= F07 / F12 / F22 / F23（单 tbody blob） =================
def simple(rel, page, cfg_rows, extra=''):
    src = load(rel)
    src = empty_tbody(src, page, 0, '<tbody id="dmBody"></tbody>')
    src = add_head_dm(src, page)
    cfg = f"""(function () {{
  var S = DM.store;
  DM.pages['{page}.list'] = {{ target: '#dmBody', rows: function () {{ return {cfg_rows}; }}, rowHtml: function (r) {{ return r.tr; }}{extra} }};
  DM.renderList('{page}.list');
}})();"""
    src = add_config(src, page, cfg)
    save(rel, src)

def f07(): simple('基金管理/P3-R01-F07-基金列表.html', 'F07', 'S.funds')
def f12(): simple('投后管理/P3-R01-F12-报告归档.html', 'F12', 'S.reports')
def f22(): simple('投后管理/P3-R01-F22-投后项目.html', 'F22', 'S.postEvents.invested')
def f23(): simple('退出管理/P3-R01-F23-退出项目.html', 'F23', 'S.postEvents.exiting')

# ================= F13 风险预警 =================
def f13():
    page, rel = 'F13', '投后管理/P3-R01-F13-风险预警.html'
    src = load(rel)
    kids = kids_ranges(src, 'alerts', '<div class="alert-card', page, 5)
    src = replace_kids_with(src, kids, '<div id="dmWarnList"></div>', page)
    for old, new in [
        ('全部<span class="cnt">5</span>', '全部<span class="cnt" id="dmCntAll">5</span>'),
        ('未读<span class="cnt" id="cntUnread">3</span>', '未读<span class="cnt" id="cntUnread">3</span>'),
        ('已读未处理<span class="cnt" id="cntReadUntreated">1</span>', '已读未处理<span class="cnt" id="cntReadUntreated">1</span>'),
        ('已处理<span class="cnt">1</span>', '已处理<span class="cnt" id="dmCntDone">1</span>'),
    ]:
        src = must(src, old, 1, page)
        if 'id=' not in old:
            src = src.replace(old, new, 1)
    src = add_head_dm(src, page)
    cfg = """(function () {
  var S = DM.store;
  DM.pages['F13.cards'] = { target: '#dmWarnList', rows: function () { return S.warnings; }, rowHtml: function (r) { return r.tr; },
    after: function () {
      var un = 0, ru = 0, dn = 0;
      S.warnings.forEach(function (w) { if (w.state === 'unread') { un++; } else if (w.state === 'readUntreated') { ru++; } else { dn++; } });
      document.getElementById('dmCntAll').textContent = S.warnings.length;
      document.getElementById('cntUnread').textContent = un;
      document.getElementById('cntReadUntreated').textContent = ru;
      document.getElementById('dmCntDone').textContent = dn;
    } };
  DM.renderList('F13.cards');
})();"""
    src = add_config(src, page, cfg)
    save(rel, src)

# ================= F14 提醒中心 =================
def f14():
    page, rel = 'F14', '投后管理/P3-R01-F14-提醒中心.html'
    src = load(rel)
    src = must(src, '提醒规则<span class="cnt">4</span>', 1, page)
    src = src.replace('提醒规则<span class="cnt">4</span>', '提醒规则<span class="cnt" id="dmRuleCnt">4</span>', 1)
    src = must(src, '到期提醒<span class="cnt">4</span>', 1, page)
    src = src.replace('到期提醒<span class="cnt">4</span>', '到期提醒<span class="cnt" id="dmDueCnt">4</span>', 1)
    src = empty_tbody(src, page, 0, '<tbody id="dmBody"></tbody>')
    kids = kids_ranges(src, 'feed', '<div class="feed-item', page, 4)
    src = replace_kids_with(src, kids, '<div id="dmDueList"></div>', page)
    src = add_head_dm(src, page)
    cfg = """(function () {
  var S = DM.store;
  DM.pages['F14.rules'] = { target: '#dmBody', rows: function () { return S.reminders.rules; }, rowHtml: function (r) { return r.tr; },
    after: function () { document.getElementById('dmRuleCnt').textContent = S.reminders.rules.length; } };
  DM.pages['F14.due'] = { target: '#dmDueList', rows: function () { return S.reminders.due; }, rowHtml: function (r) { return r.tr; },
    after: function () { document.getElementById('dmDueCnt').textContent = S.reminders.due.length; } };
  ['F14.rules', 'F14.due'].forEach(DM.renderList);
})();"""
    src = add_config(src, page, cfg)
    save(rel, src)

# ================= F16 收益分配 =================
def f16():
    page, rel = 'F16', '退出管理/P3-R01-F16-收益分配.html'
    src = load(rel)
    s = src.index('<tbody>')
    c1 = src.index('</tbody>', s)
    c2 = src.index('</tbody>', c1 + len('</tbody>'))
    src = empty_tbody(src, page, 0, '<tbody id="dmBody"></tbody>', span=(s, c2 + len('</tbody>')))
    src = add_head_dm(src, page)
    cfg = """(function () {
  var S = DM.store;
  DM.pages['F16.dst'] = { target: '#dmBody', rows: function () { return S.distributions; }, rowHtml: function (r) { return r.tr; } };
  DM.renderList('F16.dst');
})();"""
    src = add_config(src, page, cfg)
    save(rel, src)

# ================= F10 / F17（FUNDS 指向单源） =================
def f10():
    page, rel = 'F10', 'LP 管理/P3-R01-F10-LP出资.html'
    src = load(rel)
    m = re.search(r'var FUNDS = \{.*?\n\};', src, re.S)
    assert m, page + ': FUNDS 未找到'
    src = src[:m.start()] + 'var FUNDS = DM.store.capCalls;' + src[m.end():]
    src = add_head_dm(src, page)
    save(rel, src)
    EDIT_LOG.append(f"{page}: FUNDS→DM.store.capCalls")

def f17():
    page, rel = 'F17', '退出管理/P3-R01-F17-清算注销.html'
    src = load(rel)
    m = re.search(r'var FUNDS = \{.*?\n\};', src, re.S)
    assert m, page + ': FUNDS 未找到'
    src = src[:m.start()] + 'var FUNDS = DM.store.postEvents.liquidationFunds;' + src[m.end():]
    src = add_head_dm(src, page)
    save(rel, src)
    EDIT_LOG.append(f"{page}: FUNDS→DM.store.postEvents.liquidationFunds")

# ================= F18 阶段漏斗 =================
def f18():
    page, rel = 'F18', '统计报表/P3-R01-F18-阶段漏斗.html'
    src = load(rel)
    src = empty_tbody(src, page, 0, '<tbody id="dmFunnelBody"></tbody>')
    src = must(src, '<tfoot>', 1, page)
    src = re.sub(r'<tfoot>.*?</tfoot>', '<tfoot id="dmFunnelFoot"></tfoot>', src, count=1, flags=re.S)
    src = add_head_dm(src, page)
    cfg = """(function () {
  var S = DM.store;
  DM.pages['F18.body'] = { target: '#dmFunnelBody', rows: function () { return S.dmFunnel.rows; }, rowHtml: function (r) { return r.tr; } };
  DM.pages['F18.foot'] = { target: '#dmFunnelFoot', rows: function () { return [1]; }, rowHtml: function () { return S.dmFunnel.foot; } };
  ['F18.body', 'F18.foot'].forEach(DM.renderList);
})();"""
    src = add_config(src, page, cfg)
    save(rel, src)

# ================= F19 放弃原因分布 =================
def f19():
    page, rel = 'F19', '统计报表/P3-R01-F19-放弃原因分布.html'
    src = load(rel)
    for old, new in [
        ('全部<span class="cnt">10</span>', '全部<span class="cnt" id="dmCntAll">10</span>'),
        ('GP 放弃<span class="cnt">8</span>', 'GP 放弃<span class="cnt" id="dmCntGp">8</span>'),
        ('LP 否决<span class="cnt">2</span>', 'LP 否决<span class="cnt" id="dmCntLp">2</span>'),
        ('<div class="lb">放弃总数</div>\n            <div class="num">10</div>', '<div class="lb">放弃总数</div>\n            <div class="num" id="dmNumTotal">10</div>'),
        ('<div class="lb">GP 放弃</div>\n            <div class="num blue">8</div>', '<div class="lb">GP 放弃</div>\n            <div class="num blue" id="dmNumGp">8</div>'),
        ('<div class="lb">LP 否决</div>\n            <div class="num red">2</div>', '<div class="lb">LP 否决</div>\n            <div class="num red" id="dmNumLp">2</div>'),
        ('<span>第 1-10 条/总共 10 条</span>', '<span id="dmPgInfo">第 1-10 条/总共 10 条</span>'),
    ]:
        src = must(src, old, 1, page)
        src = src.replace(old, new, 1)
    src = empty_tbody(src, page, 0, '<tbody id="dmBody"></tbody>')
    src = add_head_dm(src, page)
    cfg = """(function () {
  var S = DM.store;
  var G = S.__f19Groups;
  function cntOf(g) { return S.abandons.filter(function (a) { return a.subject === g.subject && a.node === g.node; }).length; }
  DM.pages['F19.detail'] = { target: '#dmBody',
    rows: function () {
      var out = [];
      G.forEach(function (g) {
        out.push({ group: g, n: cntOf(g) });
        S.abandons.forEach(function (a) { if (a.subject === g.subject && a.node === g.node) { out.push({ row: a }); } });
      });
      return out;
    },
    rowHtml: function (r) {
      if (r.group) {
        return '<tr class="group-row" data-subject="' + r.group.subject + '" data-node="' + r.group.node + '"><td colspan="7">' + r.group.label + '<span class="g-cnt">' + (r.group.subject === 'gp' ? 'GP' : 'LP') + ' · ' + r.n + ' 条</span></td></tr>';
      }
      return r.row.tr;
    },
    after: function () {
      var gp = S.abandons.filter(function (a) { return a.subject === 'gp'; }).length;
      var lp = S.abandons.length - gp;
      document.getElementById('dmCntAll').textContent = S.abandons.length;
      document.getElementById('dmCntGp').textContent = gp;
      document.getElementById('dmCntLp').textContent = lp;
      document.getElementById('dmNumTotal').textContent = S.abandons.length;
      document.getElementById('dmNumGp').textContent = gp;
      document.getElementById('dmNumLp').textContent = lp;
      document.getElementById('dmPgInfo').textContent = '第 1-' + S.abandons.length + ' 条/总共 ' + S.abandons.length + ' 条';
      if (window.dmRefreshHook) { window.dmRefreshHook(); }
    } };
  DM.renderList('F19.detail');
})();"""
    src = add_config(src, page, cfg)
    save(rel, src)

# ================= F20 审批中心 =================
def f20():
    page, rel = 'F20', '审批中心/P3-R01-F20-审批中心.html'
    src = load(rel)
    for old, new in [
        ('待我审批<span class="cnt">3</span>', '待我审批<span class="cnt" id="dmCntTodo">3</span>'),
        ('抄送我的<span class="cnt">2</span>', '抄送我的<span class="cnt" id="dmCntCc">2</span>'),
        ('我发起的<span class="cnt">3</span>', '我发起的<span class="cnt" id="dmCntMine">3</span>'),
        ('我已审批<span class="cnt">4</span>', '我已审批<span class="cnt" id="dmCntDone">4</span>'),
    ]:
        src = must(src, old, 1, page)
        src = src.replace(old, new, 1)
    tags = ['<tbody id="dmBodyTodo"></tbody>', '<tbody id="dmBodyCc"></tbody>',
            '<tbody id="dmBodyMine"></tbody>', '<tbody id="dmBodyDone"></tbody>']
    for i, tag in enumerate(tags):
        src = empty_tbody(src, page, i, tag)
    src = add_head_dm(src, page)
    cfg = """(function () {
  var S = DM.store;
  var VIEWS = [['todo', 'dmBodyTodo', 'dmCntTodo'], ['cc', 'dmBodyCc', 'dmCntCc'], ['mine', 'dmBodyMine', 'dmCntMine'], ['done', 'dmBodyDone', 'dmCntDone']];
  VIEWS.forEach(function (v) {
    DM.pages['F20.' + v[0]] = { target: '#' + v[1], rows: function () { return S.approvals[v[0]]; }, rowHtml: function (r) { return r.tr; },
      after: function () {
        var n = S.approvals[v[0]].length;
        document.getElementById(v[2]).textContent = n;
        var panel = document.getElementById('panel-' + v[0]);
        var pg = panel.querySelector('.pg-info');
        if (pg) { pg.textContent = '第 1-' + n + ' 条/总共 ' + n + ' 条'; }
      } };
    DM.renderList('F20.' + v[0]);
  });
})();"""
    src = add_config(src, page, cfg)
    save(rel, src)

# ================= F15 项目退出 =================
def f15():
    page, rel = 'F15', '退出管理/P3-R01-F15-项目退出.html'
    src = load(rel)
    m = re.search(r'<tbody id="rowsData">.*?</tbody>', src, re.S)
    assert m, page + ': rowsData 未找到'
    src = src[:m.start()] + '<tbody id="rowsData"></tbody>' + src[m.end():]
    src = add_head_dm(src, page)
    cfg = """(function () {
  var S = DM.store;
  DM.pages['F15.bat'] = { target: '#rowsData', rows: function () { return S.batches; }, rowHtml: function (r) { return r.tr; },
    after: function () {
      var n = S.batches.length;
      var pg = document.getElementById('pgInfo');
      if (pg) { pg.textContent = '第 1-' + n + ' 条/总共 ' + n + ' 条'; }
      var empty = document.getElementById('rowEmpty');
      if (empty) { empty.style.display = n ? 'none' : ''; }
      var rowsData = document.getElementById('rowsData');
      if (rowsData) { rowsData.style.display = n ? '' : 'none'; }
    } };
  DM.renderList('F15.bat');
})();"""
    src = add_config(src, page, cfg)
    save(rel, src)

# ================= F01 项目列表 =================
def f01():
    page, rel = 'F01', '项目库/P3-R01-F01-项目列表.html'
    src = load(rel)
    src = empty_tbody(src, page, 0, '<tbody id="dmBody"></tbody>')
    # 泳道 12 列 → 容器（.kb 内 12 个 kb-col 整体替换）
    kids = kids_ranges(src, 'kb', '<div class="kb-col', page, 12)
    src = replace_kids_with(src, kids, '<div id="dmKbCols"></div>', page)
    src = add_head_dm(src, page)
    cfg = """(function () {
  var S = DM.store;
  DM.pages['F01.list'] = { target: '#dmBody', rows: function () { return S.projects; }, rowHtml: function (r) { return r.tr; },
    after: function () {
      var n = S.projects.length;
      var pg = document.querySelector('#viewList .pg-info');
      if (pg) { pg.textContent = '第 1-' + n + ' 条/总共 ' + S.dmFunnel.total + ' 条'; }
    } };
  /* 泳道列定义（列名=原泳道列头，⑧⑨ 为里程碑列） */
  var KB_COLS = [
    { n: 1, label: '① 接触/收BP', mile: false }, { n: 2, label: '② 线上路演', mile: false },
    { n: 3, label: '③ 保密协议', mile: false }, { n: 4, label: '④ 尽调/访谈', mile: false },
    { n: 5, label: '⑤ 立项', mile: false }, { n: 6, label: '⑥ 投资人路演', mile: false },
    { n: 7, label: '⑦ 投决', mile: false }, { n: 8, label: '⑧ 基金设立', mile: true },
    { n: 9, label: '⑨ 出资', mile: true }, { n: 10, label: '⑩ 投后管理', mile: false },
    { n: 11, label: '⑪ 项目退出', mile: false }, { n: 12, label: '⑫ 清算注销', mile: false }
  ];
  window.dmKbCols = KB_COLS;
  function kbCard(p) {
    var k = p.kb;
    return '<div class="kb-card" onclick="go(\\'P3-R01-F02-项目详情-项目概况.html\\')">'
      + '<div class="nm">' + k.name + '</div>'
      + '<div class="st"><span>' + p.days + '</span>' + (k.warn ? '<span class="warn">⚠ 停滞</span>' : '') + '</div>'
      + '<div class="st"><span>下一步：' + k.next + '</span></div>'
      + '<div class="foot"><span class="ab" onclick="event.stopPropagation();openAbandon(\\'' + p.id + '\\',\\'' + (KB_COLS[k.col - 1] ? KB_COLS[k.col - 1].label : p.stage) + '\\')">放弃</span></div>'
      + '</div>';
  }
  window.dmKbCard = kbCard;
  DM.pages['F01.kb'] = { target: '#dmKbCols', rows: function () { return KB_COLS; },
    rowHtml: function (c) {
      var cards = S.projects.filter(function (p) { return p.kb && p.kb.col === c.n; });
      var inner = cards.length
        ? cards.map(kbCard).join('')
        : '<div class="kb-empty">暂无项目</div>';
      return '<div class="kb-col' + (c.mile ? ' mile' : '') + '"><div class="kb-head"><span class="n">' + c.label + '</span><span class="c">' + cards.length + '</span></div><div class="kb-body">' + inner + '</div></div>';
    } };
  ['F01.list', 'F01.kb'].forEach(DM.renderList);
})();"""
    src = add_config(src, page, cfg)
    save(rel, src)

# ================= 执行（页级事务：失败页抛出） =================
PAGES = [
 ('F00', f00), ('F07', f07), ('F12', f12), ('F22', f22), ('F23', f23),
 ('F13', f13), ('F14', f14), ('F16', f16), ('F10', f10), ('F17', f17),
 ('F18', f18), ('F19', f19), ('F20', f20), ('F15', f15), ('F01', f01),
]
failed = []
for name, fn in PAGES:
    try:
        fn()
        print(f"OK   {name}")
    except AssertionError as e:
        failed.append(name)
        print(f"FAIL {name}: {e}")
    except Exception as e:
        failed.append(name)
        print(f"ERR  {name}: {type(e).__name__} {e}")
print("\n编辑日志:", len(EDIT_LOG), "处")
print("失败页:", failed if failed else "无")
json.dump(failed, open('/Users/bailey/Desktop/xiaohei-workplace/FundFlow/agent-handoff/_g03_work/integ_failed.json', 'w'))
