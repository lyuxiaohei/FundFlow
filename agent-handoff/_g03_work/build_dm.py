# -*- coding: utf-8 -*-
"""G03/T1a：生成 P3-R01-原型/_data/demo-data.js（单源演示数据层）
数据提取纪律：全部来自现有页面静态 HTML 逐字提取（blob=整行/整卡 HTML），业务数据零发明。
结构化字段仅服务于 T2/T3/T4 的联动与推导（取值同样来自原页面可见数据）。"""
import os, re, json

ROOT = "/Users/bailey/Desktop/xiaohei-workplace/FundFlow/P3-R01-原型"
P = lambda rel: os.path.join(ROOT, rel)

import subprocess
GITSHOW = ['git', '-C', '/Users/bailey/Desktop/xiaohei-workplace/FundFlow', 'show', 'ff1a86d:P3-R01-原型/']

def read(rel):
    """自存档提交读取（接入后页面 tbody 已清空，原始行区唯一可信源=ff1a86d）"""
    r = subprocess.run(GITSHOW[:-1] + [GITSHOW[-1] + rel], capture_output=True, text=True)
    assert r.returncode == 0, 'git show 失败: ' + rel
    return r.stdout

def tbody_inner(src, nth=0):
    m = re.findall(r'(<tbody[^>]*>)(.*?)(</tbody>)', src, re.S)
    return m[nth][1] if nth < len(m) else ''

def trs(tb):
    return re.findall(r'<tr[ >].*?</tr>', tb, re.S)

def dedent(s):
    """去掉行首共同缩进，压缩行间空白为单个 \n（demo-data.js 内更紧凑）"""
    lines = [l.rstrip() for l in s.strip().splitlines()]
    return '\n'.join(l.strip() for l in lines if l.strip())

# ---------- html.parser：提取容器直接子块（用于嵌套 div 卡片流） ----------
from html.parser import HTMLParser
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
class ChildGrab(HTMLParser):
    def __init__(self, container_class):
        super().__init__(convert_charrefs=False)
        self.cc = container_class
        self.in_cont = 0          # 0=容器外；>0=容器内深度
        self.child_start = None   # 当前子块起点
        self.child_depth = 0      # 当前子块内未闭合标签数
        self.kids = []
        self.line_starts = [0]
    def feed_text(self, text):
        for i, ch in enumerate(text):
            if ch == '\n': self.line_starts.append(i + 1)
        self.feed(text)
        self.close()
        return self.kids
    def pos(self):
        l, c = self.getpos()
        return self.line_starts[l - 1] + c
    def handle_starttag(self, tag, attrs):
        cls = dict(attrs).get('class', '')
        if not self.in_cont:
            if self.cc in cls.split():
                self.in_cont = 1
            return
        if tag in VOID:
            return
        if self.child_start is None:
            self.child_start = self.pos()
            self.child_depth = 1
        else:
            self.child_depth += 1
    def handle_endtag(self, tag):
        if not self.in_cont:
            return
        if tag in VOID:
            return
        if self.child_depth == 1:
            self.kids.append((self.child_start, self.pos() + len('</' + tag + '>')))
            self.child_start = None
            self.child_depth = 0
        elif self.child_depth > 1:
            self.child_depth -= 1
        else:
            self.in_cont = 0  # 容器自身闭合

def grab_children(src, container_class, marker):
    """返回容器内以 marker（如 '<div class="todo-item"'）开头的直接子块原文列表"""
    p = ChildGrab(container_class)
    out = []
    for s, e in p.feed_text(src):
        block = src[s:e]
        if marker in block[:100]:
            out.append(dedent(block))
    return out

# ================= 数据提取 =================
# ---- F01 项目列表（10 行 blob + 结构化字段 + 泳道卡） ----
f01 = read('项目库/P3-R01-F01-项目列表.html')
f01_tb = tbody_inner(f01)
f01_trs = trs(f01_tb)
assert len(f01_trs) == 10, f"F01 行数 {len(f01_trs)}"

