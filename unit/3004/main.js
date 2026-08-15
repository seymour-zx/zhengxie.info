const siteData = [
  { category: "常用", name: "百度", url: "https://www.baidu.com", desc: "中文搜索入口，常用信息检索平台。", icon: "B" },
  { category: "常用", name: "微信", url: "https://weixin.qq.com", desc: "社交沟通与内容分享平台。", icon: "W" },
  { category: "学习", name: "知乎", url: "https://www.zhihu.com", desc: "知识问答与学习社区，内容广泛。", icon: "Z" },
  { category: "学习", name: "CSDN", url: "https://www.csdn.net", desc: "程序员技术社区、文章和教程。", icon: "C" },
  { category: "开发", name: "GitHub", url: "https://github.com", desc: "全球领先的代码托管与协作平台。", icon: "G" },
  { category: "开发", name: "MDN", url: "https://developer.mozilla.org/zh-CN/", desc: "前端开发文档与学习资源。", icon: "M" },
  { category: "开发", name: "Stack Overflow", url: "https://stackoverflow.com", desc: "全球编程问答社区，技术问题解决中心。", icon: "S" },
  { category: "工具", name: "Google 翻译", url: "https://translate.google.com", desc: "通用语言翻译与多语言互译工具。", icon: "T" },
  { category: "工具", name: "小红书", url: "https://www.xiaohongshu.com", desc: "生活方式分享与发现平台。", icon: "X" },
  { category: "工具", name: "Bilibili", url: "https://www.bilibili.com", desc: "视频社区，学习、娱乐与资讯平台。", icon: "B" },
  { category: "资讯", name: "36Kr", url: "https://www.36kr.com", desc: "科技行业资讯与创业动态。", icon: "3" },
  { category: "资讯", name: "澎湃新闻", url: "https://www.thepaper.cn", desc: "时政与社会热点新闻平台。", icon: "P" },
  { category: "设计", name: "Dribbble", url: "https://dribbble.com", desc: "全球设计灵感与作品展示平台。", icon: "D" },
  { category: "设计", name: "Behance", url: "https://www.behance.net", desc: "创意作品集合与设计灵感库。", icon: "B" },
  { category: "办公", name: "Notion", url: "https://www.notion.so", desc: "知识管理、笔记与团队协作工具。", icon: "N" },
  { category: "办公", name: "飞书", url: "https://www.feishu.cn", desc: "企业协作、办公与高效沟通平台。", icon: "F" }
];

const filterButtons = document.getElementById("filterButtons");
const navGrid = document.getElementById("navGrid");
const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");
const navLinks = document.querySelectorAll(".nav-link");

const categories = ["全部", ...new Set(siteData.map((item) => item.category))];
const sectionMap = {
  hot: ["常用", "资讯"],
  tools: ["工具", "办公"],
  community: ["学习", "开发", "设计"]
};

let activeFilter = "全部";

function syncNavState() {
  navLinks.forEach((button) => {
    const target = button.dataset.target;
    const shouldBeActive = target === "hot" && activeFilter === "全部";
    button.classList.toggle("active", shouldBeActive);
  });
}

function renderFilters() {
  filterButtons.innerHTML = categories
    .map(
      (category) => `
        <button
          class="filter-btn ${category === activeFilter ? "active" : ""}"
          type="button"
          data-category="${category}"
        >
          ${category}
        </button>
      `
    )
    .join("");
}

function getVisibleSites() {
  const keyword = searchInput.value.trim().toLowerCase();

  return siteData.filter((site) => {
    const matchesCategory = activeFilter === "全部" || site.category === activeFilter;
    const content = [site.name, site.url, site.desc, site.category].join(" ").toLowerCase();
    const matchesKeyword = !keyword || content.includes(keyword);
    return matchesCategory && matchesKeyword;
  });
}

function renderSiteCard(site) {
  return `
    <article class="site-card">
      <div class="site-top">
        <div class="site-icon">${site.icon}</div>
        <div class="site-title">
          <h3>${site.name}</h3>
          <small>${site.category}</small>
        </div>
      </div>
      <p>${site.desc}</p>
      <div class="site-meta">
        <span>官网</span>
        <span>${site.url.replace(/^https?:\/\//, "")}</span>
      </div>
      <a class="site-link" href="${site.url}" target="_blank" rel="noreferrer noopener">访问网站</a>
    </article>
  `;
}

function renderSites() {
  const visibleSites = getVisibleSites();

  if (!visibleSites.length) {
    navGrid.innerHTML = '<div class="empty-state">没有找到匹配的站点，请尝试更换关键词或筛选条件。</div>';
    return;
  }

  const renderedGroups = Object.entries(sectionMap)
    .map(([key, categoriesForGroup]) => {
      const groupSites = visibleSites.filter((site) => categoriesForGroup.includes(site.category));
      if (!groupSites.length) return "";

      const titleMap = {
        hot: "热门站点",
        tools: "实用工具",
        community: "学习社区"
      };

      return `
        <section id="${key}" class="group-section">
          <div class="group-header">
            <h3>${titleMap[key]}</h3>
            <span class="group-tag">${groupSites.length} 个站点</span>
          </div>
          <div class="group-grid">
            ${groupSites.map(renderSiteCard).join("")}
          </div>
        </section>
      `;
    })
    .join("");

  navGrid.innerHTML = renderedGroups || '<div class="empty-state">没有找到匹配的站点，请尝试更换关键词或筛选条件。</div>';
}

filterButtons.addEventListener("click", (event) => {
  const button = event.target.closest(".filter-btn");
  if (!button) return;

  activeFilter = button.dataset.category;
  renderFilters();
  syncNavState();
  renderSites();
});

navLinks.forEach((button) => {
  button.addEventListener("click", () => {
    const target = button.dataset.target;
    const section = document.getElementById(target);

    if (section) {
      section.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    if (target === "contact") {
      document.getElementById("contact")?.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  });
});

searchInput.addEventListener("input", renderSites);

searchButton.addEventListener("click", () => {
  const visibleSites = getVisibleSites();
  if (visibleSites[0]) {
    window.open(visibleSites[0].url, "_blank", "noopener,noreferrer");
  }
});

renderFilters();
renderSites();
