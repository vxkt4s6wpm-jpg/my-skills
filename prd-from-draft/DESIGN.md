# UI设计规范文档
## 一、设计概述 Overview
**本规范只描述 `prototype-template.html` 骨架实际提供的东西**——色值、圆角、间距、图标一律以骨架为准；文档与骨架不一致时以骨架为准，并用 `check-consistency.py` 校验。

视觉基线为两个真实系统：`example-h5-app`（示例 H5 应用，亮色 + 青品牌层）与 `example-admin-web`（示例 Arco 后台，Arco Design）。**外壳决定几何形态，token 决定颜色**——同一套 token 下，H5 外壳（`.phone`）自动切换为 App 几何（12–14px 圆角、渐变按钮、柔和投影），Web 外壳（`.web-layout`）自动切换为 Arco 后台几何（2/4/8px 圆角、无边框扁平卡片、实色主按钮、1180px 最小宽度）。详见 5.8 / 5.9。

## 二、色彩系统 Colors
整套规范基于 Semi Design 完整 CSS 变量体系构建，**仅实现亮色一套**（原型阶段不产出暗色主题，也不做主题切换）。**开发编码禁止直接写死十六进制色值**，统一调用预设CSS变量，保障后续换肤时只改 token 不动标记。

### 2.1 语义化功能色（亮色）
| 语义变量 | 使用场景 | 色值 |
| ---- | ---- | ---- |
| `var(--semi-color-primary)` 主色 | 核心操作按钮、激活状态、关键交互元素 | #165DFF |
| `var(--semi-color-secondary)` 辅助色 | 次要操作、二级高亮标识（品牌青） | #1EC8C0 |
| `var(--semi-color-tertiary)` 三级中性色 | 三级操作、常规中性图标 | #86909C |
| `var(--semi-color-success)` 成功色 | 成功提示、正常运行状态、安全操作 | #00B42A |
| `var(--semi-color-warning)` 警告色 | 预警状态、风险提示、待处理告警 | #FF7D00 |
| `var(--semi-color-danger)` 危险色 | 故障报错、删除/高危操作、停机告警 | #F53F3F |
| `var(--semi-color-info)` 信息色 | 普通提示、中性反馈，与主色同色系 | #165DFF |

**扩展语义色**（仅用于标签的**分类**区分，不得用于状态反馈）：

| 变量名 | 使用场景 | 色值 |
| ---- | ---- | ---- |
| `var(--semi-color-purple)` 紫 | 标签分类：业绩调整、已调整 | #722ED1 |
| `var(--semi-color-cyan)` 青 | 标签分类：税银采集、数据类 | #0FC6C2 |
| `var(--semi-color-orangered)` 橙红 | 长等待类状态：待确认到账、等待执行 | #F77234 |
| `var(--semi-color-{语义}-weak)` 弱色底 | 标签、提示条底色（透明度 0.10~0.12） | 同名主色 10% 透明度 |

> 状态语义（成功/警告/危险）与分类语义（紫/青）不可互换：**状态用语义色，分类用扩展色**，避免「紫色代表失败」这类歧义。

### 2.2 页面背景与容器面层
| 变量名 | 层级用途 | 色值 |
| ---- | ---- | ---- |
| `var(--semi-color-bg-0)` 页面底层背景 | 页面最底层底色（Web 端，取自 cf_advisory 的 `body` 底色） | #F2F3F5 |
| `var(--semi-color-bg-1)` 基础容器层 | 卡片、基础内容容器、表格表头 | #FFFFFF |
| `var(--semi-color-bg-2)` 浮层弹窗容器 | 弹窗、气泡下拉、顶层浮层 | #FFFFFF |
| `var(--semi-color-fill-0)` 默认填充 | 输入框、组件默认底色 | rgba(29,33,41,0.05) |
| `var(--semi-color-fill-1)` hover填充 | 组件悬浮底色 | rgba(29,33,41,0.09) |
| `var(--semi-color-fill-2)` active填充 | 点击/选中按压底色 | rgba(29,33,41,0.13) |