PROJECT_FIELDS = [
 # no, name, industry, round, stage, stageNo, status, stCls, days, owner, updated, ops
 ('PRJ-2026-0001','聚变能源科技（核聚变初创）','先进制造·新能源','A 轮','⑦ 投决',7,'待上会','tag-blue','6 天','吕道远','2026-08-27','adv_abandon'),
 ('PRJ-2026-0002','智驾千里（自动驾驶芯片）','人工智能','B 轮','③ 保密协议签署',3,'⚠ 停滞 47 天','tag-orange','47 天','吕道远','2026-08-26','stall'),
 ('PRJ-2026-0003','蓝鲸生物医药（创新药）','医疗健康','A 轮','⑧ 基金设立',8,'基金注册审批中','tag-blue','3 天','胡博','2026-08-27','adv'),
 ('PRJ-2026-0004','星河航天（商业卫星）','先进制造·航天','Pre-A','⑨ 出资',9,'付款审批中','tag-blue','1 天','胡博','2026-08-27','adv'),
 ('PRJ-2026-0005','云雀教育（职业教育平台）','教育','A 轮','⑩ 投后管理',10,'投后管理中','tag-blue','128 天','华悦','2026-08-20','post'),
 ('PRJ-2026-0006','远山新材料（碳纤维）','新材料','B 轮','① 接触/收BP',1,'接收 BP','tag-blue','2 天','吕道远','2026-08-26','adv_abandon'),
 ('PRJ-2026-0007','海豚半导体（车规 MCU）','半导体','定增','未投归档',0,'GP·明显超出投资范围','tag-gray','—','吕道远','2026-08-10','arch'),
 ('PRJ-2026-0008','风行低空（eVTOL 整机）','低空经济','A 轮','未投归档',0,'LP·投决会否决','tag-red','—','吕道远','2026-08-15','arch'),
 ('PRJ-2026-0009','青禾农业科技（智慧种植）','农业科技','天使轮','⑤ 立项',5,'⚠ 停滞 33 天','tag-orange','33 天','胡博','2026-08-25','stall_abandon'),
 ('PRJ-2026-0010','磐石量子（量子测量）','量子科技','Pre-A','④ 尽调/访谈',4,'路径B·访谈完成','tag-blue','9 天','吕道远','2026-08-24','adv_abandon'),
]
KB = {  # 泳道卡：列号、显示名、警示、下一步（取自原泳道卡可见文本）
 'PRJ-2026-0001': (7,'聚变能源科技（核聚变）',False,'投决上会'),
 'PRJ-2026-0002': (3,'智驾千里（自动驾驶芯片）',True,'跟进 NDA'),
 'PRJ-2026-0003': (8,'蓝鲸生物医药（创新药）',False,'基金注册审批'),
 'PRJ-2026-0004': (9,'星河航天（商业卫星）',False,'付款审批'),
 'PRJ-2026-0005': (10,'云雀教育（职业教育）',False,'季报归档'),
 'PRJ-2026-0006': (1,'远山新材料（碳纤维）',False,'BP 初筛'),
 'PRJ-2026-0009': (5,'青禾农业（智慧种植）',True,'立项会排期'),
 'PRJ-2026-0010': (4,'磐石量子（量子测量）',False,'路径B·资料包'),
}
projects = []
for tr, f in zip(f01_trs, PROJECT_FIELDS):
    no, name, ind, rnd, stage, stno, st, stc, days, owner, upd, ops = f
    kb = KB.get(no)
    if 'adv' in ops:
        assert tr.count('<a>推进</a>') == 1, no + ' 推进锚点异常'
        tr = tr.replace('<a>推进</a>', '<a onclick="dmAdvance(\'' + no + '\')">推进</a>', 1)
    if no == 'PRJ-2026-0002':
        # T3：处置标注（点名改造）→ 真弹窗
        assert tr.count("alert('处置标注：对方同时对接其他资金方，保持沟通中')") == 1, 'F01 处置标注锚点'
        tr = tr.replace("alert('处置标注：对方同时对接其他资金方，保持沟通中')", "dmStallNote('PRJ-2026-0002')", 1)
    projects.append({
        'id': no, 'no': no.split('-')[-1], 'name': name, 'industry': ind, 'round': rnd,
        'stage': stage, 'stageNo': stno, 'status': st, 'stCls': stc, 'days': days,
        'owner': owner, 'updated': upd, 'ops': ops,
        'kb': ({'col': kb[0], 'name': kb[1], 'warn': kb[2], 'next': kb[3]} if kb else None),
        'tr': dedent(tr),
    })

