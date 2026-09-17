# G06 变更零上下文独立复核报告

复核对象：FundFlow 投资项目管理原型 G06（评审决策落地与字典 v2）；基线=e88825b（goal 前存档），后=当前工作区；全部证据为本复核自行重跑（Playwright file:// 直开、每页新建 page、pageerror+console.error 双监听；git 基线用 `git show e88825b:<路径>` 重取）。

复核1 PASS
证据：e88825b 的 P3-R01-原型说明.md 版本行含 V1.13；当前版本行=「| 版本 | V1.14（09-15 评审决策落地与字典 v2（见 P2-R01-A21，goal G06）：字典 v2——apType 升 7 项全称…」且全文无 V1.15+；agent-handoff/goal-20260915-评审落地-失败清单.md 不存在；e88825b 的 _data/demo-data.js 含 dictionaries、无 ruleType、apType items=6（立项/投决/基金注册/付款/分配/注销），当前 apType items=7（立项审批/投决上会/基金注册审批/付款审批/收益分配审批/注销审批/认定审批，各带 slaHours）且有 ruleType；e88825b 的 _索引.md G06 行状态列=「待执行 | —」（无已完成、无哈希），当前 G06 行=「已完成 | 2fa012c」；git log 存在 e88825b「goal 前工作区存档」。

复核2 PASS
证据：F25 数据字典页实测——window.DM=true；DM.store.dictionaries.length=17；.dict-side .dict-item=17；DM.dict('apType').items 7 项、末项=认定审批、7 项 slaHours 全为数字 [72,120,48,24,48,72,48]；DM.dict('ruleType').items=6 项逐字=[对赌到期,回购触发,履约核查,资质续期,审批超时提醒,认定到期]；#dp-apType tbody tr=7、#dp-ruleType tbody tr=6；JS 错误 0（双监听均未触发）；readyState=complete。

复核3 PASS
证据：a) F20 #newModal 内含「立项」静态项的 select options 恰 8 项且逐字=['请选择','立项审批','投决上会','基金注册审批','付款审批','收益分配审批','注销审批','认定审批']；b) 新旧 demo-data.js 对比——旧 16 分类 key 除 apType 外 15 个（gp/lp/ind/round/src/remind/report/exitType/eventType/reportSpecial/fundFileType/orgForm/warnType/warnSource/role）items 原文与 JSON 解析双口径逐字一致（items 数 11/5/9/6/5/5/4/3/5/3/5/2/2/3/4），分类 key 旧 16→当前 17（仅新增 ruleType、仅 apType 有意变更）；c) F14 文件内 #rlType 静态 options=5 项（对赌到期/回购触发/履约核查/资质续期/审批超时提醒）且全文无 dmFillSelect 调用。

复核4 PASS
证据（11 页 Playwright 逐项实测，页均 0 JS 错误）——F09：#dmQualValid=「24 个月（自认定通过日起算）」，弹窗主按钮=「提交认定审批」，confirmVerify() alert=「认定审批已提交：总经理审批 · 审批人 嘉怡（APV-2026-0040）」；F15：#dmStRemainS=「初始 2,000 万份 − 已退出 1,000 万份 = 剩余 1,000 万份」，openBatModal 后 #exType 选「IPO 减持」#dmCompBlock display:block 可见、选「股权转让」display:none 隐藏，dmCkLock/dmCkDisc/dmCkQuota（INPUT）与 dmReviewer（INPUT）在位，IPO 未全勾 dmCompCheck() 返回 false 且 alert=「IPO 减持合规复核未通过：锁定期已满 / 预披露已完成 / 90 日额度校验须全勾选，并填写复核人（从严拦截）」，BAT-2026-002 行操作列含 取消/展期（整格文本「查看编辑取消展期」），dmDeferBat alert=「已登记展期：BAT-2026-002（新执行窗口另行确认，行内留痕，不走审批）」，dmCancelBat（prompt 填「复核取消原因」）后该行第 10 列 tag 文本=已取消、class="tag tag-gray"、alert 含「已留痕」；F08：#dmWcCommit/#dmWcPaid/#dmWcInvested/#dmWcRemain=8,000万元/4,000万元/1,500万元/2,500万元，dmCallRemind() 后 #dmCallModal show=true 且 #dmCallBody 恰 2 行（含 CAP-2026-0001 与 CAP-2026-0002），dmSendCall() alert 以「已发送付款节点提醒」开头；F02：#dmSpecTermCard（头部=特殊条款）后随 fgrid2 五要素齐全=回售权/生效中/2028-12-31 前未合格上市/实际控制人回购 · 年单利 8%/2028-12-31；F16：#dmWaterfallCard 含 800 万/160/128/512/60/40 与灰字注记「静态演示顺序，BS 版按合伙协议计算」；F13：dmOpenHandle('al2','alFoot2','alState2') 打开 #dmHandleModal，空说明 dmSubmitHandle() alert=「请填写处理说明（必填，留痕口径）」且弹窗保持打开，填写 #dmHandleNote 后提交——al2 卡 head 出现「<span class="tag tag-blue">已处理</span>」、foot=「<span class="al-note">处理说明：<b>G06复核：已联系企业补齐年报</b> · 2026-09-15 · 华悦</span>」（对齐 al5 样式），页签计数 before{all5,unread3,ru1,done1}→after{all5,unread2,ru1,done2}；F12：RPT-2026-021 行含「⚠ 待上传 · 逾期 43 天（已升级）」；F20：openApproval('APV-2026-0037','投决上会','聚变能源科技 PRJ-2026-0001','吕道远','2026-08-27','投决会','x') 后 #apOwner=吕道远、#dmApApprover=胡博，DM.store.approvals.todo 含 {id:"APV-2026-0040",type:"认定审批",node:"总经理审批"}，#dmBodyTodo 行数=4；F07：香港远航行（FUND-2025-007）含「6,500 万 (USD)」；F00：.stall-item 恰 2 条=「⚠ 停滞 47 天 | 智驾千里 · ③ 保密协议签署 | 超 30 天未推进」＋「⚠ 停滞 33 天 | 青禾农业科技 · ⑤ 立项 | 超 30 天未推进」，停滞列表内不含磐石量子（全页扫描磐石量子仅命中 1 处、位于审批待办卡 t-name「APV-2026-0030 · 立项审批 · 磐石量子」，insideStallItem=false）；F01：DM.store.projects 中 ops='arch' 恰 10 行（海豚半导体/风行低空/晶彩光电/驭光微纳/蓝湾储能/恒宇装备/青云网络/南汐生物/千乘出行/蓝湾机器人），10 行「归档详情」链接与项目名 lk 的 onclick 均含 dmAbDetail（两两成对=dmAbDetail('<项目名>')），dmAbDetail('晶彩光电') 打开 #dmAbModal（show=true）标题=「晶彩光电 · 未投归档详情」。