### 2.3 文字与边框系统
| 变量名 | 使用场景 | 色值 |
| ---- | ---- | ---- |
| `var(--semi-color-text-0)` 一级文字 | 标题、核心正文、关键字段 | #1D2129 |
| `var(--semi-color-text-1)` 二级文字 | 描述文本、次要参数、标签说明 | #4E5969 |
| `var(--semi-color-text-2)` 三级文字 | 占位符、辅助备注、次要图标文字 | #86909C |
| `var(--semi-color-text-3)` 四级文字 | 禁用文字、空态图标 | #C9CDD4 |
| `var(--semi-color-border)` 分割边框 | 组件分割线、容器默认边框 | #E5E6EB |
| `var(--semi-color-disabled-border)` 禁用边框 | 禁用态控件的边框（§6.3） | #E5E6EB |

> H5 外壳（`.phone`）内一级/三级文字自动改用 `--brand-text`（#0D1B2A）与 `--brand-muted`（#5A6D86），比 Web 端偏冷，见 2.6。

### 2.4 AI 主题色（预留，骨架未内置）
Semi Design 定义了四个 AI 能力标识变量：`--semi-color-ai-general`（蓝紫粉渐变强调色）、`--semi-color-ai-purple`（`rgba(166,71,255)`）、`--semi-color-ai-background-top` / `-bottom`（区域遮罩梯度）。

**骨架 `:root` 里没有这四个**。需要时按 §2.1 的格式先加进骨架，再在原型里引用——不要直接写十六进制。

### 2.5 数据可视化色谱（预留，骨架未内置）
Semi Design 内置 20 套数据色 `var(--semi-color-data-0)` ~ `--semi-color-data-19`，用于多系列图表区分。

**骨架 `:root` 里没有这一组**。图表用色优先复用 §2.1 的语义色（骨架现有图表就是这么做的）；确实需要 20 色区分度时，再把 data 色加进骨架。

### 2.6 品牌层 Brand Tokens（H5 端主导）

品牌基线来自 `example-h5-app`：**青色承载科技感，蓝青渐变承载行动引导**。H5 整体走亮色——深色只用于文字，不作为底色，系统内不存在深色品牌底。品牌色不参与状态语义，仅用于主按钮、装饰线、Logo 底等品牌表达位。

| 变量 | 用途 | 色值 |
| ---- | ---- | ---- |
| `--brand-cyan` | 品牌青，聚焦态、强调 | #1EC8C0 |
| `--brand-text` | H5 正文色（比 Web 的 text-0 偏冷） | #0D1B2A |
| `--brand-muted` | H5 次级文字色（比 Web 的 text-2 偏冷） | #5A6D86 |
| `--brand-on-cyan` | 青色渐变上的正文色 | #041018 |

**渐变变量**（禁止手写渐变，统一取用）：

| 变量 | 效果 | 使用场景 |
| ---- | ---- | ---- |
| `--brand-grad-cta` | `140deg, #15D5FF → #0578FF` | H5 唯一主按钮渐变：表单提交、流程「下一步」、首页开始、FAB、登录按钮 |
| `--brand-grad-cta-active` | `140deg, #0FB3DB → #045FD4` | 主按钮按下态（比 cta 加深） |
| `--brand-grad-cyan` | `135deg, #0FC4B8 → #1EC8C0 40% → #3D8BFD` | Logo 标、头像底、次要 CTA |
| `--brand-grad-line` | `90deg, transparent → #1EC8C0 → #3D8BFD → transparent` | 卡片顶部装饰线 |
| `--brand-page` | `180deg, #E6EEF7 → #EEF2F7 45% → #E8EEF5` | H5 页面底色（渐变页） |

> H5 只有**一套**主按钮：蓝青渐变。`.btn-primary` 在 `.phone` 作用域内自动呈现它，强引导位也可显式写 `.btn-cta`，两者同款。不要再引入第二套视觉权重相当的渐变主按钮。

> 品牌渐变是**点缀**，不是主色：一屏内渐变面积不超过主按钮 + 一条装饰线。大面积铺渐变会让信息层级失焦。

## 三、文字排版规范 Typography
### 3.1 全局字体栈（全页面统一）
```css
"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif
```
所有标题、正文、标签、图标注释强制使用该字体栈，禁止混搭其他字体。