# ---- F19 放弃明细（10 条：字段 + blob；顺序=F19 明细顺序） ----
f19 = read('统计报表/P3-R01-F19-放弃原因分布.html')
f19_tb = tbody_inner(f19)
f19_rows = [t for t in trs(f19_tb) if 'group-row' not in t.split('>', 1)[0]]
assert len(f19_rows) == 10, f"F19 明细行 {len(f19_rows)}"
ABANDONS = [
 ('海豚半导体','gp',1,'① 看 BP 后不看','明显超出投资范围','主营业务与基金投资范围偏离较大','2026-08-10','PRJ-2026-0007'),
 ('晶彩光电','gp',1,'① 看 BP 后不看','明显超出投资范围','产能规模超出当前阶段偏好','2026-08-26',None),
 ('驭光微纳','gp',2,'② 线上路演后','专业问题答不出/逻辑薄弱','两轮问答后核心数字前后矛盾','2026-07-18',None),
 ('蓝湾储能','gp',4,'④ 访谈/尽调后','财务数据重大偏差','营收数据与纳税记录差异较大','2026-07-02',None),
 ('恒宇装备','gp',4,'④ 访谈/尽调后','工厂萧条、订单匮乏','实地走访产能利用率低，在手订单不足','2026-06-21',None),
 ('青云网络','gp',5,'⑤ 立项时','创始人信用风险/人品问题','历史涉诉与对外担保未如实披露','2026-06-09',None),
 ('南汐生物','gp',6,'⑥ 投资人路演后','全体投资人明确不出资','路演后认购意向为零，无法成案','2026-07-25',None),
 ('千乘出行','gp',7,'⑦ 投决前主动撤回','估值未谈拢（打折未成）','两轮折价沟通未达成一致','2026-08-20',None),
 ('风行低空','lp',7,'⑦ 投决会否决','不看好行业','对低空经济商业化周期判断存在分歧','2026-08-15','PRJ-2026-0008'),
 ('蓝湾机器人','lp',7,'⑦ 投决会否决','项目风险异议','适航取证进度与交付节奏存在风险','2026-07-22',None),
]
# 分组行序（主体×节点）：与原 F19 分组行一致
F19_GROUPS = [('gp',1,'① 看 BP 后不看'),('gp',2,'② 线上路演后'),('gp',4,'④ 访谈/尽调后'),
              ('gp',5,'⑤ 立项时'),('gp',6,'⑥ 投资人路演后'),('gp',7,'⑦ 投决前主动撤回'),
              ('lp',7,'⑦ 投决会否决')]
abandons = []
AB_T3 = 0
for f, tr in zip(ABANDONS, f19_rows):
    name, sub, node, nlabel, reason, custom, date, prj = f
    # T3：未投归档详情 → 真弹窗
    tr, n = re.subn(r"alert\('" + re.escape(name) + r" · 未投归档详情（[^']*'\)",
                    "dmAbDetail('" + name + "')", tr)
    AB_T3 += n
    abandons.append({'name': name, 'subject': sub, 'node': node, 'nodeLabel': nlabel,
                     'reason': reason, 'custom': custom, 'date': date, 'prj': prj, 'tr': dedent(tr)})
assert AB_T3 == 10, f'F19 T3 计数异常: {AB_T3}'

