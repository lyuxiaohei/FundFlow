# -*- coding: utf-8 -*-
"""侧栏拍平 v2（结构化）：LP 管理一级直达 F09（删箭头/子菜单；F09/F10 selected）；
审批中心直达 F20（F20 selected）。字符串索引定位＋逐处结构断言，无跨元素正则。"""
import os

ROOT = "/Users/bailey/Desktop/xiaohei-workplace/FundFlow/P3-R01-原型"
FILE = {
 'F00':'工作台/P3-R01-F00-工作台.html','F01':'项目库/P3-R01-F01-项目列表.html','F02':'项目库/P3-R01-F02-项目详情-项目概况.html',
 'F03':'项目库/P3-R01-F03-项目详情-材料库.html','F07':'基金管理/P3-R01-F07-基金列表.html','F08':'基金管理/P3-R01-F08-基金详情.html',
 'F09':'LP 管理/P3-R01-F09-LP台账.html','F10':'LP 管理/P3-R01-F10-LP出资.html','F11':'投后管理/P3-R01-F11-投后事项.html',
 'F12':'投后管理/P3-R01-F12-报告归档.html','F13':'投后管理/P3-R01-F13-风险预警.html','F14':'投后管理/P3-R01-F14-提醒中心.html',
 'F15':'退出管理/P3-R01-F15-项目退出.html','F16':'退出管理/P3-R01-F16-收益分配.html','F17':'退出管理/P3-R01-F17-清算注销.html',
 'F18':'统计报表/P3-R01-F18-阶段漏斗.html','F19':'统计报表/P3-R01-F19-放弃原因分布.html','F20':'审批中心/P3-R01-F20-审批中心.html',
 'F21':'系统管理/P3-R01-F21-系统管理.html','F22':'投后管理/P3-R01-F22-投后项目.html','F23':'退出管理/P3-R01-F23-退出项目.html',
}

def seg_ok(seg, name):
    """li 起点→菜单名 之间的结构必须恰为：li 标签 + 空白 + div 标签 + ico span"""
    assert seg.count('<li') == 1 and seg.count('<div') == 1, f"{name}: li/div 结构异常 {seg[:80]}"
    i_div = seg.index('<div')
    assert seg[:i_div].strip().startswith('<li class="sm-item'), f"{name}: li 前缀异常"
    assert seg[i_div:seg.index('>', i_div) + 1].count('>') == 1
    ico_s = seg.index('<span class="sm-ico">')
    ico_e = seg.index('</span>', ico_s)
    assert seg[ico_e:] == '</span>' and seg.count('<span class="sm-ico">') == 1, f"{name}: ico 结构异常"
    assert seg[seg.index('>') + 1:i_div].strip() == '' and seg[i_div:seg.index('>', i_div) + 1].endswith('>')
    between = seg[seg.index('>', i_div) + 1:ico_s]
    assert between.strip() == '', f"{name}: div 与 ico 间有内容"
    return seg[ico_s:ico_e + 6]

def patch(src, k):
    lp_same = "P3-R01-F09-LP台账.html" if "LP 管理/" in FILE[k] else "../LP 管理/P3-R01-F09-LP台账.html"
    ap_same = "P3-R01-F20-审批中心.html" if k == 'F20' else "../审批中心/P3-R01-F20-审批中心.html"

    # ---- LP 管理 li（含箭头＋子菜单） ----
    i_hdr = src.index('LP 管理<span class="sm-arrow">')
    li_s = src.rfind('<li class="sm-item', 0, i_hdr)
    ico_lp = seg_ok(src[li_s:i_hdr], k + '.LP')
    d_close = src.index('</div>', i_hdr)              # 组头 div 闭合（箭头 span 内无 div）
    ul_s = src.index('<ul class="sm-sub">', d_close)
    assert src[d_close + 6:ul_s].strip() == '', k + '.LP div与ul间有内容'
    ul_e = src.index('</ul>', ul_s) + 6
    li_e = src.index('</li>', ul_e) + 5
    assert src[ul_e:li_e].strip() == '</li>', k + '.LP ul与li闭合间有内容'
    if k in ('F09', 'F10'):
        head = f'<div class="sm-link selected">{ico_lp}LP 管理</div>'
    else:
        head = f'<div class="sm-link" onclick="go(\'{lp_same}\')">{ico_lp}LP 管理</div>'
    new_lp = f'<li class="sm-item">\n        {head}\n      </li>'
    src = src[:li_s] + new_lp + src[li_e:]

    # ---- 审批中心 li（has-sub 残留，无子菜单） ----
    hits = [o for o in (lambda s: [j for j in range(len(s)) if s.startswith('审批中心</div>', j)])(src)
            if _valid_ap(src, o)]
    assert len(hits) == 1, f"{k}: 审批中心头候选 {len(hits)}"
    i_hdr = hits[0]
    li_s = src.rfind('<li class="sm-item has-sub', 0, i_hdr)
    ico_ap = seg_ok(src[li_s:i_hdr], k + '.AP')
    li_e = src.index('</li>', i_hdr) + 5
    assert src[i_hdr + len('审批中心</div>'):li_e].strip() == '</li>', k + '.AP 闭合结构异常'
    if k == 'F20':
        head = f'<div class="sm-link selected">{ico_ap}审批中心</div>'
    else:
        head = f'<div class="sm-link" onclick="go(\'{ap_same}\')">{ico_ap}审批中心</div>'
    new_ap = f'<li class="sm-item">\n        {head}\n      </li>'
    src = src[:li_s] + new_ap + src[li_e:]
    return src

def _valid_ap(src, occ):
    li_s = src.rfind('<li class="sm-item has-sub', 0, occ)
    if li_s < 0:
        return False
    seg = src[li_s:occ]
    return seg.count('<li') == 1 and seg.count('<div') == 1 and seg.count('<span class="sm-ico">') == 1 \
        and seg.rstrip().endswith('</span>') and seg[seg.index('</span>'):] == '</span>'

for k in FILE:
    fp = os.path.join(ROOT, FILE[k])
    src = open(fp, encoding='utf-8').read()
    src2 = patch(src, k)
    assert 'LP 管理<span class="sm-arrow">' not in src2, k
    assert 'class="sm-link" class=' not in src2, k
    open(fp, 'w', encoding='utf-8').write(src2)
    print(f"OK {k}")

# ---- F09/F10 页签互达（纯串替换） ----
fp = os.path.join(ROOT, FILE['F09'])
src = open(fp, encoding='utf-8').read()
a1 = '<span class="tab active" data-note="1">LP 台账 <span class="close">×</span></span>'
assert src.count(a1) == 1
src = src.replace(a1, a1 + '\n      <span class="tab" onclick="go(\'P3-R01-F10-LP出资.html\')">LP 出资 <span class="close">×</span></span>', 1)
open(fp, 'w', encoding='utf-8').write(src)
print("OK F09 页签+LP 出资")

fp = os.path.join(ROOT, FILE['F10'])
src = open(fp, encoding='utf-8').read()
a2 = '<span class="tab active">LP 出资 <span class="close">×</span></span>'
assert src.count(a2) == 1
src = src.replace(a2, '<span class="tab" onclick="go(\'P3-R01-F09-LP台账.html\')">LP 台账 <span class="close">×</span></span>\n      ' + a2, 1)
open(fp, 'w', encoding='utf-8').write(src)
print("OK F10 页签+LP 台账")