### 3.2 标题层级（字重600 粗体）
- H1：字号32px，行高44px，页面主标题、大屏看板标题
- H2：字号28px，行高40px，模块分区大标题
- H3：字号24px，行高32px，卡片头部标题
- H4：字号20px，行高28px，弹窗、子面板标题
- H5：字号18px，行高24px，表格分组小标题
- H6：字号16px，行高22px，表单分区小标题

### 3.3 正文与辅助文字（字重400 常规）
1. 主体正文：14px，行高20px，表单内容、列表文本、表格单元格
2. 标签/备注文字：12px，行高16px，表头注释、占位提示、小字说明

### 3.4 文字色彩层级强制规则
- 核心内容：`var(--semi-color-text-0)`
- 次要描述：`var(--semi-color-text-1)`
- 占位辅助文字：`var(--semi-color-text-2)`
- 禁用文本：`var(--semi-color-text-3)` / `var(--semi-color-disabled-text)`

## 四、层级阴影 Elevation
仅悬浮类组件使用柔和阴影区分页面深度；常规卡片、容器采用扁平设计，依靠边框与背景色区分层级，不添加阴影。
1. 浮层阴影（弹窗、下拉、消息提示）
```css
0 0 1px rgba(0, 0, 0, 0.3), 0 4px 14px rgba(0, 0, 0, 0.1)
```
2. 品牌 CTA 阴影（H5 `.btn-cta` 蓝青渐变主键）
```css
0 10px 24px rgba(22, 93, 255, 0.35)
```

## 五、通用组件规范 Components
### 5.1 圆角层级（严格遵循统一尺寸，禁止自定义圆角）

Web 端（`.web-layout`）使用 Arco 后台刻度：

| 变量 | 圆角尺寸 | 适用组件范围 |
| ---- | ---- | ---- |
| `var(--semi-border-radius-extra-small)` | 2px | 复选框内部标记、小型内置控件 |
| `var(--semi-border-radius-small)` | 2px | 按钮、输入框、标签、分页、提示条 |
| `var(--semi-border-radius-medium)` | 4px | 卡片、下拉菜单、菜单项、指标卡色块 |
| `var(--semi-border-radius-large)` | 8px | 弹窗、品牌标、登录页输入框 |
| `var(--semi-border-radius-extra-large)` | 24px | 登录卡片 |
| `var(--semi-border-radius-circle/full)` | 50%/9999px | 头像、状态徽标、胶囊型标签 |

H5 端（`.phone`）使用 App 刻度，不受上表影响（见 5.8）：

| 变量 | 圆角尺寸 | 适用组件范围 |
| ---- | ---- | ---- |
| `var(--brand-radius-card)` | 14px | H5 端卡片 |
| `var(--brand-radius-control)` | 12px | H5 端按钮、输入框、下拉、弹窗、提示 |
| `var(--brand-radius-tag)` | 2px | H5 端标签 |

### 5.2 基础业务组件规则
1. **按钮 Button**
    - 圆角：`var(--semi-border-radius-small)` 2px
    - 主按钮：填充 `var(--semi-color-primary)`；**一屏只允许一个主色实心按钮**，其余操作降为次要/文字按钮
    - 次要按钮：填充 `var(--semi-color-secondary)`
    - 默认/三级文字按钮：透明底色，悬浮显示 `var(--semi-color-fill-0)`
2. **下拉菜单 Menu & Dropdown**
    - 圆角 `var(--semi-border-radius-medium)`，挂载浮层阴影
3. **弹窗&卡片 Modal & Card**
    - 弹窗圆角 8px（`--semi-border-radius-large`），启用浮层阴影，背景使用 `var(--semi-color-bg-2)`
    - 常规业务卡片：4px 圆角、无边框、`--semi-shadow-card` 极轻投影；**不用边框区分层级**（与 Arco 后台一致）
4. **标签&角标 Tags & Badges**
    - 普通标签圆角2px；头像、状态角标全圆角
5. **选项卡 Tabs**
    - 线条型Tab激活底部2px主色边框；卡片型Tab顶部圆角3px