# ---- F20 审批中心（四视图 blob + 结构化索引） ----
f20 = read('审批中心/P3-R01-F20-审批中心.html')
ap_views = {}
for i, v in enumerate(['todo','cc','mine','done']):
    tb = tbody_inner(f20, i)
    ap_views[v] = trs(tb)
assert [len(v) for v in ap_views.values()] == [3,2,3,4]
AP_META = {  # id: [type, biz, owner, time, node, desc(待审视图审批入参原文)]
 'APV-2026-0037': ['投决上会','聚变能源科技 PRJ-2026-0001','吕道远','2026-08-27','投决会','投决材料已齐备（BP / 尽调报告 / 估值建议），拟投 3,000 万元、投前估值 12 亿元，提请投决会审议。'],
 'APV-2026-0038': ['基金注册审批','蓝鲸生物医药 PRJ-2026-0003 / FUND-2026-001','胡博','2026-08-26','总经理审批','专项基金已完成合伙协议签署，拟注册资本与出资安排见附件，提请审批后办理工商注册。'],
 'APV-2026-0039': ['付款审批','星河航天 PRJ-2026-0004 / FUND-2026-002','胡博','2026-08-27','财务审批','首期出资 1,500 万元，投资协议与交割条件已满足，收款账户信息已补充完整，提请财务复核付款。'],
 'APV-2026-0028': ['基金注册审批','香港远航国际基金','嘉怡','2026-08-08','总经理审批',''],
 'APV-2026-0025': ['收益分配审批','磐石一期 DST-2026-001','胡博','2026-06-01','投委会',''],
 'APV-2026-0033': ['付款审批','星河航天（补充凭证） PRJ-2026-0004 / FUND-2026-002','吕道远','2026-08-24','财务审批','收款账户信息不全，请补充凭证后重新提交'],
 'APV-2026-0030': ['立项审批','磐石量子 PRJ-2026-0010','吕道远','2026-08-20','已完成','2026-08-21 通过，审批人 胡博'],
 'APV-2025-0102': ['注销审批','临港智造 FUND-2024-005','胡博','2025-05-28','已完成','发起 2025-05-28 · 处理 2025-05-30'],
}
approvals = {}
DM_T3_COUNT = {'ap': 0, 'attach': 0}
for v, lst in ap_views.items():
    rows = []
    for tr in lst:
        if v == 'mine' and ' 已撤回：' in tr:
            tr2, n = re.subn(r"alert\('(APV-\d{4}-\d+) 已撤回：[^']*'\)", r"dmWithdraw('\1')", tr)
            assert n == 1, 'F20 撤回锚点异常'
            tr = tr2
        # T3：审批单详情 → 真弹窗（附件预览 alert 位于 apModal 页面骨架，归页面编辑处理）
        tr, n = re.subn(r"alert\('(APV-\d{4}-\d+) 审批单详情[^']*'\)", r"dmApDetail('\1')", tr)
        DM_T3_COUNT['ap'] += n
        ids = re.findall(r'APV-[0-9]{4}-[0-9]{4}', tr)
        aid = ids[0] if ids else None
        meta = AP_META.get(aid, ['', '', '', '', '', ''])
        bm = re.search(r'<td class="biz-cell">(.*?)</td>', tr, re.S)
        rows.append({'id': aid, 'type': meta[0], 'biz': meta[1], 'owner': meta[2],
                     'time': meta[3], 'node': meta[4], 'desc': meta[5],
                     'bizHtml': dedent(bm.group(1)) if bm else '', 'tr': dedent(tr)})
    approvals[v] = rows
assert DM_T3_COUNT['ap'] == 14, f'F20 T3 计数异常: {DM_T3_COUNT}'

