/**
 * ============================================================
 *  导航站集中配置文件
 *  所有可配置项集中在此处，修改后刷新页面即可生效
 * ============================================================
 */

const SITE_CONFIG = {
  /* ============================================================
      站点基本信息
     ============================================================ */
  site: {
    title: "导航站 · 一键直达",
    description: "简洁高效的导航网站，一键直达常用工具与资源",
    logoIcon: "⚡",
    logoText: "导航站",
  },

  /* ============================================================
      搜索引擎配置
      - 默认选中 default 对应的引擎
      - 用户可在页面上切换，选择会保存到 localStorage
     ============================================================ */
  searchEngines: [
    {
      id: "bing",
      name: "Bing",
      url: "https://www.bing.com/search?q=",
      icon: "🔍",
    },
    {
      id: "google",
      name: "Google",
      url: "https://www.google.com/search?q=",
      icon: "🌐",
    },
    {
      id: "baidu",
      name: "百度",
      url: "https://www.baidu.com/s?wd=",
      icon: "🐾",
    },
    {
      id: "duckduckgo",
      name: "DuckDuckGo",
      url: "https://duckduckgo.com/?q=",
      icon: "🦆",
    },
    {
      id: "github",
      name: "GitHub",
      url: "https://github.com/search?q=",
      icon: "🐙",
    },
  ],
  defaultSearchEngine: "bing",

  /* ============================================================
      导航分类与链接
      每个分类包含：
        - id:     唯一标识（英文）
        - name:   分类显示名称
        - icon:   分类图标（emoji）
        - items:  链接列表
          每个链接包含：
            - name: 站点名称
            - url:  站点链接
            - icon: 站点图标（emoji）
            - desc: 简短描述（可选，暂未展示）
     ============================================================ */
  categories: [
    {
      id: "search",
      name: "搜索引擎",
      icon: "🔍",
      items: [
        { name: "Google", url: "https://www.google.com", icon: "🌐" },
        { name: "Bing", url: "https://www.bing.com", icon: "🔍" },
        { name: "百度", url: "https://www.baidu.com", icon: "🐾" },
        { name: "DuckDuckGo", url: "https://duckduckgo.com", icon: "🦆" },
        { name: "知乎", url: "https://www.zhihu.com", icon: "💡" },
      ],
    },
    {
      id: "dev",
      name: "开发工具",
      icon: "💻",
      items: [
        { name: "GitHub", url: "https://github.com", icon: "🐙" },
        { name: "Stack Overflow", url: "https://stackoverflow.com", icon: "📚" },
        { name: "MDN", url: "https://developer.mozilla.org", icon: "📖" },
        { name: "CodePen", url: "https://codepen.io", icon: "✏️" },
        { name: "JS Bin", url: "https://jsbin.com", icon: "🧪" },
        { name: "Regex101", url: "https://regex101.com", icon: "🔤" },
        { name: "JSON 格式化", url: "https://jsonformatter.curiousconcept.com", icon: "📋" },
        { name: "Can I Use", url: "https://caniuse.com", icon: "✅" },
      ],
    },
    {
      id: "design",
      name: "设计资源",
      icon: "🎨",
      items: [
        { name: "Figma", url: "https://www.figma.com", icon: "🎨" },
        { name: "Dribbble", url: "https://dribbble.com", icon: "🏀" },
        { name: "Behance", url: "https://www.behance.net", icon: "🖼️" },
        { name: "Unsplash", url: "https://unsplash.com", icon: "📷" },
        { name: "Iconfont", url: "https://www.iconfont.cn", icon: "🎯" },
        { name: "Tinypng", url: "https://tinypng.com", icon: "🐼" },
        { name: "Color Hunt", url: "https://colorhunt.co", icon: "🌈" },
      ],
    },
    {
      id: "learning",
      name: "在线学习",
      icon: "📚",
      items: [
        { name: "B 站", url: "https://www.bilibili.com", icon: "📺" },
        { name: "慕课网", url: "https://www.imooc.com", icon: "🎓" },
        { name: "极客时间", url: "https://time.geekbang.org", icon: "⏰" },
        { name: "掘金", url: "https://juejin.cn", icon: "⛏️" },
        { name: "CSDN", url: "https://www.csdn.net", icon: "💡" },
        { name: "知乎专栏", url: "https://zhuanlan.zhihu.com", icon: "📝" },
        { name: "Coursera", url: "https://www.coursera.org", icon: "🎓" },
      ],
    },
    {
      id: "tools",
      name: "实用工具",
      icon: "🛠️",
      items: [
        { name: "百度翻译", url: "https://fanyi.baidu.com", icon: "🌍" },
        { name: "DeepL 翻译", url: "https://www.deepl.com/translator", icon: "🔄" },
        { name: "石墨文档", url: "https://shimo.im", icon: "📄" },
        { name: "腾讯文档", url: "https://docs.qq.com", icon: "📊" },
        { name: "WPS 云", url: "https://www.wps.cn", icon: "📝" },
        { name: "ProcessOn", url: "https://www.processon.com", icon: "📈" },
        { name: "二维码生成", url: "https://cli.im", icon: "📱" },
        { name: "站长工具", url: "https://tool.chinaz.com", icon: "🔧" },
      ],
    },
    {
      id: "social",
      name: "娱乐社交",
      icon: "🎮",
      items: [
        { name: "微博", url: "https://weibo.com", icon: "📢" },
        { name: "小红书", url: "https://www.xiaohongshu.com", icon: "📕" },
        { name: "抖音", url: "https://www.douyin.com", icon: "🎵" },
        { name: "快手", url: "https://www.kuaishou.com", icon: "🎬" },
        { name: "豆瓣", url: "https://www.douban.com", icon: "🎭" },
        { name: "知乎", url: "https://www.zhihu.com", icon: "💡" },
        { name: "虎扑", url: "https://www.hupu.com", icon: "🏀" },
      ],
    },
    {
      id: "office",
      name: "邮箱办公",
      icon: "📧",
      items: [
        { name: "Gmail", url: "https://mail.google.com", icon: "📬" },
        { name: "Outlook", url: "https://outlook.live.com", icon: "📩" },
        { name: "QQ 邮箱", url: "https://mail.qq.com", icon: "✉️" },
        { name: "163 邮箱", url: "https://mail.163.com", icon: "📨" },
        { name: "阿里云邮箱", url: "https://mail.aliyun.com", icon: "☁️" },
        { name: "飞书", url: "https://www.feishu.cn", icon: "🐦" },
        { name: "钉钉", url: "https://www.dingtalk.com", icon: "📌" },
      ],
    },
  ],

  /* ============================================================
      百度统计配置
      - enabled: 是否启用百度统计
      - id:      百度统计 ID（在 hm.baidu.com? 后面的一串字符）
      启用后将自动在页面中注入百度统计脚本
     ============================================================ */
  baiduAnalytics: {
    enabled: true,
    id: "70e38224e5ebd850150b00a19835a25f",
  },

  /* ============================================================
      Google AdSense 配置
      - enabled: 是否启用广告
      - client:  AdSense 发布商 ID（ca-pub-xxxxxxxxxxxxxxxx）
      - slots:   广告位配置
          top:    顶部广告位 ID
          bottom: 底部广告位 ID
      启用后将自动在对应位置注入 AdSense 广告脚本
     ============================================================ */
  googleAdsense: {
    enabled: true,
    client: "ca-pub-6434243103158481",
    slots: {
      top: "4856101005",
      bottom: "4856101005",
    },
  },
};

// 将配置挂载到全局，供 app.js 使用
window.SITE_CONFIG = SITE_CONFIG;