6. **数据表格 Table**
    - 表头背景：`var(--semi-color-table-head)`（#F7F8FA）
    - 行列分割线：`var(--semi-color-border)`
    - 行悬浮底色：`var(--semi-color-fill-0)`
    - 列宽策略：列宽按内容自适应；**列数多或字段长时整表横向滚动**（列宽下限参考：文本 160px、时间 170px、状态 100px、操作 200px）；列少时用 `.is-fit` 铺满容器并允许换行
    - 操作列：固定在最右、居中对齐、不随横向滚动消失；操作项按「详情 → 业务操作 → 危险操作」排列，危险操作用 `var(--semi-color-danger)`
    - 空数据时不渲染空表，改用空态（见 5.7）

### 5.3 表单输入组件 Form & Inputs
1. 控件尺寸规格
    - 小号：24px 高度（精简表格筛选栏）
    - 默认标准：32px 高度（全局通用）
    - 大号：40px 高度（弹窗大表单、大屏看板输入）
2. 默认样式
    - 圆角2px，透明边框，默认底色 `var(--semi-color-fill-0)`
3. 交互状态
    - 悬浮：底色切换 `var(--semi-color-fill-1)`
    - 聚焦：底色还原默认，1px主色聚焦边框 `var(--semi-color-focus-border)`
4. 必填项标识：红色星号 `var(--semi-color-danger)`

### 5.4 图标规范 Iconography
1. 默认基础尺寸：20px（`.icon`），可叠加 `.icon-sm`（16px）/ `.icon-lg`（24px）
2. **画布统一 48**：所有 symbol 一律 `viewBox="0 0 48 48"`（Arco 官方画布）。**symbol 内不写 `stroke-width` / `stroke-linecap` / `stroke-linejoin`**——写进去会盖掉 CSS，让 `.icon-sm` / `.icon-lg` / `.empty .icon` 失效
3. **线宽恒定 `stroke-width: 4`**：只写在 `.icon` 上，任何尺寸都不覆盖。这是 Arco 原生值（`strokeWidth` 默认 4，不随 `size` 变），所以 16px 图标呈现 1.33px、20px 呈现 1.67px，**小图标天然更细**；若按尺寸补偿，16px 会粗到 1.8px，比真实后台明显偏粗。**唯一例外**：`.empty .icon`（40px 空态大图）降到 `2.4`，装饰性元素不该抢视线
4. **线性图标规格**：`fill: none` + `stroke: currentColor` + `stroke-linecap: butt` + `stroke-linejoin: miter`（Arco 原生端点，**不要改成 `round`**，尖角会变钝）；填充态在 symbol 内用 `fill="currentColor" stroke="none"` 覆盖
5. 色彩：默认继承 `currentColor`；中性次要图标用 `var(--semi-color-text-2)`；未激活态用 `var(--semi-color-text-3)`
6. 引用写法：`<svg class="icon"><use href="#i-search"/></svg>`；按钮 / 标签 / 输入框内自动降为 16px。**只允许内联 symbol——禁止 emoji、图标字体、外链 CDN、手写裸 `<svg>`**
7. **来源与新增**：55 个全部取自 Arco 官方 outline（MIT 授权）。Arco 没有对应物时**换一个语义最近的 Arco 图标，不要自己画**。新增路径：先取 Arco 实源 → 画布归一到 48 → 线宽交给 `.icon` 的 4
8. **一图一义**：同一原型内同级功能条目各用各的图标——菜单项、指标卡、Tab、行操作之间不得重复。骨架 55 个不够就从 Arco 补（outline 有 250 个）。例外：关闭 `i-close`、下拉 `i-down`、Toast 与提示条的状态图标属全局组件约定，可跨页复用
9. **内容图标 ≠ 状态图标**：指标卡与功能入口的图标表达「这是什么」，不要拿 `i-check` `i-warn` `i-clock` 当内容图标——那是「好不好」的语义
10. **搬 Arco 图标要连元素级属性一起搬**：Arco 在元素上只放几何 + `fill`/`stroke`/`clip-rule`，一个都不能丢。丢了 `fill`/`stroke` 图标会变双线空心（`i-rise` `i-fall` `i-storage` `i-more` `i-wechat`），丢了 `clip-rule` 影响 `i-eye`