# ---- F15 退出批次（3 行 blob + 字段） ----
f15 = read('退出管理/P3-R01-F15-项目退出.html')
f15_tb = tbody_inner(f15)
f15_trs = trs(f15_tb)
assert len(f15_trs) == 3
BATCHES = [
 ('BAT-2025-001','分红','tag-blue','0.10','2,000','200','2025-11-20','0','200','—','已完成','tag-blue','分红 0.10 元/份 × 2,000 万份 = 200 万元，2025-11-20 已完成'),
 ('BAT-2026-001','股权转让','tag-blue','2.80','1,000','2,800','2026-05-18','2,000','800','40%','已完成','tag-blue','股权转让 1,000 万份 × 2.80 元/份 = 2,800 万元，本金回收 2,000 万、批次收益 800 万'),
 ('BAT-2026-002','IPO 减持','tag-orange','预计 3.50','1,000','预计 3,500','预计 2026-09','预计 2,000','预计 1,500','预计 75%','待执行','tag-orange','IPO 减持 1,000 万份 × 预计 3.50 元/份 = 预计 3,500 万元，预计 2026-09 窗口执行'),
]
batches = []
BAT_T3 = {'detail': 0, 'edit': 0}
for f, tr in zip(BATCHES, f15_trs):
    bid, typ, typc, price, qty, amt, date, prin, gain, rate, st, stc, detail = f
    tr, n = re.subn(r"alert\('批次详情：" + re.escape(bid) + r" [^']*'\)", "dmBatDetail('" + bid + "')", tr)
    BAT_T3['detail'] += n
    tr, n = re.subn(r"alert\('编辑批次：" + re.escape(bid) + r"'\)", "dmEditBat('" + bid + "')", tr)
    BAT_T3['edit'] += n
    batches.append({'id': bid, 'type': typ, 'typeCls': typc, 'price': price, 'qty': qty,
                    'amount': amt, 'date': date, 'principal': prin, 'gain': gain, 'gainCls': 'num-pos',
                    'rate': rate, 'status': st, 'stCls': stc, 'detail': detail, 'tr': dedent(tr)})
assert BAT_T3 == {'detail': 6, 'edit': 3}, f'F15 T3 计数异常: {BAT_T3}'

# ---- F16 收益分配（单分配单：主行+子行整块 blob；外层 tbody 内嵌 LP 子表） ----
f16 = read('退出管理/P3-R01-F16-收益分配.html')
_s = f16.index('<tbody>')
_c1 = f16.index('</tbody>', _s)              # 内层 LP 表的闭合
_c2 = f16.index('</tbody>', _c1 + len('</tbody>'))  # 外层 tbody 的闭合
f16_tb = f16[_s + len('<tbody>'):_c2]
f16_blob = dedent(f16_tb)
assert f16_blob.count('<tr') == 5  # 主行1 + 子行1 + 嵌套表头1 + LP 表 2 行
# T3：分配单详情 ×2 → dmDstDetail；付款凭证 ×1（点名）→ dmVoucher；来源批次（无关键词，保留 alert）
f16_blob, n_dst = re.subn(r"alert\('分配单详情：DST-2026-001 [^']*'\)", 'dmDstDetail()', f16_blob)
f16_blob, n_vch = re.subn(r"alert\('付款凭证：付款凭证-宁波梅山远创-20260610\.pdf（已上传）'\)", 'dmVoucher()', f16_blob)
assert (n_dst, n_vch) == (2, 1), f'F16 T3 计数异常: {n_dst}/{n_vch}'
distributions = [{'id': 'DST-2026-001',
                  'biz': '磐石一期 DST-2026-001',
                  'detail': '基于批次 BAT-2026-001（股权转让 2,800 万元），按 LP 出资比例分配：宁波梅山远创 60% = 1,680 万元、悦达上海 40% = 1,120 万元',
                  'src': 'BAT-2026-001 股权转让 · 1,000 万份 × 2.80 元/份 = 2,800 万元 · 2026-05-18 完成',
                  'voucher': '付款凭证-宁波梅山远创-20260610.pdf（已上传）',
                  'tr': f16_blob}]

