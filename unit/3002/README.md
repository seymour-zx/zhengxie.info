# 静态导航网站

一个简洁、高效、可自定义的纯静态导航站。基于 HTML5 + CSS3 + JavaScript 构建，零依赖、开箱即用，支持 GitHub Pages 一键部署。

![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub%20Pages-blue)
![HTML5](https://img.shields.io/badge/HTML5-orange)
![CSS3](https://img.shields.io/badge/CSS3-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-yellow)

## ✨ 功能特性

- 🎯 **分类导航** — 7 大分类、50+ 常用网站，图标化展示
- 🔍 **多搜索引擎** — Bing / Google / 百度 / DuckDuckGo / GitHub，一键切换
- 🌓 **深色 / 浅色主题** — 一键切换，自动跟随系统偏好，刷新保留选择
- 📱 **响应式布局** — 完美适配桌面 / 平板 / 手机
- ⚡ **纯静态** — 无后端、无构建工具，直接打开即用
- 🔧 **集中配置** — 所有导航链接、搜索引擎、第三方 ID 统一在 `js/config.js` 管理
- 📊 **百度统计** — 预留接入位，填入 ID 即可启用
- 💰 **Google AdSense** — 预留顶部 / 底部广告位，填入 ID 自动生效

## 📁 项目结构

```
nav-site/
├── index.html          # 主页面
├── css/
│   └── style.css       # 样式表（含深浅主题 + 响应式）
├── js/
│   ├── config.js       # 集中配置文件（导航数据 / 搜索引擎 / 统计 / 广告）
│   └── app.js          # 主逻辑（主题切换 / 搜索 / 渲染 / 注入）
├── assets/
│   └── favicon.svg     # 站点图标
├── CNAME               # GitHub Pages 自定义域名（按需修改）
└── README.md           # 本文档
```

## 🚀 快速开始

### 本地预览

直接用浏览器打开 `index.html` 即可查看效果。

推荐用本地服务器预览（避免某些浏览器的跨域限制）：

```bash
# 方式一：Python
python3 -m http.server 8080

# 方式二：Node.js
npx serve .
```

然后访问 `http://localhost:8080`。

---

## 📦 部署到 GitHub Pages

### 第一步：创建 GitHub 仓库

1. 登录 [GitHub](https://github.com)，点击右上角 **New repository**
2. 仓库名建议：`your-username.github.io`（用户主页站点）或任意名称（项目站点）
3. 选择 **Public**，点击 **Create repository**

### 第二步：上传代码

```bash
# 克隆你的仓库
git clone https://github.com/your-username/your-repo.git
cd your-repo

# 将本项目所有文件复制进去（不含本 README 所在的外层目录）
# 例如：将 index.html、css/、js/、assets/、CNAME 复制到仓库根目录

# 提交并推送
git add .
git commit -m "init: 导航站初始化"
git push -u origin main
```

### 第三步：启用 GitHub Pages

1. 进入仓库页面 → 点击顶部 **Settings**
2. 左侧菜单找到 **Pages**
3. **Source** 选择 `Deploy from a branch`
4. **Branch** 选择 `main` 分支，目录选择 `/ (root)`，点击 **Save**
5. 等待 1~2 分钟，页面上方会显示部署成功的链接
   - 用户主页站点：`https://your-username.github.io`
   - 项目站点：`https://your-username.github.io/your-repo/`

> 💡 **提示**：如果使用项目站点（非 `username.github.io` 仓库），需要注意资源路径问题。本项目使用相对路径，直接部署即可正常使用。

---

## 🌐 阿里云域名解析到 GitHub Pages

### 准备工作

- 已在阿里云购买域名（例如 `example.com`）
- 已完成 GitHub Pages 部署（上一步）

### 方案一：顶级域名（如 example.com）

#### 1. 获取 GitHub Pages 的 IP 地址

GitHub Pages 的 A 记录 IP（2024 年最新，共 4 个）：

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

> 最新 IP 以 [GitHub 官方文档](https://docs.github.com/cn/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) 为准。

#### 2. 在阿里云配置 DNS 解析

1. 登录 [阿里云控制台](https://dns.console.aliyun.com/) → 进入 **云解析 DNS**
2. 找到你的域名，点击 **解析设置**
3. 点击 **添加记录**，添加以下 4 条 **A 记录**：

   | 记录类型 | 主机记录 | 记录值 | TTL |
   |---------|---------|--------|-----|
   | A       | @       | 185.199.108.153 | 10 分钟 |
   | A       | @       | 185.199.109.153 | 10 分钟 |
   | A       | @       | 185.199.110.153 | 10 分钟 |
   | A       | @       | 185.199.111.153 | 10 分钟 |

4. （可选）再添加一条 **CNAME 记录** 让 `www` 子域名也能访问：

   | 记录类型 | 主机记录 | 记录值 | TTL |
   |---------|---------|--------|-----|
   | CNAME   | www     | your-username.github.io | 10 分钟 |

#### 3. 在 GitHub Pages 中配置自定义域名

1. 进入仓库 → **Settings** → **Pages**
2. 在 **Custom domain** 中填入你的域名（如 `example.com`），点击 **Save**
3. GitHub 会自动进行 DNS 检查，通过后状态显示为 ✅
4. 勾选 **Enforce HTTPS**，启用 HTTPS（DNS 生效后才可勾选）

#### 4. 修改项目中的 CNAME 文件

将项目根目录下 `CNAME` 文件的内容改为你的域名：

```
example.com
```

然后提交并推送到 GitHub。

### 方案二：子域名（如 nav.example.com）

如果使用子域名，配置更简单，用 **CNAME 记录**即可：

#### 1. 阿里云 DNS 配置

| 记录类型 | 主机记录 | 记录值 | TTL |
|---------|---------|--------|-----|
| CNAME   | nav     | your-username.github.io | 10 分钟 |

#### 2. GitHub Pages 配置

在 **Custom domain** 中填入 `nav.example.com`，其余步骤同上。

#### 3. 修改 CNAME 文件

```
nav.example.com
```

### 验证 DNS 生效

```bash
# 检查 A 记录
dig example.com +noall +answer

# 检查 CNAME 记录
dig www.example.com +noall +answer
```

DNS 生效通常需要几分钟到几小时不等，全球完全生效最多 48 小时。

---

## 📊 百度统计接入

### 第一步：获取百度统计 ID

1. 登录 [百度统计](https://tongji.baidu.com/)
2. 点击 **管理** → **新增网站**
3. 填写你的网站域名和名称，完成添加
4. 在 **代码获取** 页面，找到类似这样的代码：

   ```js
   hm.src = "https://hm.baidu.com/hm.js?xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
   ```

5. `?` 后面的那串字符（`xxxxxxxx...`）就是你的**统计 ID**，复制备用

### 第二步：在配置中启用

打开 `js/config.js`，找到 `baiduAnalytics` 部分：

```js
baiduAnalytics: {
  enabled: true,           // 改为 true
  id: "你的百度统计ID",     // 填入上一步复制的 ID
},
```

保存后刷新页面，百度统计脚本将自动注入。通常 20 分钟左右可在百度统计后台看到数据。

---

## 💰 Google AdSense 接入

### 第一步：申请 AdSense 账号

1. 访问 [Google AdSense](https://www.google.com/adsense/) 注册账号
2. 填入你的网站 URL 和联系信息
3. Google 会审核你的网站，通常 1~3 天

### 第二步：获取广告代码

审核通过后：

1. 登录 AdSense 后台 → **广告** → **按广告单元**
2. 点击 **新建广告单元**，选择 **展示广告**
3. 命名广告位（如 "导航站顶部"），选择尺寸（推荐 **自适应**）
4. 点击 **创建**，获得你的 **客户端 ID**（`ca-pub-xxxxxxxxxxxxxxxx`）和 **广告位 ID**（一串数字）

### 第三步：在配置中启用

打开 `js/config.js`，找到 `googleAdsense` 部分：

```js
googleAdsense: {
  enabled: true,                                    // 改为 true
  client: "ca-pub-XXXXXXXXXXXXXXXX",                // 替换为你的客户端 ID
  slots: {
    top: "1234567890",     // 顶部广告位 ID
    bottom: "0987654321",  // 底部广告位 ID
  },
},
```

保存后刷新页面，广告将自动加载到顶部和底部的预留位置。

> ⚠️ **注意**：
> - 广告展示需要 Google 审核通过并有广告库存，新站点初期可能展示较少
> - 请确保遵守 Google AdSense 政策，不要点击自己的广告
> - 如需新增广告位，在 `index.html` 中添加新的占位 div 并在 `app.js` 中扩展注入逻辑

---

## ⚙️ 配置项速查表

所有配置集中在 `js/config.js` 中：

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `site.title` | 站点标题 | 导航站 · 一键直达 |
| `site.logoIcon` | Logo 图标（emoji） | ⚡ |
| `site.logoText` | Logo 文字 | 导航站 |
| `searchEngines[]` | 搜索引擎列表 | 5 个常用引擎 |
| `defaultSearchEngine` | 默认搜索引擎 ID | `bing` |
| `categories[]` | 导航分类与链接 | 7 大分类 50+ 站点 |
| `baiduAnalytics.enabled` | 是否启用百度统计 | `false` |
| `baiduAnalytics.id` | 百度统计 ID | 占位 |
| `googleAdsense.enabled` | 是否启用 AdSense | `false` |
| `googleAdsense.client` | AdSense 客户端 ID | 占位 |
| `googleAdsense.slots.top` | 顶部广告位 ID | 占位 |
| `googleAdsense.slots.bottom` | 底部广告位 ID | 占位 |

### 添加新的导航链接

在 `categories` 对应分类的 `items` 数组中添加：

```js
{ name: "站点名称", url: "https://example.com", icon: "🔗" },
```

### 添加新的分类

在 `categories` 数组中添加新的分类对象：

```js
{
  id: "category-id",
  name: "分类名称",
  icon: "📁",
  items: [
    // 链接列表
  ],
},
```

---

## 📝 自定义指南

### 修改主题配色

在 `css/style.css` 的 `:root` 中修改 CSS 变量即可：

```css
:root {
  --accent-color: #4f6ef7;   /* 主色调 */
  --accent-hover: #3b57d8;   /* 悬浮色 */
  /* ... */
}
```

深色主题的对应变量在 `[data-theme="dark"]` 中修改。

### 替换站点图标

将你的 favicon 放入 `assets/` 目录，然后在 `index.html` 中修改路径：

```html
<link rel="icon" type="image/svg+xml" href="assets/your-icon.svg" />
```

---

## 📄 许可证

MIT License — 可自由使用、修改、分发。

---

## 🤝 贡献

欢迎提交 Issue 和 PR！

---

**享受你的专属导航站 🎉**