**图标清单（55 个，全部 Arco 源，无自绘）**：

| 分组 | 图标 ID | 用途 |
| ---- | ---- | ---- |
| 导航 | `i-dashboard` `i-order` `i-file` `i-book` `i-storage` | 工作台 / 订单 / 单据 / 申请 / 任务 |
| 导航 | `i-apps` `i-users` `i-chart` `i-settings` `i-safe` | 机构 / 用户 / 业绩 / 配置 / 审计 |
| 操作 | `i-search` `i-refresh` `i-plus` `i-edit` `i-download` | 查询 / 刷新 / 新增 / 编辑 / 导出 |
| 操作 | `i-fold` `i-unfold` `i-right` `i-down` `i-close` | 收起 / 展开 / 右箭头 / 下拉 / 关闭 |
| 操作 | `i-link` `i-bell` `i-delete` `i-filter` `i-upload` `i-more` | 跳转 / 通知 / 删除 / 筛选 / 上传 / 更多 |
| 状态 | `i-check` `i-check-plain` `i-warn` `i-info` `i-clock` | 成功 / 纯勾 / 警告 / 提示 / 处理中 |
| 状态 | `i-rise` `i-fall` `i-empty` | 上升 / 下降 / 空态 |
| 对象 | `i-user` `i-calendar` | 人员 / 日期 |
| App | `i-back` `i-chevron` `i-eye` `i-camera` `i-wechat` | 返回 / 箭头 / 查看 / 拍照 / 微信 |
| App | `i-home` `i-loan` `i-radio` `i-chip` | 首页 / 贷超凭证 / 单选 / 检验 |
| 金融 | `i-bank` | 转账（Arco `swap`） |
| 扩展 | `i-heart` `i-history` `i-compass` `i-idcard` | 心理情绪 / 过往回顾 / 方向探索 / 个人特质 |
| 扩展 | `i-question` `i-fire` `i-message` | 疑问卡点 / 投入热情 / 沟通对话 |
| 扩展 | `i-lock` `i-image` | 授权解锁 / 图片相册 |

> 55 个都是 Arco outline 的原样内联（画布归一到 48、线宽保留 4），Web 端还原 1:1。语义 ID ≠ Arco 原名的有 4 个：`i-radio`=`record`、`i-chip`=`experiment`、`i-bank`=`swap`、`i-loan`=`stamp`。**步骤节点不是图标**——`.step-dot` 用 CSS 画圆，仅「已完成」内嵌 `i-check-plain`。完整映射表在骨架文末注释里，**落回代码按表取用，不要凭语义重挑**：图标名相近不代表图形相同（Arco 的 `dashboard` 是仪表盘，不是四宫格）。

### 5.5 详情与流程类组件 Detail & Flow

1. **抽屉 Drawer**（右侧滑出，宽 640px，H5 不用）
   - 结构：`标题栏 / 内容区（可滚动）/ 底部操作栏`
   - 内容区用 `分组标题`（左侧 3px 主色竖条）切分「基础信息 / 处理进度 / 附件」等分组
   - 底部操作栏右对齐，主操作最右；关闭按钮始终存在
2. **描述列表 Descriptions**（详情字段展示）
   - 标签列固定 104px，底色 `var(--semi-color-fill-0)`；值列白底
   - 字段 ≤ 8 个用单列；> 8 个且字段短时用双列（`.desc-2`）
   - 行边框 `var(--semi-color-border)`，圆角 `var(--semi-border-radius-small)`
3. **时间轴 Timeline**（任务进度、操作日志）
   - 节点色即状态色：成功绿 / 失败红 / 进行中蓝 / 等待执行橙
   - 单条结构：`步骤名 + 状态标签 +（失败时「重试」链接）` / 详情文案 / `时间 · 来源`
   - 无日志时展示空态，不展示空白时间轴
4. **分页 Pagination**
   - 位于表格右下角，格式：`共 N 条 · 页码 · 每页条数`
   - 当前页主色实心，其余描边；每页条数选项 10/20/50/100

