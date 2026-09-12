# _AGENT基线 · 投资项目管理（FundFlow）

> **用途**：本项目面向 agent（无人值守 goal / 新会话）的**常驻基线**——项目上下文、关键路径、口径纪律铁律、工具链全在这里。全项目唯一、滚动更新；任务档案见 `_索引.md`，一个 goal 一个任务文档。
> **维护约定**：每次 goal 收尾必须回写本文件（新现状/新路径/新口径）；本文件与历史文档冲突时以本文件为准。
> **迁移注记（2026-09-12）**：本基线抽取自原 `AGENT-交接文档.md` §一（该文件已冻结归档，其「二、当前任务」迁出为 `20260908-G01-命名合规治理.md`）。根路径由来源机 Windows（`D:\工作台-吕道远\5-【ACTIVE】投资项目管理`）适配为本机 macOS 根；历史文档（A 系列记录/旧交接文档/.research）中的 Windows 路径按映射阅读，不改原文。

---

## 一、项目根与路径声明

- **项目根（全部相对路径以此拼接，执行会话 cwd 不可依赖）**：`/Users/bailey/Desktop/xiaohei-workplace/FundFlow`
- 失败清单（按任务创建，命名沿用 `goal-<日期>-<主题>-失败清单.md`）：`/Users/bailey/Desktop/xiaohei-workplace/FundFlow/agent-handoff/goal-<日期>-<主题>-失败清单.md`

## 二、项目是什么

私募股权基金管理人（GP）自用的投资项目管理系统**高保真静态原型**（纯 HTML 单文件、file:// 直开、#1677ff 主色、admin-ui-spec 体系）。业务主线：项目十二阶段①~⑫（投前管道①~⑦宽口径入库+七放弃节点→分水岭⑧基金设立/⑨出资→投后⑩~⑫）+ 六节点在线审批 + 资料包六类 + LP 认缴实缴两步 + 退出三段递进。

## 三、现状基线（2026-09-07 时点，原型说明 V1.5）

- **页面**：21 页（F00 工作台登录默认页 + F01~F03/F07~F21 + F22 投后项目/F23 退出项目两段列表页〔A12 新增〕；F11/F15 为详情页），置 `P3-R01-原型/` 按一级菜单九文件夹归类（工作台1/项目库3/基金管理2/LP管理2/投后管理5/退出与分配4/统计报表2/审批中心1/系统管理1）；F04/F05/F06 已并入或归档（99-归档/）
- **菜单**：一级 9 项 = 工作台 + 项目库/基金管理 2 直达 + LP 管理/投后管理/退出与分配/统计报表/审批中心/系统管理 6 组；投后管理 4 项（投后项目 F22/报告归档/风险预警/提醒中心）、退出与分配 3 项（退出项目 F23/收益分配/清算注销）、审批中心单项「审批中心」（A12）；详情页不进菜单（列表行进入，A05/A12 口径）
- **已完成的四轮治理（勿重做）**：A09 审批双轨（通过/退回/否决+撤回+抄送我）与 F00 工作台；A10 菜单六项更名（项目库/LP 台账/LP 出资/投后事项/我的审批/基础数据）；A11 术语全项目统一 + 原型标注层（P3-R01-D02-原型标注数据.json，20 条/13 页，改标注只改 json 重跑注入，注入器格式以 F12 重建逐字节比对校准）；A12 原型五组改造（F22/F23 段列表页+菜单结构+F10 金额输入反转+目录重构 P3-R01-原型+admin-ui-spec 践行+D04 导航图）
- **目录现状**：`P3-R01-原型/`（21 F 页按九文件夹归类 + D02-原型标注数据.json 与 D04-业务流程导航图.html 居新根层；D01-页面关系图/D03-演示导览已移 99-归档/，`_demo_*.html` 历史脚手架留新根层待人工清理）

## 四、关键路径（绝对）