# ---- F07 基金列表（7 行 blob） ----
f07 = read('基金管理/P3-R01-F07-基金列表.html')
f07_trs = trs(tbody_inner(f07))
assert len(f07_trs) == 7
funds = []
for tr, fid, st in zip(f07_trs,
    ['FUND-2026-003','FUND-2026-002','FUND-2026-001','FUND-2025-011','FUND-2025-007','FUND-2024-005','FUND-2023-002'],
    ['存续中','存续中','设立中','清算中','存续中','已注销','存续中']):
    funds.append({'id': fid, 'status': st, 'tr': dedent(tr)})

# ---- F12 报告归档（5 行 blob + 字段） ----
f12 = read('投后管理/P3-R01-F12-报告归档.html')
f12_trs = trs(tbody_inner(f12))
assert len(f12_trs) == 5
REPORTS = [
 ('RPT-2026-021','云雀教育','季报','2026Q2','待上传'),
 ('RPT-2026-018','云雀教育','季报','2026Q1','已归档'),
 ('RPT-2026-009','云雀教育','年报','2025年度','已归档'),
 ('RPT-2026-015','磐石精密制造','专项报告 · 清算','—','已归档'),
 ('RPT-2026-012','磐石精密制造','专项报告 · 上市减持','—','待上传'),
]
reports = []
RPT_T3 = 0
for (rid, prj, typ, period, st), tr in zip(REPORTS, f12_trs):
    tr, n = re.subn(r"alert\('打开报告预览'\)", "dmViewReport('" + rid + "')", tr)
    RPT_T3 += n
    reports.append({'id': rid, 'prj': prj, 'type': typ, 'period': period, 'status': st, 'tr': dedent(tr)})
assert RPT_T3 == 3, f'F12 T3 计数异常: {RPT_T3}'

# ---- F13 风险预警（5 卡 blob + 状态） ----
f13 = read('投后管理/P3-R01-F13-风险预警.html')
cards = grab_children(f13, 'alerts', '<div class="alert-card')
assert len(cards) == 5, f"F13 卡片 {len(cards)}"
WARN_ST = ['unread','unread','unread','readUntreated','done']
warnings = [{'id': f'al{i+1}', 'state': s, 'tr': c} for i, (c, s) in enumerate(zip(cards, WARN_ST))]

# ---- F14 提醒中心（规则 4 行 blob + 到期 4 条 blob） ----
f14 = read('投后管理/P3-R01-F14-提醒中心.html')
f14_trs = trs(tbody_inner(f14))
assert len(f14_trs) == 4
due_items = grab_children(f14, 'feed', '<div class="feed-item')
assert len(due_items) == 4, f"F14 到期条 {len(due_items)}"
reminders = {'rules': [{'id': 'ALR-2026-011', 'tr': dedent(t)} for t in f14_trs],
             'due': [{'tr': d} for d in due_items]}

# ---- F00 工作台卡片（待办3/停滞2/我发起2 blob） ----
f00 = read('工作台/P3-R01-F00-工作台.html')
# 分别抓：我的待办卡（3）、停滞提醒卡（2）、我发起的卡（2）
def card_block(src, title):
    i = src.index('>' + title)
    j = src.index('<div class="card">', i)  # 下一张卡
    return src[i:j]
todo_card = card_block(f00, '我的待办')
stall_card = card_block(f00, '停滞提醒')
mine_card = card_block(f00, '我发起的')
grab = lambda blk, cls: [dedent(m) for m in re.findall(r'<div class="' + cls + r'"[^>]*>.*?</div>', blk, re.S)]
todos = grab(todo_card, 'todo-item')     # 单层 div，无嵌套
stalls = grab(stall_card, 'stall-item')
mines = grab(mine_card, 'todo-item')
assert len(todos) == 3 and len(stalls) == 2 and len(mines) == 2, (len(todos), len(stalls), len(mines))
todoView = {'todos': [{'tr': t} for t in todos], 'stalls': [{'tr': s} for s in stalls],
            'mines': [{'tr': m} for m in mines]}