### 5.6 状态色映射表 Status Mapping

同一业务状态在全站必须使用同一颜色，禁止各页面自定：

| 状态语义 | 标签类 | 典型场景 |
| ---- | ---- | ---- |
| 已完成 / 已支付 / 已授权 / 启用 / 成功 | `tag-success` | 终态且正常 |
| 处理中 / 排队 / 支付中 / 进行中 | `tag-info` | 流程进行中 |
| 待处理 / 待付款 / 待复核 | `tag-warning` | 等待人工或对方动作 |
| 待确认到账 / 等待执行 / 长等待队列 | `tag-orangered` | 已受理但需外部条件推进 |
| 失败 / 执行失败 / 停用 / 已拒绝 | `tag-danger` | 异常终态，需人工介入 |
| 未开始 / 未就绪 / 已跳过 / 已取消 | `tag-gray` | 中性、无动作 |
| 采集类 / 数据类分类标签 | `tag-cyan` | 仅作分类 |
| 调整类 / 特殊分类标签 | `tag-purple` | 仅作分类 |

### 5.7 空态、加载态与错误态 States

| 状态 | 触发时机 | 表现 |
| ---- | ---- | ---- |
| 空态 | 列表查询无结果、详情无关联数据 | 居中图标（`i-empty`，40px，`--semi-color-text-3`）+ 一句说明文案，禁止只留白 |
| 加载态 | 数据请求中 | 卡片内用骨架屏（`.skeleton`，1.2s 呼吸动画），表格可用遮罩；禁止用「加载中…」纯文字 |
| 错误态 | 表单校验失败 | 输入框边框 `var(--semi-color-danger)` + 下方红色提示文案；提示文案要说清「怎么改」而非只说「不合法」 |

### 5.8 H5 外壳几何 App Geometry（`.phone` 作用域）

H5 外壳内的组件**自动**切换为 App 几何，无需在标记上加类；Web 外壳不受影响。差异如下：

| 元素 | Web 端（企业中性） | H5 端（App） |
| ---- | ---- | ---- |
| 导航栏 `.navbar` | 60px 顶栏 + 白底 | 44px 毛玻璃白底 + 底部 1px 分割线，标题 17px/500 居中，返回键 44px 命中区 |
| 页面底色 | `--semi-color-bg-0` 中性灰 #F2F3F5 | `--brand-page` 蓝灰渐变；首页 / 列表页加 `.is-flat` 改用 `--brand-home-bg` 平铺 #F7F8FA |
| 正文 / 次级文字 | `--semi-color-text-0` #1D2129 / `-text-2` #86909C | `--brand-text` #0D1B2A / `--brand-muted` #5A6D86（偏冷） |
| 卡片 `.card` | 20px 内边距、4px 圆角、无阴影 | 16px 内边距、14px 圆角（`--brand-radius-card`）、`--brand-surface` 底 + 柔和投影 |
| 主按钮 `.btn-primary` | 实色 `--semi-color-primary` | `--brand-grad-cta` 蓝青渐变 + 白字 + `--brand-shadow-cta`；悬浮不变色，按下切 `--brand-grad-cta-active` |
| 流程 CTA `.btn-cta` | — | 与 `.btn-primary` 同款蓝青渐变（首页开始 / 下一步 / FAB / 登录） |
| 控件高度 | 32px | 按钮 44px、输入框 42px |
| 输入框 | `--semi-color-fill-0` 底 | `--brand-field-bg` 底 + 1px 描边，聚焦青色描边 + 光环 |
| 标签 `.tag` | 2px 圆角、22px 高 | 2px 圆角、20px 高 |
| 底部栏 | — | `.phone-footer` 毛玻璃吸底；`.tabbar` 三标签栏，激活态主色 |

**H5 专用组件**：