| 对象 | 路径 |
|---|---|
| 原型根（现状） | `/Users/bailey/Desktop/xiaohei-workplace/FundFlow/P3-R01-原型` |
| 原型说明（版本行=防并行覆盖标记） | `/Users/bailey/Desktop/xiaohei-workplace/FundFlow/P3-R01-原型说明.md`（当前 **V1.5**） |
| 术语表（唯一术语源） | `/Users/bailey/Desktop/xiaohei-workplace/FundFlow/P1-R02-术语表.md` |
| 需求调整记录（A 系列，下一个号 **A13**） | `/Users/bailey/Desktop/xiaohei-workplace/FundFlow/P2-R01/` |
| PRD（第十节=编码规则+10.2 文档清单） | `/Users/bailey/Desktop/xiaohei-workplace/FundFlow/P2-R01-产品需求文档.md` |
| 归档区（只进不动既有文件） | `/Users/bailey/Desktop/xiaohei-workplace/FundFlow/99-归档` |
| UI 规范技能 | `/Users/bailey/.zcode/skills/admin-ui-spec/SKILL.md` |
| 命名/编码技能 | `/Users/bailey/.zcode/skills/文件名编码管理/SKILL.md` |
| 原型标注技能 | `/Users/bailey/.zcode/skills/原型标注/SKILL.md` |
| 跨项目参考：业务流程导航图 | `/Users/bailey/Desktop/xiaohei-workplace/auto-parts-rental/P3-R01-包装租赁管理后台原型/P3-R01-F01-业务流程导航图.html` |
| 跨项目参考：会前打磨三件套先例 | `/Users/bailey/Desktop/xiaohei-workplace/auto-parts-rental/P3-R04-演示场景覆盖梳理.md`、同项目 `agent-handoff/20260912-G24-决策落实与场景闭环检查.md`、`20260912-G25-会前原型修复包.md` |

## 五、工具链（本机 macOS 实测 2026-09-12）

- **python3**：`/Users/bailey/anaconda3/bin/python3`，**playwright-py 已安装可用**——一切校验/脚本一律用 Python
- **本机无 node/npx**：任何校验禁依赖 node（差异注意：包装租赁项目在 Win 主机有 node，其经验移植时按 Python 改写）
- **git**：项目根已纳管；Playwright 验证=file:// 直开（pathlib.as_uri）、每页新建 page、双监听 pageerror+console.error 防监听器累积
- Bash 中文路径不可靠 → 文件操作一律 python 内嵌中文绝对路径或内置工具

## 六、口径与纪律（铁律，违反=返工）

- **术语**：P1-R02 术语表为唯一术语源；C 类业务口径词（GP/LP、投决会、募投管退、清算注销、认缴/实缴、阶段①~⑫、放弃两级原因树、未投归档不可回流等）永不改；阶段1 历史层（P1-R01 及附件/A 系列记录/agent-handoff 旧文档/.research）保留原词按映射阅读
- **不动项**：D02 英文实体/字段名与枚举、HTML id/class、JS 变量、标注注入块（重注入只跑技能脚本）；99-归档 与 `_p3_backup*` 只进不动既有文件
- **工程纪律**：Bash 中文路径不可靠→文件操作一律 python 内嵌中文绝对路径或内置工具；批量替换=精确串+期望计数断言+幂等，计数不符跳过留档禁猜测改写；业务页面禁整文件重写；移动用 move 禁止覆盖同名；Playwright=file:// 直开（pathlib.as_uri）、每页新建 page、双监听 pageerror+console.error 防监听器累积
- **防并行覆盖**：动手前读原型说明版本行，高于任务文档所记即停并写失败清单——本项目发生过并行会话覆盖事故（P2-R01-A06 事件记录）；同一工作区同一时刻只允许一个 agent 写（mtime 互斥检测前置）
- **落档**：变更走 A 系列记录（格式沿用 A07~A12）+ 原型说明版本升级 + PRD 10.2 同步 + 收尾回写本基线与 `_索引.md`
