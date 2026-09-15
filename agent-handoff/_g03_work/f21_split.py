# -*- coding: utf-8 -*-
"""A19：F21 系统管理拆分为两页——F21-用户与角色（更名）＋F25-基础数据（新建）；
删页内 tab；侧栏子项各自直达各自高亮；D02 标注随迁。全部锚点替换＋逐处断言。"""
import os, subprocess

ROOT = "/Users/bailey/Desktop/xiaohei-workplace/FundFlow/P3-R01-原型"
F21_OLD = os.path.join(ROOT, "系统管理/P3-R01-F21-系统管理.html")
F21_NEW = os.path.join(ROOT, "系统管理/P3-R01-F21-用户与角色.html")
F25_NEW = os.path.join(ROOT, "系统管理/P3-R01-F25-基础数据.html")

orig = open(F21_OLD, encoding="utf-8").read()

# ---- 公共锚点 ----
A_TITLE = '<title>系统管理 - 投资项目管理</title>'
A_TAB = '<span class="tab active">系统管理 <span class="close">×</span></span>'
A_STABS = '''<div class="stabs">
          <span class="stab active" data-view="user" onclick="switchPanel('user')">用户与角色<span class="cnt">5</span></span>
          <span class="stab" data-view="dict" onclick="switchPanel('dict')">基础数据<span class="cnt">7</span></span>
        </div>

'''
A_USER_C = '        <!-- ===== 面板：用户与角色 ===== -->'
A_DICT_C = '        <!-- ===== 面板：基础数据（原字典管理） ===== -->'
A_CARD_TAIL = '      </div>\n    </div>\n  </div>\n</div>'
A_M1 = '<!-- ===== 弹窗1：新建 / 编辑用户 ===== -->'
A_M3 = '<!-- ===== 弹窗3：新增数据项 ===== -->'
A_S1 = '<script>\n/* ===== 业务脚本1：双页签切换 ===== */'
A_S2 = '/* ===== 业务脚本2：用户弹窗（新建 / 编辑） ===== */'
A_S4 = '/* ===== 业务脚本4：基础数据（左侧分类 ↔ 右侧标题/表格联动） ===== */'
A_ESC = "document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeUser(); closeGrant(); closeDictItem(); } });"
A_DM = '<script>\n/* ===== G03/T3 编辑数据项 → 复用新增数据项弹窗预填（dm- 前缀） ===== */'
A_MENU = '<script>\n/* ===== 菜单折叠 / 左下角系统切换（统一脚本） ===== */'
A_NOTES = '<style id="proto-notes-style">'
SEL_USER = '<li><div class="sm-link selected">用户与角色</div></li>'
DICT_SW = '<li><div class="sm-link" onclick="switchPanel(\'dict\')">基础数据</div></li>'

def cut(src, a, b):
    i, j = src.index(a), src.index(b)
    assert i < j, f"锚点次序异常: {a[:30]} ≥ {b[:30]}"
    return src[:i] + src[j:]

def must1(src, sub):
    assert src.count(sub) == 1, f"锚点 {src.count(sub)} 处: {sub[:60]}"
    return src

# ================= F25 基础数据 =================
f25 = must1(orig, A_TITLE).replace(A_TITLE, '<title>基础数据 - 投资项目管理</title>', 1)
f25 = must1(f25, A_TAB).replace(A_TAB, '<span class="tab active">基础数据 <span class="close">×</span></span>', 1)
f25 = must1(f25, A_STABS).replace(A_STABS, '', 1)
f25 = cut(f25, A_USER_C, A_DICT_C)                      # 删用户面板
f25 = must1(f25, '<div id="panel-dict" style="display:none;">').replace('<div id="panel-dict" style="display:none;">', '<div id="panel-dict">', 1)
f25 = cut(f25, A_M1, A_M3)                              # 删用户/授权弹窗
f25 = cut(f25, A_S1[len('<script>\n'):], A_S4)          # 删脚本1-3（switchPanel/用户/授权）
f25 = must1(f25, A_ESC).replace(A_ESC, "document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeDictItem(); } });", 1)
f25 = must1(f25, SEL_USER).replace(SEL_USER, '<li><div class="sm-link" onclick="go(\'P3-R01-F21-用户与角色.html\')">用户与角色</div></li>', 1)
f25 = must1(f25, DICT_SW).replace(DICT_SW, '<li><div class="sm-link selected">基础数据</div></li>', 1)
# F25 校验
for gone in ['panel-user', 'userModal', 'grantModal', 'ROLE_PERMS', 'switchPanel', '业务脚本1', '业务脚本2', '业务脚本3']:
    assert gone not in f25, f"F25 残留 {gone}"
for keep in ['DICTS', 'dmEditDict', 'dictItemModal', 'proto-notes-style', 'panel-dict']:
    assert keep in f25, f"F25 缺失 {keep}"
open(F25_NEW, 'w', encoding='utf-8').write(f25)
print("OK F25-基础数据 新建")