1. **步骤条 `.steps`**：节点是 CSS 形状、不是图标——`.step-dot` 画 18px 圆点，三态由 `.step.is-current` / `.is-done` 控制底色描边，「已完成」内嵌 `i-check-plain`（12px）；连接线 `.step-line`（`.is-on` 表示已完成段）
2. **分组标题 `.group-title` / `.group-desc`**：H5 页面内小节标题（16px/700 + 12px 说明），与抽屉里的 `.section-title`（左侧 3px 竖条）区分，不要混用
3. **底部标签栏 `.tabbar`**：固定 3 个 `.tab-item`，激活态 `--semi-color-primary` + 600 字重；三个条目的图标从骨架取且**必须各用各的**（如 `i-home` `i-order` `i-user`）

### 5.9 Web 外壳几何 Admin Geometry（`.web-layout` 作用域）

Web 外壳对齐 `example-admin-web`（Arco 后台），与 H5 外壳的差异：

| 元素 | Web 端（Arco 后台） | H5 端（App） |
| ---- | ---- | ---- |
| 画布宽度 | `min-width: 1180px`，固定桌面宽度 | `max-width: 430px` 居中 |
| 侧边栏 | 220px / 折叠 64px，白底 + 右侧 1px 分割线 | 无 |
| 顶栏 | 60px，`rgba(255,255,255,.95)` 毛玻璃 + 底部分割线 | 44px 毛玻璃白底导航栏（与 Web 同族，仅高度与字号不同） |
| 卡片 `.card` | 4px 圆角、无边框、`--semi-shadow-card` | 14px 圆角、1px 发丝边框 + 柔和投影 |
| 主按钮 | 实色 `--semi-color-primary` | `--brand-grad-cta` 蓝青渐变 |
| 控件高度 | 32px | 按钮 44px / 输入框 42px |
| 表头 | `--semi-color-table-head`（#F7F8FA） | — |

**指标卡色块 `.metric-icon`**：36px 方块，图标取语义色、底色取对应 `-weak`，可选 `is-blue` / `is-cyan` / `is-orange` / `is-red` / `is-green` / `is-purple`。一屏指标卡不超过 4 个，颜色按语义取，禁止随机配色。

**登录页**（后台原型首屏，`prd-from-draft/prototype-template.html` 已内置）：

1. `.login-page`：满屏、内容右对齐（`padding-right: 120px`），背景用 `--brand-page` 渐变占位；有设计图时改内联 data URI，禁止外链
2. `.login-card`：452px 宽、40px 内边距、24px 圆角、`--semi-shadow-login` 投影
3. `.login-logo`：50px、8px 圆角；`.login-title` 24px/500
4. 输入框 46px 高、8px 圆角、`--semi-color-fill-1` 底；主按钮同样 46px 高

### 5.10 间距 Spacing

骨架只有五档：`--spacing-xs` 4px / `-sm` 8px / `-md` 12px / `-lg` 16px / `-xl` 24px。组件里不要手写其他数值。

## 六、交互状态规范 Interaction States
1. **悬浮 Hover**
    - 渐变主按钮：**不变色**——底色维持原渐变，只靠指针形态提示可点
    - 其余填充类组件：使用对应色系 `-hover` 衍生变量（如 `--semi-color-primary-hover`）
    - 透明/列表中性组件：背景填充 `var(--semi-color-fill-1)`
2. **点击激活 Active/Pressed**
    - 渐变主按钮：切 `--brand-grad-cta-active`（加深渐变）
    - 其余填充组件：色系 `-active` 衍生变量
    - 中性列表/文字按钮：背景填充 `var(--semi-color-fill-2)`
3. **禁用 Disabled**
    - 背景：`var(--semi-color-disabled-bg)`
    - 文字：`var(--semi-color-disabled-text)`
    - 边框：`var(--semi-color-disabled-border)`
    - 附加视觉：降低整体透明度，鼠标指针设置 `not-allowed`
4. **聚焦 Focus**
    - 输入类组件：底色还原 `var(--semi-color-bg-1)`，1px `var(--semi-color-focus-border)` 边框
    - 浮层可用 `Esc` 关闭；遮罩点击可关闭（破坏性确认弹窗除外，需 `mask-closable=false`）
5. **无权限 / 不可操作**
    - 行内操作不显示或置灰（`.is-disabled`），**不得点击后弹错误提示**——能在视觉上区分就不要等用户点了才拒绝