# ---- F10 LP出资：FUNDS 对象原文提取 ----
f10 = read('LP 管理/P3-R01-F10-LP出资.html')
m = re.search(r'var FUNDS = (\{.*?\n\});', f10, re.S)
capCalls_raw = m.group(1)
# ---- F17 清算注销：FUNDS 对象原文提取 ----
f17 = read('退出管理/P3-R01-F17-清算注销.html')
m17 = re.search(r'var FUNDS = (\{.*?\n\});', f17, re.S)
liq_raw = m17.group(1)

# ---- F22/F23 段列表（各 3 行 blob） ----
f22 = read('投后管理/P3-R01-F22-投后项目.html')
f22_trs = trs(tbody_inner(f22)); assert len(f22_trs) == 3
f23 = read('退出管理/P3-R01-F23-退出项目.html')
f23_trs = trs(tbody_inner(f23)); assert len(f23_trs) == 3
postEvents = {'liquidationFunds': '__RAW_LIQ__',
              'invested': [{'tr': dedent(t)} for t in f22_trs],
              'exiting': [{'tr': dedent(t)} for t in f23_trs]}

# ---- F18 阶段漏斗（明细 12 行 blob + 汇总数字单源） ----
f18 = read('统计报表/P3-R01-F18-阶段漏斗.html')
f18_tb = tbody_inner(f18)
f18_trs = trs(f18_tb)
assert len(f18_trs) == 12
foot_m = re.search(r'<tfoot>(.*?)</tfoot>', f18, re.S)
dmFunnel = {'total': 36, 'converting': 20, 'invested': 6, 'quit': 10, 'gp': 8, 'lp': 2,
            'rows': [{'tr': dedent(t)} for t in f18_trs], 'foot': dedent(foot_m.group(1))}

# ---- T4：F01 补 8 个未投归档项目行（对齐 F19 明细；单号按 PRJ-2025-00xx 顺延，自已知最高 0016 之后起） ----
T4_NEW = [  # (name, subject, tag文本, F19 日期)——行业/轮次无任何既有数据源，按归档旧档填「—」（A17 默认决策注记）
 ('晶彩光电', 'gp', 'GP·明显超出投资范围', '2026-08-26'),
 ('驭光微纳', 'gp', 'GP·专业问题答不出/逻辑薄弱', '2026-07-18'),
 ('蓝湾储能', 'gp', 'GP·财务数据重大偏差', '2026-07-02'),
 ('恒宇装备', 'gp', 'GP·工厂萧条、订单匮乏', '2026-06-21'),
 ('青云网络', 'gp', 'GP·创始人信用风险/人品问题', '2026-06-09'),
 ('南汐生物', 'gp', 'GP·全体投资人明确不出资', '2026-07-25'),
 ('千乘出行', 'gp', 'GP·估值未谈拢（打折未成）', '2026-08-20'),
 ('蓝湾机器人', 'lp', 'LP·投决会否决', '2026-07-22'),
]
for k, (nm, sub, tag, dt) in enumerate(T4_NEW):
    no = 'PRJ-2025-%04d' % (17 + k)
    stc = 'tag-gray' if sub == 'gp' else 'tag-red'
    tr = ('<tr>\n'
          f'<td><input type="checkbox" class="cb"></td>\n'
          f'<td><span class="lk">{no}</span></td>\n'
          f'<td><span class="lk">{nm}</span></td>\n'
          f'<td>—</td>\n<td>—</td>\n'
          f'<td><span class="stage-cell">未投归档</span></td>\n'
          f'<td><span class="tag {stc}">{tag}</span></td>\n'
          f'<td>—</td>\n<td>吕道远</td>\n<td>{dt}</td>\n'
          f'<td class="sticky-op ops"><a>归档详情</a></td>\n'
          '</tr>')
    projects.append({'id': no, 'no': no.split('-')[-1], 'name': nm, 'industry': '—', 'round': '—',
                     'stage': '未投归档', 'stageNo': 0, 'status': tag, 'stCls': stc, 'days': '—',
                     'owner': '吕道远', 'updated': dt, 'ops': 'arch', 'kb': None, 'tr': dedent(tr)})
    for a in abandons:
        if a['name'] == nm:
            a['prj'] = no