复核5 PASS
证据：23 页逐页 PASS 清单（每页 readyState=complete、pageerror+console.error 双监听错误=0）——F00 P3-R01-原型/工作台/P3-R01-F00-工作台.html PASS；F24 工作台/P3-R01-F24-登录.html PASS；F01 项目库/P3-R01-F01-项目列表.html PASS；F02 项目库/P3-R01-F02-项目详情-项目概况.html PASS；F03 项目库/P3-R01-F03-项目详情-材料库.html PASS；F07 基金管理/P3-R01-F07-基金列表.html PASS；F08 基金管理/P3-R01-F08-基金详情.html PASS；F09 LP 管理/P3-R01-F09-LP台账.html PASS；F10 LP 管理/P3-R01-F10-LP出资.html PASS；F11 投后管理/P3-R01-F11-投后事项.html PASS；F12 投后管理/P3-R01-F12-报告归档.html PASS；F13 投后管理/P3-R01-F13-风险预警.html PASS；F14 投后管理/P3-R01-F14-提醒中心.html PASS；F22 投后管理/P3-R01-F22-投后项目.html PASS；F15 退出管理/P3-R01-F15-项目退出.html PASS；F16 退出管理/P3-R01-F16-收益分配.html PASS；F17 退出管理/P3-R01-F17-清算注销.html PASS；F23 退出管理/P3-R01-F23-退出项目.html PASS；F18 统计报表/P3-R01-F18-阶段漏斗.html PASS；F19 统计报表/P3-R01-F19-放弃原因分布.html PASS；F20 审批中心/P3-R01-F20-审批中心.html PASS；F21 系统管理/P3-R01-F21-用户与角色.html PASS；F25 系统管理/P3-R01-F25-数据字典.html PASS。
PASS 23/23, FAIL 0, JS错误 0

复核6 PASS
证据：a) P2-R01/P2-R01-A21-需求调整记录-20260915.md 存在，含 slaHours 默认值行「slaHours 默认（付款 24/基金注册 48/收益分配 48/认定 48/立项 72/注销 72/投决上会 120）」（即付款 24/投决上会 120 命中）与「## 二、A20 待议映射（8 项处置）」；b) P3-R01-原型说明.md 版本行=「| 版本 | V1.14…」；c) PRD 10.2 节含 A21 行「| P2-R01-A21 | P2-R01/ | 需求调整记录-20260915.md，评审决策落地与字典 v2（goal G06）：模拟评审 28 问批 1 结论落档…」（注：PRD 实际路径为仓库根 P2-R01-产品需求文档.md，任务书所写 P2-R01/ 子目录下无此文件）；d) agent-handoff/_索引.md G06 行含 2fa012c 且状态=已完成。

复核7 PASS
证据：agent-handoff/goal-20260915-评审落地-失败清单.md 不存在（os.path.exists=False）→ 结论「无失败项」。

复核8 PASS
证据：git log --format='%h %s' 存在 2fa012c「G06 主体（T1-T11）：A21 评审批1口径落档…」与 a695583「G06 收尾回写：任务文档标完成＋执行记录…」，与「G06 主体」「G06 收尾回写」匹配；git status --porcelain 复核起始时为空，终态仅多 1 行「?? agent-handoff/_g06_verify/」——即本复核唯一获准的临时产物目录（未跟踪新目录，含本报告），属任务书预见的正常注明项，非工作区改动。

子agent复核总结论：PASS（8/8）