# ================= F21 用户与角色 =================
f21 = must1(orig, A_TITLE).replace(A_TITLE, '<title>用户与角色 - 投资项目管理</title>', 1)
f21 = must1(f21, A_TAB).replace(A_TAB, '<span class="tab active">用户与角色 <span class="close">×</span></span>', 1)
f21 = must1(f21, A_STABS).replace(A_STABS, '', 1)
f21 = cut(f21, A_DICT_C, A_CARD_TAIL)                   # 删基础数据面板（至卡片闭合）
f21 = cut(f21, A_M3, A_S1)                              # 删新增数据项弹窗
f21 = cut(f21, A_S1[len('<script>\n'):], A_S2)          # 删脚本1（switchPanel）
f21 = cut(f21, A_S4, A_ESC)                             # 删脚本4（基础数据）
f21 = must1(f21, A_ESC if A_ESC in f21 else "document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeUser(); closeGrant(); } });")
# 上一行校验原 ESC 行已被脚本4区间连带删除则需恢复 ESC；脚本4区间止于 A_ESC 前，ESC 行仍在：
# （cut 到 A_ESC 起点，ESC 行本身保留）→ 改写其内容
esc_old = A_ESC
assert f21.count(esc_old) == 1, "F21 ESC 行异常"
f21 = f21.replace(esc_old, "document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeUser(); closeGrant(); } });", 1)
f21 = cut(f21, A_DM, A_MENU)                            # 删 dmEditDict 脚本块
f21 = cut(f21, A_NOTES, '</body>')                      # 删标注层注入块（随迁 F25）
f21 = must1(f21, DICT_SW).replace(DICT_SW, '<li><div class="sm-link" onclick="go(\'P3-R01-F25-基础数据.html\')">基础数据</div></li>', 1)
for gone in ['panel-dict', 'dictItemModal', 'DICTS', 'switchPanel', 'dmEditDict', '业务脚本1', '业务脚本4', 'proto-notes', '数据项名称']:
    assert gone not in f21, f"F21 残留 {gone}"
for keep in ['userModal', 'grantModal', 'ROLE_PERMS', 'permTree']:
    assert keep in f21, f"F21 缺失 {keep}"
assert SEL_USER in f21
open(F21_OLD, 'w', encoding='utf-8').write(f21)
r = subprocess.run(['git', '-C', os.path.dirname(ROOT), 'mv',
                    'P3-R01-原型/系统管理/P3-R01-F21-系统管理.html',
                    'P3-R01-原型/系统管理/P3-R01-F21-用户与角色.html'],
                   capture_output=True, text=True)
assert r.returncode == 0, r.stderr
assert os.path.exists(F21_NEW) and not os.path.exists(F21_OLD)
print("OK F21-用户与角色 更名＋瘦身")

# ================= 其余 20 页侧栏 =================
PAGES = ['工作台/P3-R01-F00-工作台.html','项目库/P3-R01-F01-项目列表.html','项目库/P3-R01-F02-项目详情-项目概况.html',
 '项目库/P3-R01-F03-项目详情-材料库.html','基金管理/P3-R01-F07-基金列表.html','基金管理/P3-R01-F08-基金详情.html',
 'LP 管理/P3-R01-F09-LP台账.html','LP 管理/P3-R01-F10-LP出资.html','投后管理/P3-R01-F11-投后事项.html',
 '投后管理/P3-R01-F12-报告归档.html','投后管理/P3-R01-F13-风险预警.html','投后管理/P3-R01-F14-提醒中心.html',
 '退出管理/P3-R01-F15-项目退出.html','退出管理/P3-R01-F16-收益分配.html','退出管理/P3-R01-F17-清算注销.html',
 '统计报表/P3-R01-F18-阶段漏斗.html','统计报表/P3-R01-F19-放弃原因分布.html','审批中心/P3-R01-F20-审批中心.html',
 '投后管理/P3-R01-F22-投后项目.html','退出管理/P3-R01-F23-退出项目.html']
U_OLD = "go('../系统管理/P3-R01-F21-系统管理.html')\">用户与角色"
U_NEW = "go('../系统管理/P3-R01-F21-用户与角色.html')\">用户与角色"
D_OLD = "go('../系统管理/P3-R01-F21-系统管理.html')\">基础数据"
D_NEW = "go('../系统管理/P3-R01-F25-基础数据.html')\">基础数据"
for rel in PAGES:
    fp = os.path.join(ROOT, rel)
    src = open(fp, encoding='utf-8').read()
    assert src.count(U_OLD) == 1 and src.count(D_OLD) == 1, rel
    src = src.replace(U_OLD, U_NEW, 1).replace(D_OLD, D_NEW, 1)
    open(fp, 'w', encoding='utf-8').write(src)
print("OK 20 页侧栏子项分流")

# ================= D04 导航图 =================
fp = os.path.join(ROOT, 'P3-R01-D04-业务流程导航图.html')
src = open(fp, encoding='utf-8').read()
old = 'href="系统管理/P3-R01-F21-系统管理.html"'
assert src.count(old) == 1
src = src.replace(old, 'href="系统管理/P3-R01-F21-用户与角色.html"', 1)
open(fp, 'w', encoding='utf-8').write(src)
print("OK D04 href 更新")

# ================= D02 标注 json 键随迁 =================
import json
J = os.path.join(ROOT, 'P3-R01-D02-原型标注数据.json')
data = json.load(open(J, encoding='utf-8'))
OLD_KEY, NEW_KEY = 'P3-R01-F21-系统管理.html', 'P3-R01-F25-基础数据.html'
assert OLD_KEY in data and NEW_KEY not in data
items = list(data.items())
data = { (NEW_KEY if k == OLD_KEY else k): v for k, v in items }
json.dump(data, open(J, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print("OK D02 标注键随迁 F25")
print("手术全部完成")