# ================= 组装 demo-data.js =================
payload = {
    'projects': projects, 'abandons': abandons, 'approvals': approvals,
    'funds': funds, 'batches': batches, 'distributions': distributions,
    'reports': reports, 'warnings': warnings, 'reminders': reminders,
    'postEvents': postEvents, 'todoView': todoView, 'dmFunnel': dmFunnel,
}
# F19 分组定义（渲染分组行用）
payload['__f19Groups'] = [{'subject': s, 'node': n, 'label': l} for s, n, l in F19_GROUPS]
payload_json = json.dumps(payload, ensure_ascii=False, indent=1)

# postEvents.liquidationFunds 以原文嵌入（含函数无关的纯对象字面量）
payload_json = payload_json.replace('"__RAW_LIQ__"', liq_raw)
# capCalls 单独以原文嵌入
js = """/* ============================================================
   P3-R01-原型/_data/demo-data.js —— 单源演示数据层（G03/A17，V1.10）
   ------------------------------------------------------------
   · 数据来源：全部自各页静态 HTML 逐字提取（tr 字段＝原始整行 HTML），
     业务数据零发明；新增行仅 T4 的 8 个未投归档项目。
   · 接入方式：页内 <script src="../_data/demo-data.js"></script> 后，
     页内列配置 DM.pages[pageKey] = {target,rows,rowHtml,after}，
     再 DM.renderList(pageKey)。
   · 联动边界：仅页内内存态（同一浏览器会话）；不做跨页持久化，
     file:// 跨页会话不可靠，刷新/重启即还原初始演示数据。
   · 命名纪律：本文件新增 id/函数一律 dm- 前缀；不改各页既有
     id/class/JS 变量。
   ============================================================ */
window.DM = (function () {
  'use strict';
  var store = __PAYLOAD__;
  store.capCalls = __CAPCALLS__;

  var pages = {};

  function esc(s) {
    return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  /* 通用渲染器：按页内列配置渲染行区（tbody / 卡片容器均可） */
  function renderList(key) {
    var c = pages[key];
    if (!c) { return false; }
    var el = document.querySelector(c.target);
    if (!el) { return false; }
    var list = c.rows ? c.rows(store) : [];
    var html = '';
    for (var i = 0; i < list.length; i++) { html += c.rowHtml(list[i], i); }
    el.innerHTML = html;
    if (c.after) { c.after(el, list); }
    return true;
  }
  function renderAll() { Object.keys(pages).forEach(renderList); }
  /* 行实体定位（T2/T3 页内联动取值用） */
  function byId(arr, id) {
    for (var i = 0; i < arr.length; i++) { if (arr[i].id === id) { return arr[i]; } }
    return null;
  }

  return { store: store, pages: pages, renderList: renderList, renderAll: renderAll, esc: esc, byId: byId };
})();
"""
js = js.replace('__PAYLOAD__', payload_json).replace('__CAPCALLS__', capCalls_raw)

out = P('_data/demo-data.js')
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w', encoding='utf-8').write(js)
print("demo-data.js 已生成:", out, f"({len(js)//1024}KB)")
print("projects:", len(projects), "abandons:", len(abandons), "approvals:", {k: len(v) for k, v in approvals.items()})
print("funds:", len(funds), "batches:", len(batches), "reports:", len(reports), "warnings:", len(warnings))
print("reminders:", {k: len(v) for k, v in reminders.items()}, "todoView:", {k: len(v) for k, v in todoView.items()})
print("postEvents.invested:", len(postEvents['invested']), "exiting:", len(postEvents['exiting']))
print("dmFunnel rows:", len(dmFunnel['rows']))
