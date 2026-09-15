/* ============================================================
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
  var store = {
 "projects": [
  {
   "id": "PRJ-2026-0001",
   "no": "0001",
   "name": "聚变能源科技（核聚变初创）",
   "industry": "先进制造·新能源",
   "round": "A 轮",
   "stage": "⑦ 投决",
   "stageNo": 7,
   "status": "待上会",
   "stCls": "tag-blue",
   "days": "6 天",
   "owner": "吕道远",
   "updated": "2026-08-27",
   "ops": "adv_abandon",
   "kb": {
    "col": 7,
    "name": "聚变能源科技（核聚变）",
    "warn": false,
    "next": "投决上会"
   },
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2026-0001</span></td>\n<td><span class=\"lk\">聚变能源科技（核聚变初创）</span></td>\n<td>先进制造·新能源</td>\n<td>A 轮</td>\n<td><span class=\"stage-cell\">⑦ 投决</span></td>\n<td><span class=\"tag tag-blue\">待上会</span></td>\n<td>6 天</td>\n<td>吕道远</td>\n<td>2026-08-27</td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F02-项目详情-项目概况.html')\">详情</a><a onclick=\"dmAdvance('PRJ-2026-0001')\">推进</a><a class=\"danger-op\" onclick=\"openAbandon('PRJ-2026-0001','⑦ 投决')\">放弃</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2026-0002",
   "no": "0002",
   "name": "智驾千里（自动驾驶芯片）",
   "industry": "人工智能",
   "round": "B 轮",
   "stage": "③ 保密协议签署",
   "stageNo": 3,
   "status": "⚠ 停滞 47 天",
   "stCls": "tag-orange",
   "days": "47 天",
   "owner": "吕道远",
   "updated": "2026-08-26",
   "ops": "stall",
   "kb": {
    "col": 3,
    "name": "智驾千里（自动驾驶芯片）",
    "warn": true,
    "next": "跟进 NDA"
   },
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2026-0002</span></td>\n<td><span class=\"lk\">智驾千里（自动驾驶芯片）</span></td>\n<td>人工智能</td>\n<td>B 轮</td>\n<td><span class=\"stage-cell\">③ 保密协议签署</span></td>\n<td><span class=\"tag tag-orange\">⚠ 停滞 47 天</span></td>\n<td>47 天</td>\n<td>吕道远</td>\n<td>2026-08-26</td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F02-项目详情-项目概况.html')\">详情</a><a onclick=\"dmStallNote('PRJ-2026-0002')\">停滞处置</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2026-0003",
   "no": "0003",
   "name": "蓝鲸生物医药（创新药）",
   "industry": "医疗健康",
   "round": "A 轮",
   "stage": "⑧ 基金设立",
   "stageNo": 8,
   "status": "基金注册审批中",
   "stCls": "tag-blue",
   "days": "3 天",
   "owner": "胡博",
   "updated": "2026-08-27",
   "ops": "adv",
   "kb": {
    "col": 8,
    "name": "蓝鲸生物医药（创新药）",
    "warn": false,
    "next": "基金注册审批"
   },
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2026-0003</span></td>\n<td><span class=\"lk\">蓝鲸生物医药（创新药）</span></td>\n<td>医疗健康</td>\n<td>A 轮</td>\n<td><span class=\"stage-cell\">⑧ 基金设立</span></td>\n<td><span class=\"tag tag-blue\">基金注册审批中</span></td>\n<td>3 天</td>\n<td>胡博</td>\n<td>2026-08-27</td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F02-项目详情-项目概况.html')\">详情</a><a onclick=\"dmAdvance('PRJ-2026-0003')\">推进</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2026-0004",
   "no": "0004",
   "name": "星河航天（商业卫星）",
   "industry": "先进制造·航天",
   "round": "Pre-A",
   "stage": "⑨ 出资",
   "stageNo": 9,
   "status": "付款审批中",
   "stCls": "tag-blue",
   "days": "1 天",
   "owner": "胡博",
   "updated": "2026-08-27",
   "ops": "adv",
   "kb": {
    "col": 9,
    "name": "星河航天（商业卫星）",
    "warn": false,
    "next": "付款审批"
   },
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2026-0004</span></td>\n<td><span class=\"lk\">星河航天（商业卫星）</span></td>\n<td>先进制造·航天</td>\n<td>Pre-A</td>\n<td><span class=\"stage-cell\">⑨ 出资</span></td>\n<td><span class=\"tag tag-blue\">付款审批中</span></td>\n<td>1 天</td>\n<td>胡博</td>\n<td>2026-08-27</td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F02-项目详情-项目概况.html')\">详情</a><a onclick=\"dmAdvance('PRJ-2026-0004')\">推进</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2026-0005",
   "no": "0005",
   "name": "云雀教育（职业教育平台）",
   "industry": "教育",
   "round": "A 轮",
   "stage": "⑩ 投后管理",
   "stageNo": 10,
   "status": "投后管理中",
   "stCls": "tag-blue",
   "days": "128 天",
   "owner": "华悦",
   "updated": "2026-08-20",
   "ops": "post",
   "kb": {
    "col": 10,
    "name": "云雀教育（职业教育）",
    "warn": false,
    "next": "季报归档"
   },
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2026-0005</span></td>\n<td><span class=\"lk\">云雀教育（职业教育平台）</span></td>\n<td>教育</td>\n<td>A 轮</td>\n<td><span class=\"stage-cell\">⑩ 投后管理</span></td>\n<td><span class=\"tag tag-blue\">投后管理中</span></td>\n<td>128 天</td>\n<td>华悦</td>\n<td>2026-08-20</td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F02-项目详情-项目概况.html')\">详情</a><a>转入投后</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2026-0006",
   "no": "0006",
   "name": "远山新材料（碳纤维）",
   "industry": "新材料",
   "round": "B 轮",
   "stage": "① 接触/收BP",
   "stageNo": 1,
   "status": "接收 BP",
   "stCls": "tag-blue",
   "days": "2 天",
   "owner": "吕道远",
   "updated": "2026-08-26",
   "ops": "adv_abandon",
   "kb": {
    "col": 1,
    "name": "远山新材料（碳纤维）",
    "warn": false,
    "next": "BP 初筛"
   },
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2026-0006</span></td>\n<td><span class=\"lk\">远山新材料（碳纤维）</span></td>\n<td>新材料</td>\n<td>B 轮</td>\n<td><span class=\"stage-cell\">① 接触/收BP</span></td>\n<td><span class=\"tag tag-blue\">接收 BP</span></td>\n<td>2 天</td>\n<td>吕道远</td>\n<td>2026-08-26</td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F02-项目详情-项目概况.html')\">详情</a><a onclick=\"dmAdvance('PRJ-2026-0006')\">推进</a><a class=\"danger-op\" onclick=\"openAbandon('PRJ-2026-0006','① 接触/收BP')\">放弃</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2026-0007",
   "no": "0007",
   "name": "海豚半导体（车规 MCU）",
   "industry": "半导体",
   "round": "定增",
   "stage": "未投归档",
   "stageNo": 0,
   "status": "GP·明显超出投资范围",
   "stCls": "tag-gray",
   "days": "—",
   "owner": "吕道远",
   "updated": "2026-08-10",
   "ops": "arch",
   "kb": null,
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2026-0007</span></td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('海豚半导体')\">海豚半导体（车规 MCU）</span></td>\n<td>半导体</td>\n<td>定增</td>\n<td><span class=\"stage-cell\">未投归档</span></td>\n<td><span class=\"tag tag-gray\">GP·明显超出投资范围</span></td>\n<td>—</td>\n<td>吕道远</td>\n<td>2026-08-10</td>\n<td class=\"sticky-op ops\"><a onclick=\"dmAbDetail('海豚半导体')\">归档详情</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2026-0008",
   "no": "0008",
   "name": "风行低空（eVTOL 整机）",
   "industry": "低空经济",
   "round": "A 轮",
   "stage": "未投归档",
   "stageNo": 0,
   "status": "LP·投决会否决",
   "stCls": "tag-red",
   "days": "—",
   "owner": "吕道远",
   "updated": "2026-08-15",
   "ops": "arch",
   "kb": null,
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2026-0008</span></td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('风行低空')\">风行低空（eVTOL 整机）</span></td>\n<td>低空经济</td>\n<td>A 轮</td>\n<td><span class=\"stage-cell\">未投归档</span></td>\n<td><span class=\"tag tag-red\">LP·投决会否决</span></td>\n<td>—</td>\n<td>吕道远</td>\n<td>2026-08-15</td>\n<td class=\"sticky-op ops\"><a onclick=\"dmAbDetail('风行低空')\">归档详情</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2026-0009",
   "no": "0009",
   "name": "青禾农业科技（智慧种植）",
   "industry": "农业科技",
   "round": "天使轮",
   "stage": "⑤ 立项",
   "stageNo": 5,
   "status": "⚠ 停滞 33 天",
   "stCls": "tag-orange",
   "days": "33 天",
   "owner": "胡博",
   "updated": "2026-08-25",
   "ops": "stall_abandon",
   "kb": {
    "col": 5,
    "name": "青禾农业（智慧种植）",
    "warn": true,
    "next": "立项会排期"
   },
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2026-0009</span></td>\n<td><span class=\"lk\">青禾农业科技（智慧种植）</span></td>\n<td>农业科技</td>\n<td>天使轮</td>\n<td><span class=\"stage-cell\">⑤ 立项</span></td>\n<td><span class=\"tag tag-orange\">⚠ 停滞 33 天</span></td>\n<td>33 天</td>\n<td>胡博</td>\n<td>2026-08-25</td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F02-项目详情-项目概况.html')\">详情</a><a onclick=\"alert('已推送停滞提醒给负责人')\">停滞处置</a><a class=\"danger-op\" onclick=\"openAbandon('PRJ-2026-0009','⑤ 立项')\">放弃</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2026-0010",
   "no": "0010",
   "name": "磐石量子（量子测量）",
   "industry": "量子科技",
   "round": "Pre-A",
   "stage": "④ 尽调/访谈",
   "stageNo": 4,
   "status": "路径B·访谈完成",
   "stCls": "tag-blue",
   "days": "9 天",
   "owner": "吕道远",
   "updated": "2026-08-24",
   "ops": "adv_abandon",
   "kb": {
    "col": 4,
    "name": "磐石量子（量子测量）",
    "warn": false,
    "next": "路径B·资料包"
   },
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2026-0010</span></td>\n<td><span class=\"lk\">磐石量子（量子测量）</span></td>\n<td>量子科技</td>\n<td>Pre-A</td>\n<td><span class=\"stage-cell\">④ 尽调/访谈</span></td>\n<td><span class=\"tag tag-blue\">路径B·访谈完成</span></td>\n<td>9 天</td>\n<td>吕道远</td>\n<td>2026-08-24</td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F02-项目详情-项目概况.html')\">详情</a><a onclick=\"dmAdvance('PRJ-2026-0010')\">推进</a><a class=\"danger-op\" onclick=\"openAbandon('PRJ-2026-0010','④ 尽调/访谈')\">放弃</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2025-0017",
   "no": "0017",
   "name": "晶彩光电",
   "industry": "—",
   "round": "—",
   "stage": "未投归档",
   "stageNo": 0,
   "status": "GP·明显超出投资范围",
   "stCls": "tag-gray",
   "days": "—",
   "owner": "吕道远",
   "updated": "2026-08-26",
   "ops": "arch",
   "kb": null,
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2025-0017</span></td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('晶彩光电')\">晶彩光电</span></td>\n<td>—</td>\n<td>—</td>\n<td><span class=\"stage-cell\">未投归档</span></td>\n<td><span class=\"tag tag-gray\">GP·明显超出投资范围</span></td>\n<td>—</td>\n<td>吕道远</td>\n<td>2026-08-26</td>\n<td class=\"sticky-op ops\"><a onclick=\"dmAbDetail('晶彩光电')\">归档详情</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2025-0018",
   "no": "0018",
   "name": "驭光微纳",
   "industry": "—",
   "round": "—",
   "stage": "未投归档",
   "stageNo": 0,
   "status": "GP·专业问题答不出/逻辑薄弱",
   "stCls": "tag-gray",
   "days": "—",
   "owner": "吕道远",
   "updated": "2026-07-18",
   "ops": "arch",
   "kb": null,
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2025-0018</span></td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('驭光微纳')\">驭光微纳</span></td>\n<td>—</td>\n<td>—</td>\n<td><span class=\"stage-cell\">未投归档</span></td>\n<td><span class=\"tag tag-gray\">GP·专业问题答不出/逻辑薄弱</span></td>\n<td>—</td>\n<td>吕道远</td>\n<td>2026-07-18</td>\n<td class=\"sticky-op ops\"><a onclick=\"dmAbDetail('驭光微纳')\">归档详情</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2025-0019",
   "no": "0019",
   "name": "蓝湾储能",
   "industry": "—",
   "round": "—",
   "stage": "未投归档",
   "stageNo": 0,
   "status": "GP·财务数据重大偏差",
   "stCls": "tag-gray",
   "days": "—",
   "owner": "吕道远",
   "updated": "2026-07-02",
   "ops": "arch",
   "kb": null,
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2025-0019</span></td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('蓝湾储能')\">蓝湾储能</span></td>\n<td>—</td>\n<td>—</td>\n<td><span class=\"stage-cell\">未投归档</span></td>\n<td><span class=\"tag tag-gray\">GP·财务数据重大偏差</span></td>\n<td>—</td>\n<td>吕道远</td>\n<td>2026-07-02</td>\n<td class=\"sticky-op ops\"><a onclick=\"dmAbDetail('蓝湾储能')\">归档详情</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2025-0020",
   "no": "0020",
   "name": "恒宇装备",
   "industry": "—",
   "round": "—",
   "stage": "未投归档",
   "stageNo": 0,
   "status": "GP·工厂萧条、订单匮乏",
   "stCls": "tag-gray",
   "days": "—",
   "owner": "吕道远",
   "updated": "2026-06-21",
   "ops": "arch",
   "kb": null,
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2025-0020</span></td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('恒宇装备')\">恒宇装备</span></td>\n<td>—</td>\n<td>—</td>\n<td><span class=\"stage-cell\">未投归档</span></td>\n<td><span class=\"tag tag-gray\">GP·工厂萧条、订单匮乏</span></td>\n<td>—</td>\n<td>吕道远</td>\n<td>2026-06-21</td>\n<td class=\"sticky-op ops\"><a onclick=\"dmAbDetail('恒宇装备')\">归档详情</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2025-0021",
   "no": "0021",
   "name": "青云网络",
   "industry": "—",
   "round": "—",
   "stage": "未投归档",
   "stageNo": 0,
   "status": "GP·创始人信用风险/人品问题",
   "stCls": "tag-gray",
   "days": "—",
   "owner": "吕道远",
   "updated": "2026-06-09",
   "ops": "arch",
   "kb": null,
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2025-0021</span></td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('青云网络')\">青云网络</span></td>\n<td>—</td>\n<td>—</td>\n<td><span class=\"stage-cell\">未投归档</span></td>\n<td><span class=\"tag tag-gray\">GP·创始人信用风险/人品问题</span></td>\n<td>—</td>\n<td>吕道远</td>\n<td>2026-06-09</td>\n<td class=\"sticky-op ops\"><a onclick=\"dmAbDetail('青云网络')\">归档详情</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2025-0022",
   "no": "0022",
   "name": "南汐生物",
   "industry": "—",
   "round": "—",
   "stage": "未投归档",
   "stageNo": 0,
   "status": "GP·全体投资人明确不出资",
   "stCls": "tag-gray",
   "days": "—",
   "owner": "吕道远",
   "updated": "2026-07-25",
   "ops": "arch",
   "kb": null,
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2025-0022</span></td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('南汐生物')\">南汐生物</span></td>\n<td>—</td>\n<td>—</td>\n<td><span class=\"stage-cell\">未投归档</span></td>\n<td><span class=\"tag tag-gray\">GP·全体投资人明确不出资</span></td>\n<td>—</td>\n<td>吕道远</td>\n<td>2026-07-25</td>\n<td class=\"sticky-op ops\"><a onclick=\"dmAbDetail('南汐生物')\">归档详情</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2025-0023",
   "no": "0023",
   "name": "千乘出行",
   "industry": "—",
   "round": "—",
   "stage": "未投归档",
   "stageNo": 0,
   "status": "GP·估值未谈拢（打折未成）",
   "stCls": "tag-gray",
   "days": "—",
   "owner": "吕道远",
   "updated": "2026-08-20",
   "ops": "arch",
   "kb": null,
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2025-0023</span></td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('千乘出行')\">千乘出行</span></td>\n<td>—</td>\n<td>—</td>\n<td><span class=\"stage-cell\">未投归档</span></td>\n<td><span class=\"tag tag-gray\">GP·估值未谈拢（打折未成）</span></td>\n<td>—</td>\n<td>吕道远</td>\n<td>2026-08-20</td>\n<td class=\"sticky-op ops\"><a onclick=\"dmAbDetail('千乘出行')\">归档详情</a></td>\n</tr>"
  },
  {
   "id": "PRJ-2025-0024",
   "no": "0024",
   "name": "蓝湾机器人",
   "industry": "—",
   "round": "—",
   "stage": "未投归档",
   "stageNo": 0,
   "status": "LP·投决会否决",
   "stCls": "tag-red",
   "days": "—",
   "owner": "吕道远",
   "updated": "2026-07-22",
   "ops": "arch",
   "kb": null,
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\">PRJ-2025-0024</span></td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('蓝湾机器人')\">蓝湾机器人</span></td>\n<td>—</td>\n<td>—</td>\n<td><span class=\"stage-cell\">未投归档</span></td>\n<td><span class=\"tag tag-red\">LP·投决会否决</span></td>\n<td>—</td>\n<td>吕道远</td>\n<td>2026-07-22</td>\n<td class=\"sticky-op ops\"><a onclick=\"dmAbDetail('蓝湾机器人')\">归档详情</a></td>\n</tr>"
  }
 ],
 "abandons": [
  {
   "name": "海豚半导体",
   "subject": "gp",
   "node": 1,
   "nodeLabel": "① 看 BP 后不看",
   "reason": "明显超出投资范围",
   "custom": "主营业务与基金投资范围偏离较大",
   "date": "2026-08-10",
   "prj": "PRJ-2026-0007",
   "tr": "<tr data-subject=\"gp\" data-node=\"1\">\n<td><span class=\"tag tag-blue\">GP</span></td>\n<td>① 看 BP 后不看</td>\n<td>明显超出投资范围</td>\n<td class=\"dim\">主营业务与基金投资范围偏离较大</td>\n<td>1</td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('海豚半导体')\">海豚半导体</span></td>\n<td>2026-08-10</td>\n</tr>"
  },
  {
   "name": "晶彩光电",
   "subject": "gp",
   "node": 1,
   "nodeLabel": "① 看 BP 后不看",
   "reason": "明显超出投资范围",
   "custom": "产能规模超出当前阶段偏好",
   "date": "2026-08-26",
   "prj": "PRJ-2025-0017",
   "tr": "<tr data-subject=\"gp\" data-node=\"1\">\n<td><span class=\"tag tag-blue\">GP</span></td>\n<td>① 看 BP 后不看</td>\n<td>明显超出投资范围</td>\n<td class=\"dim\">产能规模超出当前阶段偏好</td>\n<td>1</td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('晶彩光电')\">晶彩光电</span></td>\n<td>2026-08-26</td>\n</tr>"
  },
  {
   "name": "驭光微纳",
   "subject": "gp",
   "node": 2,
   "nodeLabel": "② 线上路演后",
   "reason": "专业问题答不出/逻辑薄弱",
   "custom": "两轮问答后核心数字前后矛盾",
   "date": "2026-07-18",
   "prj": "PRJ-2025-0018",
   "tr": "<tr data-subject=\"gp\" data-node=\"2\">\n<td><span class=\"tag tag-blue\">GP</span></td>\n<td>② 线上路演后</td>\n<td>专业问题答不出/逻辑薄弱</td>\n<td class=\"dim\">两轮问答后核心数字前后矛盾</td>\n<td>1</td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('驭光微纳')\">驭光微纳</span></td>\n<td>2026-07-18</td>\n</tr>"
  },
  {
   "name": "蓝湾储能",
   "subject": "gp",
   "node": 4,
   "nodeLabel": "④ 访谈/尽调后",
   "reason": "财务数据重大偏差",
   "custom": "营收数据与纳税记录差异较大",
   "date": "2026-07-02",
   "prj": "PRJ-2025-0019",
   "tr": "<tr data-subject=\"gp\" data-node=\"4\">\n<td><span class=\"tag tag-blue\">GP</span></td>\n<td>④ 访谈/尽调后</td>\n<td>财务数据重大偏差</td>\n<td class=\"dim\">营收数据与纳税记录差异较大</td>\n<td>1</td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('蓝湾储能')\">蓝湾储能</span></td>\n<td>2026-07-02</td>\n</tr>"
  },
  {
   "name": "恒宇装备",
   "subject": "gp",
   "node": 4,
   "nodeLabel": "④ 访谈/尽调后",
   "reason": "工厂萧条、订单匮乏",
   "custom": "实地走访产能利用率低，在手订单不足",
   "date": "2026-06-21",
   "prj": "PRJ-2025-0020",
   "tr": "<tr data-subject=\"gp\" data-node=\"4\">\n<td><span class=\"tag tag-blue\">GP</span></td>\n<td>④ 访谈/尽调后</td>\n<td>工厂萧条、订单匮乏</td>\n<td class=\"dim\">实地走访产能利用率低，在手订单不足</td>\n<td>1</td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('恒宇装备')\">恒宇装备</span></td>\n<td>2026-06-21</td>\n</tr>"
  },
  {
   "name": "青云网络",
   "subject": "gp",
   "node": 5,
   "nodeLabel": "⑤ 立项时",
   "reason": "创始人信用风险/人品问题",
   "custom": "历史涉诉与对外担保未如实披露",
   "date": "2026-06-09",
   "prj": "PRJ-2025-0021",
   "tr": "<tr data-subject=\"gp\" data-node=\"5\">\n<td><span class=\"tag tag-blue\">GP</span></td>\n<td>⑤ 立项时</td>\n<td>创始人信用风险/人品问题</td>\n<td class=\"dim\">历史涉诉与对外担保未如实披露</td>\n<td>1</td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('青云网络')\">青云网络</span></td>\n<td>2026-06-09</td>\n</tr>"
  },
  {
   "name": "南汐生物",
   "subject": "gp",
   "node": 6,
   "nodeLabel": "⑥ 投资人路演后",
   "reason": "全体投资人明确不出资",
   "custom": "路演后认购意向为零，无法成案",
   "date": "2026-07-25",
   "prj": "PRJ-2025-0022",
   "tr": "<tr data-subject=\"gp\" data-node=\"6\">\n<td><span class=\"tag tag-blue\">GP</span></td>\n<td>⑥ 投资人路演后</td>\n<td>全体投资人明确不出资</td>\n<td class=\"dim\">路演后认购意向为零，无法成案</td>\n<td>1</td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('南汐生物')\">南汐生物</span></td>\n<td>2026-07-25</td>\n</tr>"
  },
  {
   "name": "千乘出行",
   "subject": "gp",
   "node": 7,
   "nodeLabel": "⑦ 投决前主动撤回",
   "reason": "估值未谈拢（打折未成）",
   "custom": "两轮折价沟通未达成一致",
   "date": "2026-08-20",
   "prj": "PRJ-2025-0023",
   "tr": "<tr data-subject=\"gp\" data-node=\"7\">\n<td><span class=\"tag tag-blue\">GP</span></td>\n<td>⑦ 投决前主动撤回</td>\n<td>估值未谈拢（打折未成）</td>\n<td class=\"dim\">两轮折价沟通未达成一致</td>\n<td>1</td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('千乘出行')\">千乘出行</span></td>\n<td>2026-08-20</td>\n</tr>"
  },
  {
   "name": "风行低空",
   "subject": "lp",
   "node": 7,
   "nodeLabel": "⑦ 投决会否决",
   "reason": "不看好行业",
   "custom": "对低空经济商业化周期判断存在分歧",
   "date": "2026-08-15",
   "prj": "PRJ-2026-0008",
   "tr": "<tr data-subject=\"lp\" data-node=\"7\">\n<td><span class=\"tag tag-red\">LP</span></td>\n<td>⑦ 投决会否决</td>\n<td>不看好行业</td>\n<td class=\"dim\">对低空经济商业化周期判断存在分歧</td>\n<td>1</td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('风行低空')\">风行低空</span></td>\n<td>2026-08-15</td>\n</tr>"
  },
  {
   "name": "蓝湾机器人",
   "subject": "lp",
   "node": 7,
   "nodeLabel": "⑦ 投决会否决",
   "reason": "项目风险异议",
   "custom": "适航取证进度与交付节奏存在风险",
   "date": "2026-07-22",
   "prj": "PRJ-2025-0024",
   "tr": "<tr data-subject=\"lp\" data-node=\"7\">\n<td><span class=\"tag tag-red\">LP</span></td>\n<td>⑦ 投决会否决</td>\n<td>项目风险异议</td>\n<td class=\"dim\">适航取证进度与交付节奏存在风险</td>\n<td>1</td>\n<td><span class=\"lk\" onclick=\"dmAbDetail('蓝湾机器人')\">蓝湾机器人</span></td>\n<td>2026-07-22</td>\n</tr>"
  }
 ],
 "approvals": {
  "todo": [
   {
    "id": "APV-2026-0037",
    "type": "投决上会",
    "biz": "聚变能源科技 PRJ-2026-0001",
    "owner": "吕道远",
    "time": "2026-08-27",
    "node": "投决会",
    "desc": "投决材料已齐备（BP / 尽调报告 / 估值建议），拟投 3,000 万元、投前估值 12 亿元，提请投决会审议。",
    "bizHtml": "<span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">聚变能源科技</span> <span class=\"dim\">PRJ-2026-0001</span>",
    "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmApDetail('APV-2026-0037')\">APV-2026-0037</span></td>\n<td><span class=\"tag tag-blue\">投决上会</span></td>\n<td class=\"biz-cell\"><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">聚变能源科技</span> <span class=\"dim\">PRJ-2026-0001</span></td>\n<td>吕道远</td>\n<td>2026-08-27</td>\n<td>投决会</td>\n<td><span class=\"tag tag-orange\">待审</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"openApproval('APV-2026-0037','投决上会','聚变能源科技 PRJ-2026-0001','吕道远','2026-08-27','投决会','投决材料已齐备（BP / 尽调报告 / 估值建议），拟投 3,000 万元、投前估值 12 亿元，提请投决会审议。')\">审批</a></td>\n</tr>"
   },
   {
    "id": "APV-2026-0038",
    "type": "基金注册审批",
    "biz": "蓝鲸生物医药 PRJ-2026-0003 / FUND-2026-001",
    "owner": "胡博",
    "time": "2026-08-26",
    "node": "总经理审批",
    "desc": "专项基金已完成合伙协议签署，拟注册资本与出资安排见附件，提请审批后办理工商注册。",
    "bizHtml": "<span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">蓝鲸生物医药</span> <span class=\"dim\">PRJ-2026-0003 / FUND-2026-001</span>",
    "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmApDetail('APV-2026-0038')\">APV-2026-0038</span></td>\n<td><span class=\"tag tag-blue\">基金注册审批</span></td>\n<td class=\"biz-cell\"><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">蓝鲸生物医药</span> <span class=\"dim\">PRJ-2026-0003 / FUND-2026-001</span></td>\n<td>胡博</td>\n<td>2026-08-26</td>\n<td>总经理审批</td>\n<td><span class=\"tag tag-orange\">待审</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"openApproval('APV-2026-0038','基金注册审批','蓝鲸生物医药 PRJ-2026-0003 / FUND-2026-001','胡博','2026-08-26','总经理审批','专项基金已完成合伙协议签署，拟注册资本与出资安排见附件，提请审批后办理工商注册。')\">审批</a></td>\n</tr>"
   },
   {
    "id": "APV-2026-0039",
    "type": "付款审批",
    "biz": "星河航天 PRJ-2026-0004 / FUND-2026-002",
    "owner": "胡博",
    "time": "2026-08-27",
    "node": "财务审批",
    "desc": "首期出资 1,500 万元，投资协议与交割条件已满足，收款账户信息已补充完整，提请财务复核付款。",
    "bizHtml": "<span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">星河航天</span> <span class=\"dim\">PRJ-2026-0004 / FUND-2026-002</span>",
    "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmApDetail('APV-2026-0039')\">APV-2026-0039</span></td>\n<td><span class=\"tag tag-blue\">付款审批</span></td>\n<td class=\"biz-cell\"><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">星河航天</span> <span class=\"dim\">PRJ-2026-0004 / FUND-2026-002</span></td>\n<td>胡博</td>\n<td>2026-08-27</td>\n<td>财务审批</td>\n<td><span class=\"tag tag-orange\">待审</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"openApproval('APV-2026-0039','付款审批','星河航天 PRJ-2026-0004 / FUND-2026-002','胡博','2026-08-27','财务审批','首期出资 1,500 万元，投资协议与交割条件已满足，收款账户信息已补充完整，提请财务复核付款。')\">审批</a></td>\n</tr>"
   },
   {
    "id": "APV-2026-0040",
    "type": "认定审批",
    "biz": "江苏悦达（合格投资者认定）",
    "owner": "吕道远",
    "time": "2026-08-28",
    "node": "总经理审批",
    "desc": "江苏悦达产业资本管理有限公司提交合格投资者认定：资质材料齐备，认定结论建议「通过」，提请总经理审批。",
    "bizHtml": "<span class=\"lk\" onclick=\"go('../LP 管理/P3-R01-F09-LP台账.html')\">江苏悦达</span> <span class=\"dim\">合格投资者认定</span>",
    "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmApDetail('APV-2026-0040')\">APV-2026-0040</span></td>\n<td><span class=\"tag tag-blue\">认定审批</span></td>\n<td class=\"biz-cell\"><span class=\"lk\" onclick=\"go('../LP 管理/P3-R01-F09-LP台账.html')\">江苏悦达</span> <span class=\"dim\">合格投资者认定</span></td>\n<td>吕道远</td>\n<td>2026-08-28</td>\n<td>总经理审批</td>\n<td><span class=\"tag tag-orange\">待审</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"openApproval('APV-2026-0040','认定审批','江苏悦达（合格投资者认定）','吕道远','2026-08-28','总经理审批','江苏悦达产业资本管理有限公司提交合格投资者认定：资质材料齐备，认定结论建议「通过」，提请总经理审批。')\">审批</a></td>\n</tr>"
   }
  ],
  "cc": [
   {
    "id": "APV-2026-0028",
    "type": "基金注册审批",
    "biz": "香港远航国际基金",
    "owner": "嘉怡",
    "time": "2026-08-08",
    "node": "总经理审批",
    "desc": "",
    "bizHtml": "香港远航国际基金",
    "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmApDetail('APV-2026-0028')\">APV-2026-0028</span></td>\n<td><span class=\"tag tag-blue\">基金注册审批</span></td>\n<td class=\"biz-cell\">香港远航国际基金</td>\n<td>嘉怡</td>\n<td>2026-08-08</td>\n<td>总经理审批</td>\n<td><span class=\"tag tag-blue\">已通过</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"dmApDetail('APV-2026-0028')\">详情</a></td>\n</tr>"
   },
   {
    "id": "APV-2026-0025",
    "type": "收益分配审批",
    "biz": "磐石一期 DST-2026-001",
    "owner": "胡博",
    "time": "2026-06-01",
    "node": "投委会",
    "desc": "",
    "bizHtml": "<span class=\"lk\" onclick=\"go('../退出管理/P3-R01-F16-收益分配.html')\">磐石一期</span> <span class=\"dim\">DST-2026-001</span>",
    "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmApDetail('APV-2026-0025')\">APV-2026-0025</span></td>\n<td><span class=\"tag tag-blue\">收益分配审批</span></td>\n<td class=\"biz-cell\"><span class=\"lk\" onclick=\"go('../退出管理/P3-R01-F16-收益分配.html')\">磐石一期</span> <span class=\"dim\">DST-2026-001</span></td>\n<td>胡博</td>\n<td>2026-06-01</td>\n<td>投委会</td>\n<td><span class=\"tag tag-blue\">已通过</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"dmApDetail('APV-2026-0025')\">详情</a></td>\n</tr>"
   }
  ],
  "mine": [
   {
    "id": "APV-2026-0037",
    "type": "投决上会",
    "biz": "聚变能源科技 PRJ-2026-0001",
    "owner": "吕道远",
    "time": "2026-08-27",
    "node": "投决会",
    "desc": "投决材料已齐备（BP / 尽调报告 / 估值建议），拟投 3,000 万元、投前估值 12 亿元，提请投决会审议。",
    "bizHtml": "<span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">聚变能源科技</span> <span class=\"dim\">PRJ-2026-0001</span>",
    "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmApDetail('APV-2026-0037')\">APV-2026-0037</span></td>\n<td><span class=\"tag tag-blue\">投决上会</span></td>\n<td class=\"biz-cell\"><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">聚变能源科技</span> <span class=\"dim\">PRJ-2026-0001</span></td>\n<td>吕道远</td>\n<td>2026-08-27</td>\n<td>投决会</td>\n<td><span class=\"tag tag-blue\">审批中</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"alert('APV-2026-0037：投决会待审，已发起 0 天')\">详情</a><a onclick=\"dmWithdraw('APV-2026-0037')\">撤回</a><a onclick=\"alert('已向当前审批人发送催办提醒')\">催办</a></td>\n</tr>"
   },
   {
    "id": "APV-2026-0033",
    "type": "付款审批",
    "biz": "星河航天（补充凭证） PRJ-2026-0004 / FUND-2026-002",
    "owner": "吕道远",
    "time": "2026-08-24",
    "node": "财务审批",
    "desc": "收款账户信息不全，请补充凭证后重新提交",
    "bizHtml": "<span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">星河航天（补充凭证）</span> <span class=\"dim\">PRJ-2026-0004 / FUND-2026-002</span>",
    "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmApDetail('APV-2026-0033')\">APV-2026-0033</span></td>\n<td><span class=\"tag tag-blue\">付款审批</span></td>\n<td class=\"biz-cell\"><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">星河航天（补充凭证）</span> <span class=\"dim\">PRJ-2026-0004 / FUND-2026-002</span></td>\n<td>吕道远</td>\n<td>2026-08-24</td>\n<td>财务审批</td>\n<td><span class=\"tag tag-orange\">已退回</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"alert('退回原因：收款账户信息不全；修改后重新提交，可直达当前审批节点（历史审批记录保留）')\">详情</a><a onclick=\"openNew()\">重新提交</a></td>\n</tr>"
   },
   {
    "id": "APV-2026-0030",
    "type": "立项审批",
    "biz": "磐石量子 PRJ-2026-0010",
    "owner": "吕道远",
    "time": "2026-08-20",
    "node": "已完成",
    "desc": "2026-08-21 通过，审批人 胡博",
    "bizHtml": "<span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">磐石量子</span> <span class=\"dim\">PRJ-2026-0010</span>",
    "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmApDetail('APV-2026-0030')\">APV-2026-0030</span></td>\n<td><span class=\"tag tag-blue\">立项审批</span></td>\n<td class=\"biz-cell\"><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">磐石量子</span> <span class=\"dim\">PRJ-2026-0010</span></td>\n<td>吕道远</td>\n<td>2026-08-20</td>\n<td>已完成</td>\n<td><span class=\"tag tag-blue\">已通过</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"alert('APV-2026-0030：2026-08-21 通过，审批人 胡博')\">详情</a></td>\n</tr>"
   }
  ],
  "done": [
   {
    "id": "APV-2026-0033",
    "type": "付款审批",
    "biz": "星河航天（补充凭证） PRJ-2026-0004 / FUND-2026-002",
    "owner": "吕道远",
    "time": "2026-08-24",
    "node": "财务审批",
    "desc": "收款账户信息不全，请补充凭证后重新提交",
    "bizHtml": "<span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">星河航天（补充凭证）</span> <span class=\"dim\">PRJ-2026-0004 / FUND-2026-002</span>",
    "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmApDetail('APV-2026-0033')\">APV-2026-0033</span></td>\n<td><span class=\"tag tag-blue\">付款审批</span></td>\n<td class=\"biz-cell\"><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">星河航天（补充凭证）</span> <span class=\"dim\">PRJ-2026-0004 / FUND-2026-002</span></td>\n<td>胡博</td>\n<td><span class=\"tag tag-orange\">退回</span></td>\n<td>2026-08-24</td>\n<td>收款账户信息不全，请补充凭证后重新提交</td>\n</tr>"
   },
   {
    "id": "APV-2026-0028",
    "type": "基金注册审批",
    "biz": "香港远航国际基金",
    "owner": "嘉怡",
    "time": "2026-08-08",
    "node": "总经理审批",
    "desc": "",
    "bizHtml": "香港远航国际基金",
    "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmApDetail('APV-2026-0028')\">APV-2026-0028</span></td>\n<td><span class=\"tag tag-blue\">基金注册审批</span></td>\n<td class=\"biz-cell\">香港远航国际基金</td>\n<td>嘉怡</td>\n<td><span class=\"tag tag-blue\">通过</span></td>\n<td>2026-08-12</td>\n<td>境外架构核对无误</td>\n</tr>"
   },
   {
    "id": "APV-2026-0025",
    "type": "收益分配审批",
    "biz": "磐石一期 DST-2026-001",
    "owner": "胡博",
    "time": "2026-06-01",
    "node": "投委会",
    "desc": "",
    "bizHtml": "<span class=\"lk\" onclick=\"go('../退出管理/P3-R01-F16-收益分配.html')\">磐石一期</span> <span class=\"dim\">DST-2026-001</span>",
    "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmApDetail('APV-2026-0025')\">APV-2026-0025</span></td>\n<td><span class=\"tag tag-blue\">收益分配审批</span></td>\n<td class=\"biz-cell\"><span class=\"lk\" onclick=\"go('../退出管理/P3-R01-F16-收益分配.html')\">磐石一期</span> <span class=\"dim\">DST-2026-001</span></td>\n<td>胡博</td>\n<td><span class=\"tag tag-blue\">通过</span></td>\n<td>2026-06-03</td>\n<td>分配方案与合伙协议一致，同意</td>\n</tr>"
   },
   {
    "id": "APV-2025-0102",
    "type": "注销审批",
    "biz": "临港智造 FUND-2024-005",
    "owner": "胡博",
    "time": "2025-05-28",
    "node": "已完成",
    "desc": "发起 2025-05-28 · 处理 2025-05-30",
    "bizHtml": "<span class=\"lk\" onclick=\"go('../退出管理/P3-R01-F17-清算注销.html')\">临港智造</span> <span class=\"dim\">FUND-2024-005</span>",
    "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmApDetail('APV-2025-0102')\">APV-2025-0102</span></td>\n<td><span class=\"tag tag-blue\">注销审批</span></td>\n<td class=\"biz-cell\"><span class=\"lk\" onclick=\"go('../退出管理/P3-R01-F17-清算注销.html')\">临港智造</span> <span class=\"dim\">FUND-2024-005</span></td>\n<td>胡博</td>\n<td><span class=\"tag tag-blue\">通过</span></td>\n<td>2025-05-30</td>\n<td>清算材料齐备，同意注销</td>\n</tr>"
   }
  ]
 },
 "funds": [
  {
   "id": "FUND-2026-003",
   "status": "存续中",
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\" onclick=\"go('P3-R01-F08-基金详情.html')\">FUND-2026-003</span></td>\n<td><span class=\"lk\" onclick=\"go('P3-R01-F08-基金详情.html')\">杭州云雀教育创业投资合伙企业（有限合伙）</span></td>\n<td>6,000 万</td>\n<td>2026-02-15</td>\n<td>境内 · 杭州</td>\n<td><span class=\"tag tag-blue\">存续中</span></td>\n<td><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">云雀教育</span><span class=\"muted\">PRJ-2026-0005</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F08-基金详情.html')\">详情</a><a>编辑</a></td>\n</tr>"
  },
  {
   "id": "FUND-2026-002",
   "status": "存续中",
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\" onclick=\"go('P3-R01-F08-基金详情.html')\">FUND-2026-002</span></td>\n<td><span class=\"lk\" onclick=\"go('P3-R01-F08-基金详情.html')\">苏州工业园区星河航天投资合伙企业（有限合伙）</span></td>\n<td>8,000 万</td>\n<td>2026-08-10</td>\n<td>境内 · 苏州工业园区</td>\n<td><span class=\"tag tag-blue\">存续中</span></td>\n<td><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">星河航天</span><span class=\"muted\">PRJ-2026-0004</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F08-基金详情.html')\">详情</a><a>编辑</a></td>\n</tr>"
  },
  {
   "id": "FUND-2026-001",
   "status": "设立中",
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\" onclick=\"go('P3-R01-F08-基金详情.html')\">FUND-2026-001</span></td>\n<td><span class=\"lk\" onclick=\"go('P3-R01-F08-基金详情.html')\">宁波梅山保税港区蓝鲸产业投资合伙企业（有限合伙）</span></td>\n<td>5,000 万</td>\n<td>—</td>\n<td>境内 · 宁波梅山</td>\n<td><span class=\"tag tag-orange\">设立中</span></td>\n<td><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">蓝鲸生物医药</span><span class=\"muted\">PRJ-2026-0003</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F08-基金详情.html')\">详情</a><a>编辑</a></td>\n</tr>"
  },
  {
   "id": "FUND-2025-011",
   "status": "清算中",
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\" onclick=\"go('P3-R01-F08-基金详情.html')\">FUND-2025-011</span></td>\n<td><span class=\"lk\" onclick=\"go('P3-R01-F08-基金详情.html')\">深圳磐石一期股权投资合伙企业（有限合伙）</span></td>\n<td>4,000 万</td>\n<td>2025-03-10</td>\n<td>境内 · 深圳</td>\n<td><span class=\"tag tag-orange\">清算中</span></td>\n<td><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">磐石精密制造</span><span class=\"muted\">PRJ-2025-0016</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F08-基金详情.html')\">详情</a><a onclick=\"go('../退出管理/P3-R01-F17-清算注销.html')\">清算进度</a><a>编辑</a></td>\n</tr>"
  },
  {
   "id": "FUND-2025-007",
   "status": "存续中",
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\" onclick=\"go('P3-R01-F08-基金详情.html')\">FUND-2025-007</span></td>\n<td><span class=\"lk\" onclick=\"go('P3-R01-F08-基金详情.html')\">香港远航国际投资有限公司</span></td>\n<td>6,500 万 (USD)</td>\n<td>2025-05-16</td>\n<td>境外 · 香港</td>\n<td><span class=\"tag tag-blue\">存续中</span></td>\n<td><span style=\"color:var(--text-3);\">—</span> <span class=\"tag tag-blue tag-sm\">可关联</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F08-基金详情.html')\">详情</a><a>编辑</a></td>\n</tr>"
  },
  {
   "id": "FUND-2024-005",
   "status": "已注销",
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\" onclick=\"go('P3-R01-F08-基金详情.html')\">FUND-2024-005</span></td>\n<td><span class=\"lk\" onclick=\"go('P3-R01-F08-基金详情.html')\">上海临港智造股权投资合伙企业（有限合伙）</span></td>\n<td>3,000 万</td>\n<td>2024-06-28</td>\n<td>境内 · 上海临港</td>\n<td><span class=\"tag tag-gray\">已注销</span></td>\n<td><span style=\"color:var(--text-3);\">—</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F08-基金详情.html')\">详情</a><a>编辑</a></td>\n</tr>"
  },
  {
   "id": "FUND-2023-002",
   "status": "存续中",
   "tr": "<tr>\n<td><input type=\"checkbox\" class=\"cb\"></td>\n<td><span class=\"lk\" onclick=\"go('P3-R01-F08-基金详情.html')\">FUND-2023-002</span></td>\n<td><span class=\"lk\" onclick=\"go('P3-R01-F08-基金详情.html')\">宁波远见创业投资合伙企业（有限合伙）</span></td>\n<td>3,500 万</td>\n<td>2023-11-08</td>\n<td>境内 · 宁波</td>\n<td><span class=\"tag tag-blue\">存续中</span></td>\n<td><span style=\"color:var(--text-3);\">—</span> <span class=\"tag tag-blue tag-sm\">可关联</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F08-基金详情.html')\">详情</a><a>编辑</a></td>\n</tr>"
  }
 ],
 "batches": [
  {
   "id": "BAT-2025-001",
   "type": "分红",
   "typeCls": "tag-blue",
   "price": "0.10",
   "qty": "2,000",
   "amount": "200",
   "date": "2025-11-20",
   "principal": "0",
   "gain": "200",
   "gainCls": "num-pos",
   "rate": "—",
   "status": "已完成",
   "stCls": "tag-blue",
   "detail": "分红 0.10 元/份 × 2,000 万份 = 200 万元，2025-11-20 已完成",
   "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmBatDetail('BAT-2025-001')\">BAT-2025-001</span></td>\n<td><span class=\"tag tag-blue\">分红</span></td>\n<td>0.10</td>\n<td>2,000</td>\n<td>200</td>\n<td>2025-11-20</td>\n<td>0</td>\n<td class=\"num-pos\">200</td>\n<td>—</td>\n<td><span class=\"tag tag-blue\">已完成</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"dmBatDetail('BAT-2025-001')\">查看</a><a onclick=\"dmEditBat('BAT-2025-001')\">编辑</a></td>\n</tr>"
  },
  {
   "id": "BAT-2026-001",
   "type": "股权转让",
   "typeCls": "tag-blue",
   "price": "2.80",
   "qty": "1,000",
   "amount": "2,800",
   "date": "2026-05-18",
   "principal": "2,000",
   "gain": "800",
   "gainCls": "num-pos",
   "rate": "40%",
   "status": "已完成",
   "stCls": "tag-blue",
   "detail": "股权转让 1,000 万份 × 2.80 元/份 = 2,800 万元，本金回收 2,000 万、批次收益 800 万",
   "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmBatDetail('BAT-2026-001')\">BAT-2026-001</span></td>\n<td><span class=\"tag tag-blue\">股权转让</span></td>\n<td>2.80</td>\n<td>1,000</td>\n<td>2,800</td>\n<td>2026-05-18</td>\n<td>2,000</td>\n<td class=\"num-pos\">800</td>\n<td>40%</td>\n<td><span class=\"tag tag-blue\">已完成</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"dmBatDetail('BAT-2026-001')\">查看</a><a onclick=\"dmEditBat('BAT-2026-001')\">编辑</a><a onclick=\"go('P3-R01-F16-收益分配.html')\">收益分配</a></td>\n</tr>"
  },
  {
   "id": "BAT-2026-002",
   "type": "IPO 减持",
   "typeCls": "tag-orange",
   "price": "预计 3.50",
   "qty": "1,000",
   "amount": "预计 3,500",
   "date": "预计 2026-09",
   "principal": "预计 2,000",
   "gain": "预计 1,500",
   "gainCls": "num-pos",
   "rate": "预计 75%",
   "status": "待执行",
   "stCls": "tag-orange",
   "detail": "IPO 减持 1,000 万份 × 预计 3.50 元/份 = 预计 3,500 万元，预计 2026-09 窗口执行",
   "tr": "<tr>\n<td><span class=\"lk\" onclick=\"dmBatDetail('BAT-2026-002')\">BAT-2026-002</span></td>\n<td><span class=\"tag tag-orange\">IPO 减持</span></td>\n<td>预计 3.50</td>\n<td>1,000</td>\n<td>预计 3,500</td>\n<td>预计 2026-09</td>\n<td>预计 2,000</td>\n<td class=\"num-pos\">预计 1,500</td>\n<td>预计 75%</td>\n<td><span class=\"tag tag-orange\">待执行</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"dmBatDetail('BAT-2026-002')\">查看</a><a onclick=\"dmEditBat('BAT-2026-002')\">编辑</a><a class=\"danger-op\" onclick=\"dmCancelBat('BAT-2026-002')\">取消</a><a onclick=\"dmDeferBat('BAT-2026-002')\">展期</a></td>\n</tr>"
  }
 ],
 "distributions": [
  {
   "id": "DST-2026-001",
   "biz": "磐石一期 DST-2026-001",
   "detail": "基于批次 BAT-2026-001（股权转让 2,800 万元），按 LP 出资比例分配：宁波梅山远创 60% = 1,680 万元、悦达上海 40% = 1,120 万元",
   "src": "BAT-2026-001 股权转让 · 1,000 万份 × 2.80 元/份 = 2,800 万元 · 2026-05-18 完成",
   "voucher": "付款凭证-宁波梅山远创-20260610.pdf（已上传）",
   "tr": "<tr class=\"main-row\">\n<td><span class=\"exp-arrow open\" onclick=\"toggleSub(this)\" title=\"展开 / 收起\">▸</span></td>\n<td><span class=\"lk\" onclick=\"dmDstDetail()\">DST-2026-001</span></td>\n<td><span class=\"lk\" onclick=\"alert('来源批次：BAT-2026-001 股权转让 · 1,000 万份 × 2.80 元/份 = 2,800 万元 · 2026-05-18 完成')\">BAT-2026-001</span> · 股权转让</td>\n<td>2,800</td>\n<td><span class=\"tag tag-blue\">分配中</span></td>\n<td>2026-05-25</td>\n<td class=\"sticky-op ops\"><a onclick=\"openPay('悦达（上海）资产管理有限公司','1,120 万元')\">登记付款</a><a onclick=\"dmDstDetail()\">查看</a></td>\n</tr>\n<tr class=\"sub-row\">\n<td colspan=\"7\">\n<table class=\"lp-table\">\n<thead>\n<tr>\n<th>出资主体</th>\n<th>出资比例</th>\n<th data-note=\"1\">分配金额（万元）</th>\n<th>付款状态</th>\n<th>付款日期</th>\n<th>凭证 / 操作</th>\n</tr>\n</thead>\n<tbody>\n<tr data-pay=\"paid\">\n<td>宁波梅山远创投资合伙企业<span class=\"lp-sub\">LP-A 宁波梅山远见投资有限公司</span></td>\n<td>60%</td>\n<td class=\"num-pos\">1,680</td>\n<td><span class=\"tag tag-blue\">已付款</span></td>\n<td>2026-06-10</td>\n<td class=\"ops\"><a onclick=\"dmVoucher()\">查看凭证</a></td>\n</tr>\n<tr data-pay=\"unpaid\">\n<td>悦达（上海）资产管理有限公司<span class=\"lp-sub\">LP-B 江苏悦达产业资本</span></td>\n<td>40%</td>\n<td class=\"num-pos\">1,120</td>\n<td><span class=\"tag tag-orange\">待付款</span></td>\n<td>—</td>\n<td class=\"ops\"><a onclick=\"openPay('悦达（上海）资产管理有限公司','1,120 万元')\">登记付款</a></td>\n</tr>\n</tbody>\n</table>\n</td>\n</tr>"
  }
 ],
 "reports": [
  {
   "id": "RPT-2026-021",
   "prj": "云雀教育",
   "type": "季报",
   "period": "2026Q2",
   "status": "待上传",
   "tr": "<tr>\n<td><span class=\"lk\">RPT-2026-021</span></td>\n<td><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">云雀教育</span></td>\n<td><span class=\"tag tag-blue\">季报</span></td>\n<td>2026Q2</td>\n<td>2026-07-15</td>\n<td>—</td>\n<td>—</td>\n<td><span class=\"tag tag-orange\">⚠ 待上传 · 逾期 43 天（已升级）</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"openUpload('yunke','q','2026Q2')\">上传</a></td>\n</tr>"
  },
  {
   "id": "RPT-2026-018",
   "prj": "云雀教育",
   "type": "季报",
   "period": "2026Q1",
   "status": "已归档",
   "tr": "<tr>\n<td><span class=\"lk\">RPT-2026-018</span></td>\n<td><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">云雀教育</span></td>\n<td><span class=\"tag tag-blue\">季报</span></td>\n<td>2026Q1</td>\n<td>2026-04-15</td>\n<td>华悦</td>\n<td>2026-04-28</td>\n<td><span class=\"tag tag-blue\">已归档</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"dmViewReport('RPT-2026-018')\">预览</a><a onclick=\"alert('已开始下载')\">下载</a></td>\n</tr>"
  },
  {
   "id": "RPT-2026-009",
   "prj": "云雀教育",
   "type": "年报",
   "period": "2025年度",
   "status": "已归档",
   "tr": "<tr>\n<td><span class=\"lk\">RPT-2026-009</span></td>\n<td><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">云雀教育</span></td>\n<td><span class=\"tag tag-blue\">年报</span></td>\n<td>2025年度</td>\n<td>2026-03-31</td>\n<td>华悦</td>\n<td>2026-03-30</td>\n<td><span class=\"tag tag-blue\">已归档</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"dmViewReport('RPT-2026-009')\">预览</a><a onclick=\"alert('已开始下载')\">下载</a></td>\n</tr>"
  },
  {
   "id": "RPT-2026-015",
   "prj": "磐石精密制造",
   "type": "专项报告 · 清算",
   "period": "—",
   "status": "已归档",
   "tr": "<tr>\n<td><span class=\"lk\">RPT-2026-015</span></td>\n<td><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">磐石精密制造</span></td>\n<td><span class=\"tag tag-blue\">专项报告 · 清算</span></td>\n<td>—</td>\n<td>2026-06-30</td>\n<td>胡博</td>\n<td>2026-06-20</td>\n<td><span class=\"tag tag-blue\">已归档</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"dmViewReport('RPT-2026-015')\">预览</a><a onclick=\"alert('已开始下载')\">下载</a></td>\n</tr>"
  },
  {
   "id": "RPT-2026-012",
   "prj": "磐石精密制造",
   "type": "专项报告 · 上市减持",
   "period": "—",
   "status": "待上传",
   "tr": "<tr>\n<td><span class=\"lk\">RPT-2026-012</span></td>\n<td><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">磐石精密制造</span></td>\n<td><span class=\"tag tag-blue\">专项报告 · 上市减持</span></td>\n<td>—</td>\n<td>2026-09-30</td>\n<td>—</td>\n<td>—</td>\n<td><span class=\"tag tag-gray\">待上传</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"openUpload('panshi','s','上市减持方案')\">上传</a></td>\n</tr>"
  }
 ],
 "warnings": [
  {
   "id": "al1",
   "state": "unread",
   "tr": "<div class=\"alert-card unread al-red\" id=\"al1\">\n<div class=\"al-ico\"><span class=\"al-ico-c\"><svg width=\"22\" height=\"22\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><polyline points=\"23 18 13.5 8.5 8.5 13.5 1 6\"/><polyline points=\"17 18 23 18 23 12\"/></svg></span></div>\n<div class=\"al-main\">\n<div class=\"al-head\">\n<span class=\"al-title\"><span class=\"al-dot\"></span><b>股价跌破减持参考线</b></span>\n<span class=\"tag tag-red\">股价</span><span class=\"tag tag-gray\">系统</span>\n<span class=\"al-time\">2026-08-27 09:32</span>\n</div>\n<div class=\"al-desc\">收盘价 18.6 元，低于减持方案参考价 19.0 元，连续 5 个交易日，建议结合 9 月减持窗口评估退出批次执行 · 关联项目：<span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">磐石精密制造</span></div>\n<div class=\"al-foot ops\" id=\"alFoot1\">\n<a onclick=\"markRead('al1','alFoot1')\">标记已读</a>\n<a onclick=\"go('../退出管理/P3-R01-F15-项目退出.html')\">登记退出</a>\n</div>\n</div>\n</div>"
  },
  {
   "id": "al2",
   "state": "unread",
   "tr": "<div class=\"alert-card unread al-orange\" id=\"al2\">\n<div class=\"al-ico\"><span class=\"al-ico-c\"><svg width=\"22\" height=\"22\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M3 11l16-6v12L3 13v-2z\"/><path d=\"M11.6 16.8a3 3 0 1 1-5.8-1.6\"/></svg></span></div>\n<div class=\"al-main\">\n<div class=\"al-head\">\n<span class=\"al-title\"><span class=\"al-dot\"></span><b>法定代表人变更</b></span>\n<span class=\"tag tag-orange\">舆情</span><span class=\"tag tag-gray\">企查查</span>\n<span class=\"al-time\">2026-08-26 16:05</span>\n</div>\n<div class=\"al-desc\">市场主体信息变更，需核实是否影响投后条款 · 关联项目：<span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">云雀教育</span></div>\n<div class=\"al-foot ops\" id=\"alFoot2\">\n<a onclick=\"markRead('al2','alFoot2')\">标记已读</a>\n<a onclick=\"handleAlert('al2','alFoot2','alState2')\">处理</a>\n</div>\n</div>\n</div>"
  },
  {
   "id": "al3",
   "state": "unread",
   "tr": "<div class=\"alert-card unread al-orange\" id=\"al3\">\n<div class=\"al-ico\"><span class=\"al-ico-c\"><svg width=\"22\" height=\"22\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M4 22h16\"/><path d=\"M6 18V8a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v10\"/><path d=\"M6 12h12\"/><line x1=\"9\" y1=\"9.5\" x2=\"9\" y2=\"9.51\"/><line x1=\"12\" y1=\"9.5\" x2=\"12\" y2=\"9.51\"/><line x1=\"15\" y1=\"9.5\" x2=\"15\" y2=\"9.51\"/></svg></span></div>\n<div class=\"al-main\">\n<div class=\"al-head\">\n<span class=\"al-title\"><span class=\"al-dot\"></span><b>媒体报道：营收下滑传闻</b></span>\n<span class=\"tag tag-orange\">舆情</span><span class=\"tag tag-gray\">同花顺</span>\n<span class=\"al-time\">2026-08-25 11:20</span>\n</div>\n<div class=\"al-desc\">需与投后访谈数据交叉核实 · 关联项目：<span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">云雀教育</span></div>\n<div class=\"al-foot ops\" id=\"alFoot3\">\n<a onclick=\"markRead('al3','alFoot3')\">标记已读</a>\n<a onclick=\"handleAlert('al3','alFoot3','alState3')\">处理</a>\n</div>\n</div>\n</div>"
  },
  {
   "id": "al4",
   "state": "readUntreated",
   "tr": "<div class=\"alert-card al-red\" id=\"al4\">\n<div class=\"al-ico\"><span class=\"al-ico-c\"><svg width=\"22\" height=\"22\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><polyline points=\"23 6 13.5 15.5 8.5 10.5 1 18\"/><polyline points=\"17 6 23 6 23 12\"/></svg></span></div>\n<div class=\"al-main\">\n<div class=\"al-head\">\n<span class=\"al-title\"><b>减持窗口开启提示</b></span>\n<span class=\"tag tag-red\">股价</span><span class=\"tag tag-gray\">系统</span><span class=\"tag tag-gray\" id=\"alState4\">已读未处理</span>\n<span class=\"al-time\">2026-08-20 09:00</span>\n</div>\n<div class=\"al-desc\">IPO 减持窗口 2026-09-01 开启，可登记退出批次 · 关联项目：<span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">磐石精密制造</span></div>\n<div class=\"al-foot ops\" id=\"alFoot4\">\n<a onclick=\"handleAlert('al4','alFoot4','alState4')\">标记已处理</a>\n<a onclick=\"go('../退出管理/P3-R01-F15-项目退出.html')\">登记退出</a>\n</div>\n</div>\n</div>"
  },
  {
   "id": "al5",
   "state": "done",
   "tr": "<div class=\"alert-card al-orange\" id=\"al5\">\n<div class=\"al-ico\"><span class=\"al-ico-c\"><svg width=\"22\" height=\"22\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M3 11l16-6v12L3 13v-2z\"/><path d=\"M11.6 16.8a3 3 0 1 1-5.8-1.6\"/></svg></span></div>\n<div class=\"al-main\">\n<div class=\"al-head\">\n<span class=\"al-title\"><b>新增被执行人信息</b></span>\n<span class=\"tag tag-orange\">舆情</span><span class=\"tag tag-gray\">企查查</span><span class=\"tag tag-blue\">已处理</span>\n<span class=\"al-time\">2026-08-18 14:40</span>\n</div>\n<div class=\"al-desc\">触发被执行人信息预警 · 关联项目：<span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">星河航天</span></div>\n<div class=\"al-foot\">\n<span class=\"al-note\">处理说明：<b>已核实为同名企业，误报</b> · 2026-08-19 · 胡博</span>\n</div>\n</div>\n</div>"
  }
 ],
 "reminders": {
  "rules": [
   {
    "id": "ALR-2026-011",
    "tr": "<tr>\n<td><span class=\"lk\">ALR-2026-011</span></td>\n<td><span class=\"tag tag-orange\">对赌到期</span></td>\n<td><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">云雀教育（2026 年营收对赌）</span></td>\n<td>2027-06-30</td>\n<td>30 天</td>\n<td>吕道远、华悦</td>\n<td id=\"rs1\"><span class=\"tag tag-blue\">启用</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"openRuleModal('edit','dud','yunke_du','2027-06-30',30,['lyd','hy'])\">编辑</a><a id=\"rt1\" onclick=\"toggleRule(1)\">停用</a></td>\n</tr>"
   },
   {
    "id": "ALR-2026-011",
    "tr": "<tr>\n<td><span class=\"lk\">ALR-2026-010</span></td>\n<td><span class=\"tag tag-orange\">回购触发</span></td>\n<td><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">星河航天（投资协议回购条款）</span></td>\n<td>2026-12-31</td>\n<td>30 天</td>\n<td>胡博</td>\n<td id=\"rs2\"><span class=\"tag tag-blue\">启用</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"openRuleModal('edit','hg','xinghe_hg','2026-12-31',30,['hb'])\">编辑</a><a id=\"rt2\" onclick=\"toggleRule(2)\">停用</a></td>\n</tr>"
   },
   {
    "id": "ALR-2026-011",
    "tr": "<tr>\n<td><span class=\"lk\">ALR-2026-009</span></td>\n<td><span class=\"tag tag-blue\">资质续期</span></td>\n<td>华金（宁波梅山）股权投资有限公司</td>\n<td>2026-10-15</td>\n<td>45 天</td>\n<td>嘉怡</td>\n<td id=\"rs3\"><span class=\"tag tag-blue\">启用</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"openRuleModal('edit','zz','huajin_zz','2026-10-15',45,['jy'])\">编辑</a><a id=\"rt3\" onclick=\"toggleRule(3)\">停用</a></td>\n</tr>"
   },
   {
    "id": "ALR-2026-011",
    "tr": "<tr>\n<td><span class=\"lk\">ALR-2026-008</span></td>\n<td><span class=\"tag tag-blue\">履约核查</span></td>\n<td><span class=\"lk\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">云雀教育（分期出资履约）</span></td>\n<td>2026-09-08</td>\n<td>30 天</td>\n<td>华悦</td>\n<td id=\"rs4\"><span class=\"tag tag-blue\">启用</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"openRuleModal('edit','lv','yunke_lv','2026-09-08',30,['hy'])\">编辑</a><a id=\"rt4\" onclick=\"toggleRule(4)\">停用</a></td>\n</tr>"
   }
  ],
  "due": [
   {
    "tr": "<div class=\"feed-item cur\">\n<span class=\"feed-dot\"></span>\n<div class=\"feed-card\">\n<div class=\"feed-title\"><b>华金（宁波梅山）营业期限续展</b><span class=\"tag tag-blue\">资质续期</span><span class=\"tag tag-blue\">剩 49 天</span>\n<span class=\"due-op ops\"><a onclick=\"confirmDue(this)\">确认处理</a></span>\n</div>\n<div class=\"feed-meta\"><span>到期日：2026-10-15</span><span>提醒对象：嘉怡</span><span>对应规则：ALR-2026-009</span></div>\n</div>\n</div>"
   },
   {
    "tr": "<div class=\"feed-item\">\n<span class=\"feed-dot\"></span>\n<div class=\"feed-card\">\n<div class=\"feed-title\"><b>云雀教育 Q3 出资履约核查</b><span class=\"tag tag-blue\">履约核查</span><span class=\"tag tag-orange\">⚠ 剩 12 天</span>\n<span class=\"due-op ops\"><a onclick=\"confirmDue(this)\">确认处理</a></span>\n</div>\n<div class=\"feed-meta\"><span>到期日：2026-09-08</span><span>提醒对象：华悦</span><span>对应规则：ALR-2026-008</span></div>\n</div>\n</div>"
   },
   {
    "tr": "<div class=\"feed-item\">\n<span class=\"feed-dot\"></span>\n<div class=\"feed-card\">\n<div class=\"feed-title\"><b>星河航天投资协议回购条款跟踪</b><span class=\"tag tag-orange\">回购触发</span><span class=\"tag tag-blue\">剩 126 天</span></div>\n<div class=\"feed-meta\"><span>到期日：2026-12-31</span><span>提醒对象：胡博</span><span>对应规则：ALR-2026-010</span></div>\n</div>\n</div>"
   },
   {
    "tr": "<div class=\"feed-item\">\n<span class=\"feed-dot\"></span>\n<div class=\"feed-card\">\n<div class=\"feed-title\"><b>云雀教育 2026 年营收对赌</b><span class=\"tag tag-orange\">对赌到期</span><span class=\"tag tag-blue\">剩 307 天</span></div>\n<div class=\"feed-meta\"><span>到期日：2027-06-30</span><span>提醒对象：吕道远、华悦</span><span>对应规则：ALR-2026-011</span></div>\n</div>\n</div>"
   }
  ]
 },
 "postEvents": {
  "liquidationFunds": {
  'FUND-2025-011': {
    tag: '<span class="tag tag-orange">清算中 · 步骤 3/5</span>',
    badge: '',
    meta: '<span class="fm"><b>关联项目</b><span class="lk" onclick="go(\'P3-R01-F02-项目详情-项目概况.html\')">磐石精密制造</span><span class="tag tag-blue">已退出</span></span>'
      + '<span class="fm"><b>退出完成度</b>100%</span>'
      + '<span class="fm"><b>成立日期</b>2025-03-10</span>'
      + '<span class="fm"><b>注册资本</b>4,000 万元</span>',
    steps: [
      { t: '清算报告生成', s: 'done', note: '2026-06-20' },
      { t: '资产处置', s: 'done', note: '2026-07-15' },
      { t: '税务办理', s: 'cur', note: '进行中（预计 09-10）' },
      { t: '剩余财产分配', s: 'todo', note: '未开始' },
      { t: '工商注销', s: 'todo', note: '未开始' }
    ],
    op: '<div class="card-title">③ 税务办理<span style="margin-left:10px;font-size:12px;font-weight:400;color:var(--text-3);">当前步骤 3/5</span></div>'
      + '<p class="op-desc">办理基金清算期间的增值税、所得税清缴；完税凭证上传归档后，可推进至「剩余财产分配」并发起分配审批。</p>'
      + '<div class="op-grid">'
      + '<div class="upload-zone" onclick="this.querySelector(\'input\').click()">点击或拖拽上传<span class="up-strong">完税凭证</span>（税务局开具 / 扫描件）<input type="file" style="display:none"></div>'
      + '<div class="op-acts">'
      + '<button class="btn btn-primary" onclick="alert(\'已推进：剩余财产分配 待发起分配审批\')">推进至 ④ 剩余财产分配</button>'
      + '<a class="link-btn" onclick="go(\'P3-R01-F20-审批中心.html\')">查看分配审批 →</a>'
      + '</div></div>',
    docs: [
      { name: '清算报告-磐石一期.pdf', tag: '<span class="tag tag-blue">已上传</span>', meta: '步骤① 清算报告生成 · 2026-06-20 · 胡博', act: '预览' }
    ],
    feed: [
      { t: '税务申报材料提交', d: '增值税 / 所得税清算申报材料已递交主管税务机关', m: '2026-08-22 · 胡博', cur: true },
      { t: '资产处置完成', d: '转让对价 3,000 万元到账', m: '2026-07-15' },
      { t: '清算报告上传', d: '清算报告-磐石一期.pdf 归档至步骤材料', m: '2026-06-20 · 胡博' },
      { t: '发起清算审批通过', d: '清算方案经审批中心核准', m: '2026-06-15', tag: '<span class="tag tag-gray">已通过</span>' }
    ]
  },
  'FUND-2026-002': {
    tag: '<span class="tag tag-blue">存续中 · 未启动清算</span>',
    badge: '',
    meta: '<span class="fm"><b>关联项目</b><span>星河航天</span><span class="tag tag-orange">未退出</span></span>'
      + '<span class="fm"><b>退出完成度</b>0%</span>'
      + '<span class="fm"><b>成立日期</b>2026-08-10</span>'
      + '<span class="fm"><b>注册资本</b>8,000 万元</span>',
    steps: [
      { t: '清算报告生成', s: 'todo', note: '未开始' },
      { t: '资产处置', s: 'todo', note: '未开始' },
      { t: '税务办理', s: 'todo', note: '未开始' },
      { t: '剩余财产分配', s: 'todo', note: '未开始' },
      { t: '工商注销', s: 'todo', note: '未开始' }
    ],
    op: '<div class="card-title">发起清算</div>'
      + '<div class="warn-strip"><span>⚠</span><span>发起清算前系统校验：关联项目须已全部退出</span></div>'
      + '<div class="blk-meta">当前关联项目：星河航天（⑨ 出资 · 付款审批中）· 退出完成度 0%</div>'
      + '<button class="btn btn-primary" style="height:32px;font-size:13px;" onclick="alert(\'校验未通过：关联项目「星河航天」未全部退出，不可发起清算\')">发起清算</button>'
      + '<div class="f-hint" style="margin-top:10px;">基金存续中，待关联项目全部完成退出（⑪）后方可发起清算审批</div>',
    docs: [],
    feed: []
  },
  'FUND-2024-005': {
    tag: '<span class="tag tag-gray">已注销</span>',
    badge: '<span class="tag tag-gray">已注销 2025-06-20</span>',
    meta: '<span class="fm"><b>关联项目</b><span class="lk" onclick="go(\'P3-R01-F02-项目详情-项目概况.html\')">临港智造</span><span class="tag tag-gray">已注销归档</span></span>'
      + '<span class="fm"><b>退出完成度</b>100%</span>'
      + '<span class="fm"><b>成立日期</b>2024-06-28</span>'
      + '<span class="fm"><b>注册资本</b>3,000 万元</span>',
    steps: [
      { t: '清算报告生成', s: 'done', note: '2025-02-15' },
      { t: '资产处置', s: 'done', note: '2025-03-20' },
      { t: '税务办理', s: 'done', note: '2025-04-18' },
      { t: '剩余财产分配', s: 'done', note: '2025-05-30' },
      { t: '工商注销', s: 'done', note: '2025-06-20' }
    ],
    op: '<div class="card-title">⑤ 工商注销<span style="margin-left:10px;"><span class="tag tag-gray">已注销 2025-06-20</span></span></div>'
      + '<p class="op-desc">五步清算流程已全部完成，基金主体已注销并转入归档，全流程材料可在归档中查阅。</p>'
      + '<div class="op-acts" style="flex-direction:row;">'
      + '<button class="btn btn-primary" disabled>上传材料</button>'
      + '<button class="btn btn-primary" disabled>推进至下一步</button>'
      + '<a class="link-btn disabled">查看分配审批 →</a>'
      + '</div>'
      + '<div class="f-hint" style="margin-top:10px;">流程已完结，操作已锁定</div>',
    docs: [
      { name: '清算报告-临港智造.pdf', tag: '<span class="tag tag-gray">已归档</span>', meta: '步骤① 清算报告生成 · 2025-02-15 · 陈有', act: '预览' },
      { name: '工商注销核准通知书.pdf', tag: '<span class="tag tag-gray">已归档</span>', meta: '步骤⑤ 工商注销 · 2025-06-20 · 陈有', act: '预览' }
    ],
    feed: [
      { t: '工商注销完成', d: '注销核准通知书领取，基金转入归档', m: '2025-06-20 · 陈有' },
      { t: '剩余财产分配完成', d: '按 LP 出资比例分配完毕', m: '2025-05-30' },
      { t: '税务清缴完成', d: '增值税 / 所得税清算完毕', m: '2025-04-18' },
      { t: '发起清算审批通过', d: '清算方案经审批中心核准', m: '2025-01-20', tag: '<span class="tag tag-gray">已通过</span>' }
    ]
  }
},
  "invested": [
   {
    "tr": "<tr>\n<td>云雀教育</td>\n<td>FUND-2026-003 · 杭州云雀教育创业投资合伙企业（有限合伙）</td>\n<td>2026-05-02</td>\n<td>128</td>\n<td>半年度经营访谈（2026-08-15）</td>\n<td>2026Q1 季报（2026-04-28）</td>\n<td><span class=\"tag tag-orange\">1 条未读</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F11-投后事项.html')\">详情</a><a onclick=\"go('P3-R01-F11-投后事项.html')\">记事件</a></td>\n</tr>"
   },
   {
    "tr": "<tr>\n<td>磐石精密制造</td>\n<td>FUND-2025-011 · 深圳磐石一期股权投资合伙企业（有限合伙）</td>\n<td>2025-06-10</td>\n<td>444</td>\n<td>事件归档 <span class=\"tag tag-gray\">已退出</span></td>\n<td>专项报告 · 清算（2026-06-20）</td>\n<td>—</td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F11-投后事项.html')\">详情</a><a onclick=\"go('P3-R01-F11-投后事项.html')\">记事件</a></td>\n</tr>"
   },
   {
    "tr": "<tr>\n<td>星河航天</td>\n<td>FUND-2026-002 · 苏州工业园区星河航天投资合伙企业（有限合伙）</td>\n<td>—</td>\n<td>—</td>\n<td><span class=\"tag tag-blue\">⑨ 付款审批中 · 即将进入投后</span></td>\n<td>—</td>\n<td>—</td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F11-投后事项.html')\">详情</a><a onclick=\"go('P3-R01-F11-投后事项.html')\">记事件</a></td>\n</tr>"
   }
  ],
  "exiting": [
   {
    "tr": "<tr>\n<td>磐石精密制造</td>\n<td>FUND-2025-011 · 深圳磐石一期股权投资合伙企业（有限合伙）</td>\n<td>2,000 万份</td>\n<td>3,000 万元</td>\n<td>1,000 万元</td>\n<td>BAT-2026-002（共 3 批）</td>\n<td><span class=\"tag tag-blue\">已完成</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F15-项目退出.html')\">详情</a><a onclick=\"go('P3-R01-F15-项目退出.html')\">登记批次</a></td>\n</tr>"
   },
   {
    "tr": "<tr>\n<td>云雀教育 <span class=\"tag tag-gray\">⑩ 投后中</span></td>\n<td>FUND-2026-003 · 杭州云雀教育创业投资合伙企业（有限合伙）</td>\n<td>—</td>\n<td>—</td>\n<td>—</td>\n<td>—</td>\n<td><span class=\"tag tag-blue\">持仓中</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F15-项目退出.html')\">详情</a><a onclick=\"go('P3-R01-F15-项目退出.html')\">登记批次</a></td>\n</tr>"
   },
   {
    "tr": "<tr>\n<td>星河航天 <span class=\"tag tag-gray\">⑨ 付款审批中</span></td>\n<td>FUND-2026-002 · 苏州工业园区星河航天投资合伙企业（有限合伙）</td>\n<td>—</td>\n<td>—</td>\n<td>—</td>\n<td>—</td>\n<td><span class=\"tag tag-gray\">未进入退出</span></td>\n<td class=\"sticky-op ops\"><a onclick=\"go('P3-R01-F15-项目退出.html')\">详情</a><a onclick=\"go('P3-R01-F15-项目退出.html')\">登记批次</a></td>\n</tr>"
   }
  ]
 },
 "todoView": {
  "todos": [
   {
    "tr": "<div class=\"todo-item\" onclick=\"go('../审批中心/P3-R01-F20-审批中心.html')\">\n<span class=\"tag tag-blue\">投决上会</span>\n<span class=\"t-name\">聚变能源科技 · APV-2026-0037</span>\n<span class=\"t-sub\">投决会 · 0 天</span>\n</div>"
   },
   {
    "tr": "<div class=\"todo-item\" onclick=\"go('../审批中心/P3-R01-F20-审批中心.html')\">\n<span class=\"tag tag-blue\">基金注册审批</span>\n<span class=\"t-name\">蓝鲸生物医药 · APV-2026-0038</span>\n<span class=\"t-sub\">总经理审批 · 1 天</span>\n</div>"
   },
   {
    "tr": "<div class=\"todo-item\" onclick=\"go('../审批中心/P3-R01-F20-审批中心.html')\">\n<span class=\"tag tag-blue\">付款审批</span>\n<span class=\"t-name\">星河航天 · APV-2026-0039</span>\n<span class=\"t-sub\">财务审批 · 0 天</span>\n</div>"
   }
  ],
  "stalls": [
   {
    "tr": "<div class=\"stall-item\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">\n<span class=\"warn-days\">⚠ 停滞 47 天</span>\n<span class=\"t-name\">智驾千里 · ③ 保密协议签署</span>\n<span class=\"t-sub\">超 30 天未推进</span>\n</div>"
   },
   {
    "tr": "<div class=\"stall-item\" onclick=\"go('../项目库/P3-R01-F02-项目详情-项目概况.html')\">\n<span class=\"warn-days\">⚠ 停滞 33 天</span>\n<span class=\"t-name\">青禾农业科技 · ⑤ 立项</span>\n<span class=\"t-sub\">超 30 天未推进</span>\n</div>"
   }
  ],
  "mines": [
   {
    "tr": "<div class=\"todo-item\" onclick=\"go('../审批中心/P3-R01-F20-审批中心.html')\">\n<span class=\"tag tag-blue\">审批中</span>\n<span class=\"t-name\">APV-2026-0037 · 投决上会 · 聚变能源科技</span>\n<span class=\"t-sub\" onclick=\"event.stopPropagation();alert('已向当前审批人发送催办提醒');\">催办</span>\n</div>"
   },
   {
    "tr": "<div class=\"todo-item\" onclick=\"go('../审批中心/P3-R01-F20-审批中心.html')\">\n<span class=\"tag tag-blue\">已通过</span>\n<span class=\"t-name\">APV-2026-0030 · 立项审批 · 磐石量子</span>\n<span class=\"t-sub\">2026-08-21 通过</span>\n</div>"
   }
  ]
 },
 "dmFunnel": {
  "total": 36,
  "converting": 20,
  "invested": 6,
  "quit": 10,
  "gp": 8,
  "lp": 2,
  "rows": [
   {
    "tr": "<tr>\n<td><span class=\"stage-cell\">① 接触/收BP</span></td>\n<td>36</td>\n<td>31</td>\n<td>86%</td>\n<td><span class=\"num-red\">2</span></td>\n<td class=\"dim\">—</td>\n<td>6%</td>\n</tr>"
   },
   {
    "tr": "<tr>\n<td><span class=\"stage-cell\">② 线上路演</span></td>\n<td>31</td>\n<td>28</td>\n<td>90%</td>\n<td><span class=\"num-red\">1</span></td>\n<td class=\"dim\">—</td>\n<td>3%</td>\n</tr>"
   },
   {
    "tr": "<tr>\n<td><span class=\"stage-cell\">③ 保密协议签署</span></td>\n<td>28</td>\n<td>24</td>\n<td>86%</td>\n<td class=\"dim\">—</td>\n<td class=\"dim\">—</td>\n<td class=\"dim\">—</td>\n</tr>"
   },
   {
    "tr": "<tr>\n<td><span class=\"stage-cell\">④ 尽调/访谈</span></td>\n<td>24</td>\n<td>19</td>\n<td>79%</td>\n<td><span class=\"num-red\">2</span></td>\n<td class=\"dim\">—</td>\n<td>8%</td>\n</tr>"
   },
   {
    "tr": "<tr>\n<td><span class=\"stage-cell\">⑤ 立项</span></td>\n<td>19</td>\n<td>16</td>\n<td>84%</td>\n<td><span class=\"num-red\">1</span></td>\n<td class=\"dim\">—</td>\n<td>5%</td>\n</tr>"
   },
   {
    "tr": "<tr>\n<td><span class=\"stage-cell\">⑥ 投资人路演</span></td>\n<td>16</td>\n<td>14</td>\n<td>88%</td>\n<td><span class=\"num-red\">1</span></td>\n<td class=\"dim\">—</td>\n<td>6%</td>\n</tr>"
   },
   {
    "tr": "<tr>\n<td><span class=\"stage-cell\">⑦ 投决</span></td>\n<td>14</td>\n<td>6</td>\n<td>43%</td>\n<td><span class=\"num-red\">1</span></td>\n<td><span class=\"num-red\">2</span></td>\n<td>21%</td>\n</tr>"
   },
   {
    "tr": "<tr>\n<td><span class=\"stage-cell\">⑧ 基金设立</span></td>\n<td>6</td>\n<td>5</td>\n<td>83%</td>\n<td class=\"dim\">—</td>\n<td class=\"dim\">—</td>\n<td class=\"dim\">—</td>\n</tr>"
   },
   {
    "tr": "<tr>\n<td><span class=\"stage-cell\">⑨ 出资</span></td>\n<td>5</td>\n<td>4</td>\n<td>80%</td>\n<td class=\"dim\">—</td>\n<td class=\"dim\">—</td>\n<td class=\"dim\">—</td>\n</tr>"
   },
   {
    "tr": "<tr>\n<td><span class=\"stage-cell\">⑩ 投后管理</span></td>\n<td>4</td>\n<td>2</td>\n<td>50%</td>\n<td class=\"dim\">—</td>\n<td class=\"dim\">—</td>\n<td class=\"dim\">—</td>\n</tr>"
   },
   {
    "tr": "<tr>\n<td><span class=\"stage-cell\">⑪ 项目退出</span></td>\n<td>2</td>\n<td>1</td>\n<td>50%</td>\n<td class=\"dim\">—</td>\n<td class=\"dim\">—</td>\n<td class=\"dim\">—</td>\n</tr>"
   },
   {
    "tr": "<tr>\n<td><span class=\"stage-cell\">⑫ 清算注销</span></td>\n<td>1</td>\n<td class=\"dim\">—（终态）</td>\n<td class=\"dim\">—</td>\n<td class=\"dim\">—</td>\n<td class=\"dim\">—</td>\n<td class=\"dim\">—</td>\n</tr>"
   }
  ],
  "foot": "<tr>\n<td>合计（去重项目）</td>\n<td>36</td>\n<td class=\"dim\">—</td>\n<td class=\"dim\">—</td>\n<td><span class=\"num-red\">8</span></td>\n<td><span class=\"num-red\">2</span></td>\n<td>28%</td>\n</tr>"
 },
 "__f19Groups": [
  {
   "subject": "gp",
   "node": 1,
   "label": "① 看 BP 后不看"
  },
  {
   "subject": "gp",
   "node": 2,
   "label": "② 线上路演后"
  },
  {
   "subject": "gp",
   "node": 4,
   "label": "④ 访谈/尽调后"
  },
  {
   "subject": "gp",
   "node": 5,
   "label": "⑤ 立项时"
  },
  {
   "subject": "gp",
   "node": 6,
   "label": "⑥ 投资人路演后"
  },
  {
   "subject": "gp",
   "node": 7,
   "label": "⑦ 投决前主动撤回"
  },
  {
   "subject": "lp",
   "node": 7,
   "label": "⑦ 投决会否决"
  }
 ]
};
  store.capCalls = {
  f002: {
    name: 'FUND-2026-002 苏州工业园区星河航天投资合伙企业（有限合伙）',
    commit: '8,000', paid: '4,000', pct: 50, subs: 2,
    rows: [
      { id: 'CAP-2026-0001', sub: '宁波梅山远创投资合伙企业（有限合伙）', lp: 'LP-001 宁波梅山远见', commit: '4,800 万', commitCN: '四千八百万', paid: '2,400 万', ratio: '60%', last: '2026-08-20', st: '实缴中 · 50%', stCls: 'tag-orange' },
      { id: 'CAP-2026-0002', sub: '悦达（上海）资产管理有限公司', lp: 'LP-002 江苏悦达', commit: '3,200 万', commitCN: '三千二百万', paid: '1,600 万', ratio: '40%', last: '2026-08-20', st: '实缴中 · 50%', stCls: 'tag-orange' }
    ]
  },
  f003: {
    name: 'FUND-2026-003 杭州云雀教育创业投资合伙企业（有限合伙）',
    commit: '6,000', paid: '6,000', pct: 100, subs: 2,
    rows: [
      { id: 'CAP-2026-0007', sub: '宁波梅山远创投资合伙企业（有限合伙）', lp: 'LP-001 宁波梅山远见', commit: '3,600 万', commitCN: '三千六百万', paid: '3,600 万', ratio: '60%', last: '2026-02-10', st: '已缴足', stCls: 'tag-blue' },
      { id: 'CAP-2026-0008', sub: '悦达（上海）资产管理有限公司', lp: 'LP-002 江苏悦达', commit: '2,400 万', commitCN: '二千四百万', paid: '2,400 万', ratio: '40%', last: '2026-02-10', st: '已缴足', stCls: 'tag-blue' }
    ]
  },
  f011: {
    name: 'FUND-2025-011 深圳磐石一期股权投资合伙企业（有限合伙）',
    commit: '4,000', paid: '4,000', pct: 100, subs: 2,
    rows: [
      { id: 'CAP-2025-0021', sub: '宁波梅山远创投资合伙企业（有限合伙）', lp: 'LP-001 宁波梅山远见', commit: '2,400 万', commitCN: '二千四百万', paid: '2,400 万', ratio: '60%', last: '2025-04-18', st: '已缴足', stCls: 'tag-blue' },
      { id: 'CAP-2025-0022', sub: '悦达（上海）资产管理有限公司', lp: 'LP-002 江苏悦达', commit: '1,600 万', commitCN: '一千六百万', paid: '1,600 万', ratio: '40%', last: '2025-04-20', st: '已缴足', stCls: 'tag-blue' }
    ]
  }
};

  /* G05/A20：字典单源段（16 分类＝7 既有逐字迁移＋9 新收纳；rowTr＝F25 静态行区逐字源） */
  store.dictionaries = [
    {"key": "gp", "name": "放弃原因 · GP", "note": "按放弃节点分组的末级原因，供放弃登记与统计使用", "grouped": true, "nodes": ["① 看 BP 后不看", "② 线上路演后", "④ 访谈/尽调后", "⑤ 立项时", "⑥ 投资人路演后", "⑦ 投决前主动撤回"], "items": [{"name": "明显超出投资范围", "node": "① 看 BP 后不看", "status": "启用", "sort": 1}, {"name": "专业问题答不出/逻辑薄弱", "node": "② 线上路演后", "status": "启用", "sort": 1}, {"name": "团队能力不足", "node": "② 线上路演后", "status": "启用", "sort": 2}, {"name": "工厂萧条、订单匮乏", "node": "④ 访谈/尽调后", "status": "启用", "sort": 1}, {"name": "财务数据重大偏差", "node": "④ 访谈/尽调后", "status": "启用", "sort": 2}, {"name": "疑似造假", "node": "④ 访谈/尽调后", "status": "启用", "sort": 3}, {"name": "创始人信用风险/人品问题", "node": "⑤ 立项时", "status": "启用", "sort": 1}, {"name": "债务纠纷（老板否决）", "node": "⑤ 立项时", "status": "启用", "sort": 2}, {"name": "全体投资人明确不出资", "node": "⑥ 投资人路演后", "status": "启用", "sort": 1}, {"name": "估值未谈拢（打折未成）", "node": "⑦ 投决前主动撤回", "status": "启用", "sort": 1}, {"name": "对赌条款设置不合理", "node": "⑦ 投决前主动撤回", "status": "启用", "sort": 2}], "rowTr": "\n                      <tr class=\"group-row\"><td colspan=\"5\">① 看 BP 后不看<span class=\"g-cnt\">1 项</span></td></tr>\n                      <tr>\n                        <td class=\"leaf-name\">明显超出投资范围</td>\n                        <td>① 看 BP 后不看</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>1</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('明显超出投资范围')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：明显超出投资范围')\">停用</a></td>\n                      </tr>\n                      <tr class=\"group-row\"><td colspan=\"5\">② 线上路演后<span class=\"g-cnt\">2 项</span></td></tr>\n                      <tr>\n                        <td class=\"leaf-name\">专业问题答不出/逻辑薄弱</td>\n                        <td>② 线上路演后</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>1</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('专业问题答不出/逻辑薄弱')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：专业问题答不出/逻辑薄弱')\">停用</a></td>\n                      </tr>\n                      <tr>\n                        <td class=\"leaf-name\">团队能力不足</td>\n                        <td>② 线上路演后</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>2</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('团队能力不足')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：团队能力不足')\">停用</a></td>\n                      </tr>\n                      <tr class=\"group-row\"><td colspan=\"5\">④ 访谈/尽调后<span class=\"g-cnt\">3 项</span></td></tr>\n                      <tr>\n                        <td class=\"leaf-name\">工厂萧条、订单匮乏</td>\n                        <td>④ 访谈/尽调后</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>1</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('工厂萧条、订单匮乏')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：工厂萧条、订单匮乏')\">停用</a></td>\n                      </tr>\n                      <tr>\n                        <td class=\"leaf-name\">财务数据重大偏差</td>\n                        <td>④ 访谈/尽调后</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>2</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('财务数据重大偏差')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：财务数据重大偏差')\">停用</a></td>\n                      </tr>\n                      <tr>\n                        <td class=\"leaf-name\">疑似造假</td>\n                        <td>④ 访谈/尽调后</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>3</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('疑似造假')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：疑似造假')\">停用</a></td>\n                      </tr>\n                      <tr class=\"group-row\"><td colspan=\"5\">⑤ 立项时<span class=\"g-cnt\">2 项</span></td></tr>\n                      <tr>\n                        <td class=\"leaf-name\">创始人信用风险/人品问题</td>\n                        <td>⑤ 立项时</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>1</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('创始人信用风险/人品问题')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：创始人信用风险/人品问题')\">停用</a></td>\n                      </tr>\n                      <tr>\n                        <td class=\"leaf-name\">债务纠纷（老板否决）</td>\n                        <td>⑤ 立项时</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>2</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('债务纠纷（老板否决）')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：债务纠纷（老板否决）')\">停用</a></td>\n                      </tr>\n                      <tr class=\"group-row\"><td colspan=\"5\">⑥ 投资人路演后<span class=\"g-cnt\">1 项</span></td></tr>\n                      <tr>\n                        <td class=\"leaf-name\">全体投资人明确不出资</td>\n                        <td>⑥ 投资人路演后</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>1</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('全体投资人明确不出资')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：全体投资人明确不出资')\">停用</a></td>\n                      </tr>\n                      <tr class=\"group-row\"><td colspan=\"5\">⑦ 投决前主动撤回<span class=\"g-cnt\">2 项</span></td></tr>\n                      <tr>\n                        <td class=\"leaf-name\">估值未谈拢（打折未成）</td>\n                        <td>⑦ 投决前主动撤回</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>1</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('估值未谈拢（打折未成）')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：估值未谈拢（打折未成）')\">停用</a></td>\n                      </tr>\n                      <tr>\n                        <td class=\"leaf-name\">对赌条款设置不合理</td>\n                        <td>⑦ 投决前主动撤回</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>2</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('对赌条款设置不合理')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：对赌条款设置不合理')\">停用</a></td>\n                      </tr>\n                    "},
    {"key": "lp", "name": "放弃原因 · LP", "note": "投决会否决的末级原因，仅在 ⑦ 投决节点可选", "grouped": true, "nodes": ["⑦ 投决会否决"], "items": [{"name": "不看好行业", "node": "⑦ 投决会否决", "status": "启用", "sort": 1}, {"name": "不看好赛道", "node": "⑦ 投决会否决", "status": "启用", "sort": 2}, {"name": "项目风险异议", "node": "⑦ 投决会否决", "status": "启用", "sort": 3}, {"name": "估值异议", "node": "⑦ 投决会否决", "status": "启用", "sort": 4}, {"name": "政策/合规顾虑", "node": "⑦ 投决会否决", "status": "启用", "sort": 5}], "rowTr": "\n                      <tr class=\"group-row\"><td colspan=\"5\">⑦ 投决会否决<span class=\"g-cnt\">5 项</span></td></tr>\n                      <tr>\n                        <td class=\"leaf-name\">不看好行业</td>\n                        <td>⑦ 投决会否决</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>1</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('不看好行业')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：不看好行业')\">停用</a></td>\n                      </tr>\n                      <tr>\n                        <td class=\"leaf-name\">不看好赛道</td>\n                        <td>⑦ 投决会否决</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>2</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('不看好赛道')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：不看好赛道')\">停用</a></td>\n                      </tr>\n                      <tr>\n                        <td class=\"leaf-name\">项目风险异议</td>\n                        <td>⑦ 投决会否决</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>3</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('项目风险异议')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：项目风险异议')\">停用</a></td>\n                      </tr>\n                      <tr>\n                        <td class=\"leaf-name\">估值异议</td>\n                        <td>⑦ 投决会否决</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>4</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('估值异议')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：估值异议')\">停用</a></td>\n                      </tr>\n                      <tr>\n                        <td class=\"leaf-name\">政策/合规顾虑</td>\n                        <td>⑦ 投决会否决</td>\n                        <td><span class=\"tag tag-blue\">启用</span></td>\n                        <td>5</td>\n                        <td class=\"sticky-op ops\"><a onclick=\"dmEditDict('政策/合规顾虑')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：政策/合规顾虑')\">停用</a></td>\n                      </tr>\n                    "},
    {"key": "ind", "name": "行业赛道", "note": "项目建档与筛选使用的行业维度", "grouped": false, "items": [{"name": "人工智能", "status": "启用", "sort": 1}, {"name": "先进制造·新能源", "status": "启用", "sort": 2}, {"name": "医疗健康", "status": "启用", "sort": 3}, {"name": "半导体", "status": "启用", "sort": 4}, {"name": "低空经济", "status": "启用", "sort": 5}, {"name": "教育", "status": "启用", "sort": 6}, {"name": "新材料", "status": "启用", "sort": 7}, {"name": "农业科技", "status": "启用", "sort": 8}, {"name": "量子科技", "status": "启用", "sort": 9}], "rowTr": "\n                      <tr><td>人工智能</td><td><span class=\"tag tag-blue\">启用</span></td><td>1</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('人工智能')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：人工智能')\">停用</a></td></tr>\n                      <tr><td>先进制造·新能源</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('先进制造·新能源')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：先进制造·新能源')\">停用</a></td></tr>\n                      <tr><td>医疗健康</td><td><span class=\"tag tag-blue\">启用</span></td><td>3</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('医疗健康')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：医疗健康')\">停用</a></td></tr>\n                      <tr><td>半导体</td><td><span class=\"tag tag-blue\">启用</span></td><td>4</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('半导体')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：半导体')\">停用</a></td></tr>\n                      <tr><td>低空经济</td><td><span class=\"tag tag-blue\">启用</span></td><td>5</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('低空经济')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：低空经济')\">停用</a></td></tr>\n                      <tr><td>教育</td><td><span class=\"tag tag-blue\">启用</span></td><td>6</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('教育')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：教育')\">停用</a></td></tr>\n                      <tr><td>新材料</td><td><span class=\"tag tag-blue\">启用</span></td><td>7</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('新材料')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：新材料')\">停用</a></td></tr>\n                      <tr><td>农业科技</td><td><span class=\"tag tag-blue\">启用</span></td><td>8</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('农业科技')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：农业科技')\">停用</a></td></tr>\n                      <tr><td>量子科技</td><td><span class=\"tag tag-blue\">启用</span></td><td>9</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('量子科技')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：量子科技')\">停用</a></td></tr>\n                    "},
    {"key": "round", "name": "轮次", "note": "项目投资轮次维度", "grouped": false, "items": [{"name": "天使轮", "status": "启用", "sort": 1}, {"name": "Pre-A", "status": "启用", "sort": 2}, {"name": "A 轮", "status": "启用", "sort": 3}, {"name": "B 轮", "status": "启用", "sort": 4}, {"name": "定增", "status": "启用", "sort": 5}, {"name": "C 轮", "status": "停用", "sort": 6}], "rowTr": "\n                      <tr><td>天使轮</td><td><span class=\"tag tag-blue\">启用</span></td><td>1</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('天使轮')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：天使轮')\">停用</a></td></tr>\n                      <tr><td>Pre-A</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('Pre-A')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：Pre-A')\">停用</a></td></tr>\n                      <tr><td>A 轮</td><td><span class=\"tag tag-blue\">启用</span></td><td>3</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('A 轮')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：A 轮')\">停用</a></td></tr>\n                      <tr><td>B 轮</td><td><span class=\"tag tag-blue\">启用</span></td><td>4</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('B 轮')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：B 轮')\">停用</a></td></tr>\n                      <tr><td>定增</td><td><span class=\"tag tag-blue\">启用</span></td><td>5</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('定增')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：定增')\">停用</a></td></tr>\n                      <tr><td>C 轮</td><td><span class=\"tag tag-gray\">停用</span></td><td>6</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('C 轮')\">编辑</a><a onclick=\"alert('已启用：C 轮')\">启用</a></td></tr>\n                    "},
    {"key": "src", "name": "项目来源", "note": "项目建档时的来源渠道", "grouped": false, "items": [{"name": "主动接洽", "status": "启用", "sort": 1}, {"name": "机构推荐", "status": "启用", "sort": 2}, {"name": "行业峰会", "status": "启用", "sort": 3}, {"name": "政府引荐", "status": "启用", "sort": 4}, {"name": "LP 推荐", "status": "启用", "sort": 5}], "rowTr": "\n                      <tr><td>主动接洽</td><td><span class=\"tag tag-blue\">启用</span></td><td>1</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('主动接洽')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：主动接洽')\">停用</a></td></tr>\n                      <tr><td>机构推荐</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('机构推荐')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：机构推荐')\">停用</a></td></tr>\n                      <tr><td>行业峰会</td><td><span class=\"tag tag-blue\">启用</span></td><td>3</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('行业峰会')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：行业峰会')\">停用</a></td></tr>\n                      <tr><td>政府引荐</td><td><span class=\"tag tag-blue\">启用</span></td><td>4</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('政府引荐')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：政府引荐')\">停用</a></td></tr>\n                      <tr><td>LP 推荐</td><td><span class=\"tag tag-blue\">启用</span></td><td>5</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('LP 推荐')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：LP 推荐')\">停用</a></td></tr>\n                    "},
    {"key": "remind", "name": "提醒类型", "note": "提醒中心可配置的提醒类别", "grouped": false, "items": [{"name": "阶段停滞提醒", "status": "启用", "sort": 1}, {"name": "报告逾期提醒", "status": "启用", "sort": 2}, {"name": "证照到期提醒", "status": "启用", "sort": 3}, {"name": "付款节点提醒", "status": "启用", "sort": 4}, {"name": "审批超时提醒", "status": "启用", "sort": 2}], "rowTr": "\n                      <tr><td>阶段停滞提醒</td><td><span class=\"tag tag-blue\">启用</span></td><td>1</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('阶段停滞提醒')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：阶段停滞提醒')\">停用</a></td></tr>\n                      <tr><td>报告逾期提醒</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('报告逾期提醒')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：报告逾期提醒')\">停用</a></td></tr>\n                      <tr><td>证照到期提醒</td><td><span class=\"tag tag-blue\">启用</span></td><td>3</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('证照到期提醒')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：证照到期提醒')\">停用</a></td></tr>\n                      <tr><td>付款节点提醒</td><td><span class=\"tag tag-blue\">启用</span></td><td>4</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('付款节点提醒')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：付款节点提醒')\">停用</a></td></tr>\n                      <tr><td>审批超时提醒</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('审批超时提醒')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：审批超时提醒')\">停用</a></td></tr>\n                    "},
    {"key": "report", "name": "报告类型", "note": "投后报告归档的类别", "grouped": false, "items": [{"name": "月报", "status": "启用", "sort": 1}, {"name": "季报", "status": "启用", "sort": 2}, {"name": "年报", "status": "启用", "sort": 3}, {"name": "专项报告", "status": "启用", "sort": 4}], "rowTr": "\n                      <tr><td>月报</td><td><span class=\"tag tag-blue\">启用</span></td><td>1</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('月报')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：月报')\">停用</a></td></tr>\n                      <tr><td>季报</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('季报')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：季报')\">停用</a></td></tr>\n                      <tr><td>年报</td><td><span class=\"tag tag-blue\">启用</span></td><td>3</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('年报')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：年报')\">停用</a></td></tr>\n                      <tr><td>专项报告</td><td><span class=\"tag tag-blue\">启用</span></td><td>4</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('专项报告')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：专项报告')\">停用</a></td></tr>\n                    "},
    {"key": "apType", "name": "审批类型", "note": "审批发起使用的审批类型维度", "grouped": false, "items": [{"name": "立项审批", "status": "启用", "sort": 1, "slaHours": 72}, {"name": "投决上会", "status": "启用", "sort": 2, "slaHours": 120}, {"name": "基金注册审批", "status": "启用", "sort": 3, "slaHours": 48}, {"name": "付款审批", "status": "启用", "sort": 4, "slaHours": 24}, {"name": "收益分配审批", "status": "启用", "sort": 5, "slaHours": 48}, {"name": "注销审批", "status": "启用", "sort": 6, "slaHours": 72}, {"name": "认定审批", "status": "启用", "sort": 7, "slaHours": 48}], "rowTr": "<tr><td>立项审批</td><td><span class=\"tag tag-blue\">启用</span></td><td>1</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('立项审批')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：立项审批')\">停用</a></td></tr>\n<tr><td>投决上会</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('投决上会')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：投决上会')\">停用</a></td></tr>\n<tr><td>基金注册审批</td><td><span class=\"tag tag-blue\">启用</span></td><td>3</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('基金注册审批')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：基金注册审批')\">停用</a></td></tr>\n<tr><td>付款审批</td><td><span class=\"tag tag-blue\">启用</span></td><td>4</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('付款审批')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：付款审批')\">停用</a></td></tr>\n<tr><td>收益分配审批</td><td><span class=\"tag tag-blue\">启用</span></td><td>5</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('收益分配审批')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：收益分配审批')\">停用</a></td></tr>\n<tr><td>注销审批</td><td><span class=\"tag tag-blue\">启用</span></td><td>6</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('注销审批')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：注销审批')\">停用</a></td></tr>\n<tr><td>认定审批</td><td><span class=\"tag tag-blue\">启用</span></td><td>7</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('认定审批')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：认定审批')\">停用</a></td></tr>\n"},
    {"key": "exitType", "name": "退出类型", "note": "项目退出登记使用的退出方式维度", "grouped": false, "items": [{"name": "分红", "status": "启用", "sort": 1}, {"name": "股权转让", "status": "启用", "sort": 2}, {"name": "IPO 减持", "status": "启用", "sort": 3}], "rowTr": "<tr><td>分红</td><td><span class=\"tag tag-blue\">启用</span></td><td>1</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('分红')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：分红')\">停用</a></td></tr>\n<tr><td>股权转让</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('股权转让')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：股权转让')\">停用</a></td></tr>\n<tr><td>IPO 减持</td><td><span class=\"tag tag-blue\">启用</span></td><td>3</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('IPO 减持')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：IPO 减持')\">停用</a></td></tr>\n"},
    {"key": "eventType", "name": "事件类型", "note": "投后事项记录使用的事件类型维度", "grouped": false, "items": [{"name": "股东会决议", "status": "启用", "sort": 1}, {"name": "董事会决议", "status": "启用", "sort": 2}, {"name": "重大经营变动", "status": "启用", "sort": 3}, {"name": "访谈纪要", "status": "启用", "sort": 4}, {"name": "其他", "status": "启用", "sort": 5}], "rowTr": "<tr><td>股东会决议</td><td><span class=\"tag tag-blue\">启用</span></td><td>1</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('股东会决议')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：股东会决议')\">停用</a></td></tr>\n<tr><td>董事会决议</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('董事会决议')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：董事会决议')\">停用</a></td></tr>\n<tr><td>重大经营变动</td><td><span class=\"tag tag-blue\">启用</span></td><td>3</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('重大经营变动')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：重大经营变动')\">停用</a></td></tr>\n<tr><td>访谈纪要</td><td><span class=\"tag tag-blue\">启用</span></td><td>4</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('访谈纪要')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：访谈纪要')\">停用</a></td></tr>\n<tr><td>其他</td><td><span class=\"tag tag-blue\">启用</span></td><td>5</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('其他')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：其他')\">停用</a></td></tr>\n"},
    {"key": "reportSpecial", "name": "专项报告类型", "note": "专项报告上传使用的专项类型维度", "grouped": false, "items": [{"name": "上市减持方案", "status": "启用", "sort": 1}, {"name": "清算报告", "status": "启用", "sort": 2}, {"name": "重大事项专项", "status": "启用", "sort": 3}], "rowTr": "<tr><td>上市减持方案</td><td><span class=\"tag tag-blue\">启用</span></td><td>1</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('上市减持方案')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：上市减持方案')\">停用</a></td></tr>\n<tr><td>清算报告</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('清算报告')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：清算报告')\">停用</a></td></tr>\n<tr><td>重大事项专项</td><td><span class=\"tag tag-blue\">启用</span></td><td>3</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('重大事项专项')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：重大事项专项')\">停用</a></td></tr>\n"},
    {"key": "fundFileType", "name": "基金文件类型", "note": "基金资料包归档使用的文件类型维度", "grouped": false, "items": [{"name": "LPA", "status": "启用", "sort": 1}, {"name": "工商注册文件", "status": "启用", "sort": 2}, {"name": "实缴凭证", "status": "启用", "sort": 3}, {"name": "清算报告", "status": "启用", "sort": 4}, {"name": "其他", "status": "启用", "sort": 5}], "rowTr": "<tr><td>LPA</td><td><span class=\"tag tag-blue\">启用</span></td><td>1</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('LPA')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：LPA')\">停用</a></td></tr>\n<tr><td>工商注册文件</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('工商注册文件')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：工商注册文件')\">停用</a></td></tr>\n<tr><td>实缴凭证</td><td><span class=\"tag tag-blue\">启用</span></td><td>3</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('实缴凭证')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：实缴凭证')\">停用</a></td></tr>\n<tr><td>清算报告</td><td><span class=\"tag tag-blue\">启用</span></td><td>4</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('清算报告')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：清算报告')\">停用</a></td></tr>\n<tr><td>其他</td><td><span class=\"tag tag-blue\">启用</span></td><td>5</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('其他')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：其他')\">停用</a></td></tr>\n"},
    {"key": "orgForm", "name": "组织形式", "note": "基金建档使用的组织形式维度", "grouped": false, "items": [{"name": "有限合伙", "status": "启用", "sort": 1}, {"name": "公司型", "status": "启用", "sort": 2}], "rowTr": "<tr><td>有限合伙</td><td><span class=\"tag tag-blue\">启用</span></td><td>1</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('有限合伙')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：有限合伙')\">停用</a></td></tr>\n<tr><td>公司型</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('公司型')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：公司型')\">停用</a></td></tr>\n"},
    {"key": "warnType", "name": "预警类型", "note": "风险预警卡片使用的预警类型维度", "grouped": false, "items": [{"name": "股价", "status": "启用", "sort": 1}, {"name": "舆情", "status": "启用", "sort": 2}], "rowTr": "<tr><td>股价</td><td><span class=\"tag tag-blue\">启用</span></td><td>1</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('股价')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：股价')\">停用</a></td></tr>\n<tr><td>舆情</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('舆情')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：舆情')\">停用</a></td></tr>\n"},
    {"key": "warnSource", "name": "信息来源", "note": "风险预警卡片使用的信息来源维度", "grouped": false, "items": [{"name": "系统", "status": "启用", "sort": 1}, {"name": "企查查", "status": "启用", "sort": 2}, {"name": "同花顺", "status": "启用", "sort": 3}], "rowTr": "<tr><td>系统</td><td><span class=\"tag tag-blue\">启用</span></td><td>1</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('系统')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：系统')\">停用</a></td></tr>\n<tr><td>企查查</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('企查查')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：企查查')\">停用</a></td></tr>\n<tr><td>同花顺</td><td><span class=\"tag tag-blue\">启用</span></td><td>3</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('同花顺')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：同花顺')\">停用</a></td></tr>\n"},
    {"key": "role", "name": "系统角色", "note": "用户与角色管理使用的系统角色维度", "grouped": false, "items": [{"name": "超级管理员", "status": "启用", "sort": 1}, {"name": "投资经理", "status": "启用", "sort": 2}, {"name": "投后专员", "status": "启用", "sort": 3}, {"name": "只读", "status": "启用", "sort": 4}], "rowTr": "<tr><td>超级管理员</td><td><span class=\"tag tag-blue\">启用</span></td><td>1</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('超级管理员')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：超级管理员')\">停用</a></td></tr>\n<tr><td>投资经理</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('投资经理')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：投资经理')\">停用</a></td></tr>\n<tr><td>投后专员</td><td><span class=\"tag tag-blue\">启用</span></td><td>3</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('投后专员')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：投后专员')\">停用</a></td></tr>\n<tr><td>只读</td><td><span class=\"tag tag-blue\">启用</span></td><td>4</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('只读')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：只读')\">停用</a></td></tr>\n"},
    {"key": "ruleType", "name": "提醒规则类型", "note": "提醒规则触发使用的事件维度", "grouped": false, "items": [{"name": "对赌到期", "status": "启用", "sort": 1}, {"name": "回购触发", "status": "启用", "sort": 2}, {"name": "履约核查", "status": "启用", "sort": 3}, {"name": "资质续期", "status": "启用", "sort": 4}, {"name": "审批超时提醒", "status": "启用", "sort": 5}, {"name": "认定到期", "status": "启用", "sort": 6}], "rowTr": "<tr><td>对赌到期</td><td><span class=\"tag tag-blue\">启用</span></td><td>1</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('对赌到期')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：对赌到期')\">停用</a></td></tr>\n<tr><td>回购触发</td><td><span class=\"tag tag-blue\">启用</span></td><td>2</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('回购触发')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：回购触发')\">停用</a></td></tr>\n<tr><td>履约核查</td><td><span class=\"tag tag-blue\">启用</span></td><td>3</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('履约核查')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：履约核查')\">停用</a></td></tr>\n<tr><td>资质续期</td><td><span class=\"tag tag-blue\">启用</span></td><td>4</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('资质续期')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：资质续期')\">停用</a></td></tr>\n<tr><td>审批超时提醒</td><td><span class=\"tag tag-blue\">启用</span></td><td>5</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('审批超时提醒')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：审批超时提醒')\">停用</a></td></tr>\n<tr><td>认定到期</td><td><span class=\"tag tag-blue\">启用</span></td><td>6</td><td class=\"sticky-op ops\"><a onclick=\"dmEditDict('认定到期')\">编辑</a><a class=\"danger-op\" onclick=\"alert('已停用：认定到期')\">停用</a></td></tr>\n"}
  ];
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

  /* G05/T4：字典分类查找 */
  function dict(key) {
    for (var i = 0; i < store.dictionaries.length; i++) { if (store.dictionaries[i].key === key) { return store.dictionaries[i]; } }
    return null;
  }
  /* G05/T4：枚举下拉数据驱动——保留前 keep 个静态占位项，其余按字典生成；
     与原静态项文本相同者逐字保留其 value/selected/disabled 属性（零丢失）；
     停用项不生成（以现状静态为准绳，过滤策略登记待议） */
  function dmFillSelect(sel, key, keep) {
    if (!sel) { return false; }
    var d = dict(key);
    if (!d) { return false; }
    keep = keep || 0;
    var attrs = {};
    for (var j = sel.options.length - 1; j >= keep; j--) {
      var o = sel.options[j];
      attrs[o.text] = { value: o.getAttribute('value'), selected: o.selected, disabled: o.disabled };
      sel.remove(j);
    }
    for (var k = 0; k < d.items.length; k++) {
      var it = d.items[k];
      if (it.status === '停用') { continue; }
      var op = document.createElement('option');
      op.text = it.name;
      var a = attrs[it.name];
      if (a) {
        if (a.value !== null && a.value !== '') { op.setAttribute('value', a.value); }
        if (a.selected) { op.selected = true; }
        if (a.disabled) { op.disabled = true; }
      }
      sel.appendChild(op);
    }
    return true;
  }
  return { store: store, pages: pages, renderList: renderList, renderAll: renderAll, esc: esc, byId: byId, dict: dict, dmFillSelect: dmFillSelect };
})();
