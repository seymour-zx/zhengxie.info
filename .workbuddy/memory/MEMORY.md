# 项目长期约定（MEMORY.md）

> 硬规则；解释见宪法/契约/日志。≤3000字符，超限=记忆断裂。

## 世界秩序（最高）
- 造物主=用户；agent=创世神；新世界=miniworld→取代旧世界 zhengxie.com.cn
- 旧世界=素材库，禁止改进；边吸边删(D-17)：提取→提纯→决策→吸收→删

## 产品本质（不可偏离）
- 主题卡片陈列馆/百科索引，非导航站（旧世界被弃根因）
- 卡片=词条；可无链接（空行占位=信息）；链接行不限，xlsx 10 位预留
- 综合全品类；政协+民主党派=首页专题；绝不纯垂直
- 名称/slogan 永不改：正协导航+「让每一次寻找，都不止于找到」
- 做索引不做内容；切割防假冒官方
- 第三方声明条(D-18)：首次访问显示→关闭记localStorage戳→30天不显、超期重显；未关下次继续

## 五铁律
1 单一权威：宪法+DEC库，永不两处说法不同
2 完整记忆：先记日志再动手；无记录=无效动作
3 一步一步：每步造物主确认；不批量不越权
4 提纯取代：内容提炼自旧世界，最终完全取代
5 旧项目冻结（仅素材库）

## 公开分层（判据=URL可访问）
- 公开层(README/html/css/robots/sitemap/CNAME/ads/favicon)：仅公开内容
- 私有层 .workbuddy/：治理/记忆/契约，URL 404；内部治理一律入内

## 发布（GitHub Pages）
- 发布源=docs/（2026-09-14由根改docs，造物主在GitHub设置切换）
- docs/根：index/404/robots/sitemap/ads/favicon/CNAME + assets/(仅css/js/images/json) + pages/ + topics/ + articles/
- CNAME必须留docs/；README/.gitignore/xlsx/.build留仓库根（不发布）
- 源码数据=仓库根 xlsx/ + .build/（非publish/、非assets/；避免随Pages公开）
- 路径基准：REPO=dirname(HERE)、BASE=REPO/docs、XLSX=REPO/xlsx
- 相对路径按层级深度写(../assets、../../assets)，docs内拓扑不变

## 坐标保护（防泄漏第一）
- 公开层禁：GitHub用户名/仓库名/github.com用户路径/users.noreply/<用户>.github.io
- "GitHub Pages"仅作服务名可公开（2026-08-31裁定）；上线前坐标扫描零命中

## 记忆机制
- MEMORY.md ≤3000字符，超限立即瘦身；决策记录必含原因(DEC-007)
- agent=闹钟：循环任务到点提醒(cycle-tasks.md)；造物主回"做/跳过/取消"

## 命名要点
- 专题=topics；hub=/topics/；政务=/topics/gov/；搜索=/topics/search/；人大=renda(后期)
- 政务/官方类专题名必带第三方属性词(DEC-008)；纯工具/文化类不限
- 首页只放政协+民主党派；其他=子频道(D-03)

## 架构（D-16）
- 页面=片段拼装：pages.unified.xlsx控广告位(1,3式)/GA4/百度/搜索框/导语；空=零代码
- 统计/广告增删=改xlsx；境外留三件套，境内迁移时关GA4/AdSense
- ZX(被删组件≠zx_前缀)；zx_=正协拼音前缀，保留；后端+事件分析迁移时提醒
- 数据流：cards-pages/*.xlsx→merge_cards→unified→build；不改unified

## 结构铁律（build HTML与旧世界一致）
- 分类行category-nav__inner+ul.category-nav__list.track#category-bar+li>h2>button；logo双文字；fav文本span(★/☆)；scroll-btns 4状态
- 卡片=旧build_card：t1/t2/t3+media5形态(首字fallback)+tags按钮+links(link_attr+箭头)+fav key(首URL/标题#row_seq)；相邻type变化插grid-break分行
- 排序仅row_seq（2026-09-30修订，type不参与）；有意偏离旧世界先type分组
- 搜索框=hero__search/hero__engines/hero__searchrow/track+21 data-engine；footer=sun/moon+完整导航
- 新功能只新增元素，禁改结构；改动先呈报
- 随机漫步已于2026-09-28移除，勿再引用
- 无链接卡=空行占位(<div class="card__links"></div>)，不加提示文字

## 回归闸门（改main.js必跑）
- 每次改main.js必跑 node .build/qa-scroll-check.js（退出码0=过）：滚动按钮单点脆弱，一处运行时错误=全站JS死
- 改#consent-bar必跑 .build/qa-consent-check.js（playwright-core+本地8899服务）
- 双场景：现代smooth/老内核降级；stub用真实index.html卡片+覆盖池为空(广告卡0张)
- safeScrollTo(smooth→两参数降级→120ms未动再降级)；CSS禁scroll-behavior:smooth(冲突致失效)；滚动按钮不锁输入、位置由scroll事件同步
- 滑道触摸(T6/MIUI已修)：.track/.filter-tags__track/.card__tags/.card__links/.card__sources用touch-action:pan-x+overscroll-behavior:contain；html,body用overscroll-behavior:none；标题/描述为点按展开不在此列

## README铁律（改README必校契约06）
- 纯手工流(教手写HTML，禁xlsx/.py/.build)；零内部引用；目录树不列内部层；定位=综合全品类；不写已删功能；发布源写docs/

## Git纪律
- agent不执行任何git命令；init/commit/push由造物主执行

## 路线与现状
- 路线见宪法§四；进度：立宪✅分层✅身份✅2-9步✅→第10步取代上线(push+删壳)
- 独立小世界：可运行本体=仓库根 xlsx/+.build/+docs/assets/；.workbuddy=内部治理(剥离不留)
- DEC库：宪法§五(DEC-001~008)；产品决策(D/N)由contracts/承载
