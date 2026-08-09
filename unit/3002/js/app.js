/**
 * ============================================================
 *  导航站主逻辑文件
 *  功能：
 *    1. 搜索引擎渲染、切换、搜索提交
 *    2. 导航分类与链接动态渲染
 *    3. 分类标签筛选 + 本地记忆
 *    4. 标签栏滚动渐变遮罩
 *    5. 百度统计自动注入（根据配置）
 *    6. Google AdSense 广告位自动注入（根据配置）
 * ============================================================ */

(function () {
  "use strict";

  const config = window.SITE_CONFIG;
  const STORAGE_KEY_ENGINE = "nav-search-engine";
  const STORAGE_KEY_CATEGORY = "nav-active-category";

  /* ============================================================
      1. 搜索功能
     ============================================================ */
  function initSearch() {
    const select = document.getElementById("search-engine");
    const input = document.getElementById("search-input");
    const btn = document.getElementById("search-btn");

    if (!select || !input || !btn) return;

    // 渲染搜索引擎选项
    const engines = config.searchEngines || [];
    const savedEngine = localStorage.getItem(STORAGE_KEY_ENGINE);
    const defaultEngine = savedEngine || config.defaultSearchEngine || engines[0]?.id;

    engines.forEach((engine) => {
      const option = document.createElement("option");
      option.value = engine.id;
      option.textContent = engine.icon ? `${engine.icon} ${engine.name}` : engine.name;
      if (engine.id === defaultEngine) {
        option.selected = true;
      }
      select.appendChild(option);
    });

    // 切换搜索引擎
    select.addEventListener("change", function () {
      localStorage.setItem(STORAGE_KEY_ENGINE, this.value);
      input.focus();
    });

    // 执行搜索
    function doSearch() {
      const keyword = input.value.trim();
      if (!keyword) {
        input.focus();
        return;
      }
      const engineId = select.value;
      const engine = engines.find((e) => e.id === engineId) || engines[0];
      if (engine && engine.url) {
        window.open(engine.url + encodeURIComponent(keyword), "_blank");
      }
    }

    btn.addEventListener("click", doSearch);
    input.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        doSearch();
      }
    });
  }

  /* ============================================================
      2. 导航分类与链接渲染
     ============================================================ */
  function renderNav() {
    const container = document.getElementById("nav-container");
    if (!container || !config.categories) return;

    config.categories.forEach((category) => {
      if (!category.items || category.items.length === 0) return;

      const section = document.createElement("section");
      section.className = "category-section";
      section.id = `category-${category.id}`;
      section.dataset.categoryId = category.id;

      // 分类标题
      const title = document.createElement("h2");
      title.className = "category-title";
      title.innerHTML = `
        <span class="category-icon">${category.icon || "📁"}</span>
        <span>${category.name}</span>
      `;
      section.appendChild(title);

      // 链接网格
      const grid = document.createElement("div");
      grid.className = "nav-grid";

      category.items.forEach((item) => {
        const card = document.createElement("a");
        card.className = "nav-card";
        card.href = item.url;
        card.target = "_blank";
        card.rel = "noopener noreferrer";
        card.title = item.desc || item.name;

        card.innerHTML = `
          <div class="nav-card-icon">${item.icon || "🔗"}</div>
          <span class="nav-card-name">${item.name}</span>
        `;

        grid.appendChild(card);
      });

      section.appendChild(grid);
      container.appendChild(section);
    });
  }

  /* ============================================================
      3. 分类标签筛选栏
     ============================================================ */
  function initCategoryTabs() {
    const tabsContainer = document.getElementById("category-tabs");
    if (!tabsContainer || !config.categories) return;

    // 「全部」标签
    const allTab = createTab("all", "全部", "⚜", true);
    tabsContainer.appendChild(allTab);

    // 各分类标签
    config.categories.forEach((category) => {
      const tab = createTab(category.id, category.name, category.icon, false);
      tabsContainer.appendChild(tab);
    });

    // 初始化滚动渐变遮罩
    initTabsFade();
  }

  function createTab(id, name, icon, isActive) {
    const tab = document.createElement("button");
    tab.className = "category-tab" + (isActive ? " active" : "");
    tab.dataset.categoryId = id;
    tab.innerHTML = `
      <span class="tab-icon">${icon || "📁"}</span>
      <span class="tab-name">${name}</span>
    `;
    tab.addEventListener("click", () => {
      switchCategory(id);
      // 点击后将选中标签滚动到可视区域中间
      tab.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
    });
    return tab;
  }

  function switchCategory(categoryId) {
    // 更新标签激活状态
    const tabs = document.querySelectorAll(".category-tab");
    tabs.forEach((tab) => {
      if (tab.dataset.categoryId === categoryId) {
        tab.classList.add("active");
      } else {
        tab.classList.remove("active");
      }
    });

    // 筛选显示对应分类
    const sections = document.querySelectorAll(".category-section");
    sections.forEach((section) => {
      if (categoryId === "all" || section.dataset.categoryId === categoryId) {
        section.style.display = "";
      } else {
        section.style.display = "none";
      }
    });

    // 保存用户选择
    localStorage.setItem(STORAGE_KEY_CATEGORY, categoryId);
  }

  /* ============================================================
      4. 标签栏滚动渐变遮罩
     ============================================================ */
  function initTabsFade() {
    const wrapper = document.querySelector(".category-tabs-wrapper");
    const fadeLeft = document.querySelector(".tabs-fade-left");
    const fadeRight = document.querySelector(".tabs-fade-right");

    if (!wrapper || !fadeLeft || !fadeRight) return;

    function updateFade() {
      const scrollLeft = wrapper.scrollLeft;
      const maxScroll = wrapper.scrollWidth - wrapper.clientWidth;

      // 左边遮罩：滚动 > 0 时显示
      fadeLeft.style.opacity = scrollLeft > 10 ? "1" : "0";

      // 右边遮罩：未滚到底时显示
      fadeRight.style.opacity = scrollLeft < maxScroll - 10 ? "1" : "0";
    }

    // 初始状态
    updateFade();

    // 滚动时更新
    wrapper.addEventListener("scroll", updateFade, { passive: true });

    // 窗口大小变化时重新计算
    window.addEventListener("resize", updateFade);
  }

  /* ============================================================
      5. 恢复上次选中的分类
     ============================================================ */
  function restoreActiveCategory() {
    const saved = localStorage.getItem(STORAGE_KEY_CATEGORY);
    if (saved && saved !== "all") {
      // 验证分类是否存在
      const exists = config.categories.some((c) => c.id === saved);
      if (exists) {
        switchCategory(saved);
      }
    }
  }

  /* ============================================================
      6. 百度统计注入
     ============================================================ */
  function injectBaiduAnalytics() {
    const baidu = config.baiduAnalytics;
    if (!baidu || !baidu.enabled || !baidu.id || baidu.id.indexOf("在此处") !== -1) {
      return;
    }

    window._hmt = window._hmt || [];
    const hm = document.createElement("script");
    hm.src = `https://hm.baidu.com/hm.js?${baidu.id}`;
    const s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(hm, s);
    console.log("[导航站] 百度统计已加载");
  }

  /* ============================================================
      7. Google AdSense 注入
     ============================================================ */
  function injectGoogleAdsense() {
    const ads = config.googleAdsense;
    if (!ads || !ads.enabled || !ads.client || ads.client.indexOf("XXXXXXXX") !== -1) {
      return;
    }

    // 加载 AdSense 脚本
    const script = document.createElement("script");
    script.src = `https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${ads.client}`;
    script.crossOrigin = "anonymous";
    script.async = true;
    document.head.appendChild(script);

    // 顶部广告位 — 广告嵌入大图卡片容器内
    if (ads.slots && ads.slots.top) {
      const topSlot = document.getElementById("ad-top");
      if (topSlot) {
        topSlot.classList.add("active");
        const adCard = topSlot.querySelector(".ad-card");
        if (adCard) {
          adCard.innerHTML = `
            <ins class="adsbygoogle"
                 style="display:block"
                 data-ad-client="${ads.client}"
                 data-ad-slot="${ads.slots.top}"
                 data-ad-format="auto"
                 data-full-width-responsive="true"></ins>
          `;
          adCard.style.borderStyle = "solid";
          adCard.style.minHeight = "auto";
          adCard.style.padding = "12px";
        }
        (window.adsbygoogle = window.adsbygoogle || []).push({});
      }
    }

    // 底部广告位 — 广告嵌入大图卡片容器内
    if (ads.slots && ads.slots.bottom) {
      const bottomSlot = document.getElementById("ad-bottom");
      if (bottomSlot) {
        bottomSlot.classList.add("active");
        const adCard = bottomSlot.querySelector(".ad-card");
        if (adCard) {
          adCard.innerHTML = `
            <ins class="adsbygoogle"
                 style="display:block"
                 data-ad-client="${ads.client}"
                 data-ad-slot="${ads.slots.bottom}"
                 data-ad-format="auto"
                 data-full-width-responsive="true"></ins>
          `;
          adCard.style.borderStyle = "solid";
          adCard.style.minHeight = "auto";
          adCard.style.padding = "12px";
        }
        (window.adsbygoogle = window.adsbygoogle || []).push({});
      }
    }

    console.log("[导航站] Google AdSense 已加载");
  }

  /* ============================================================
      8. 杂项：年份等
     ============================================================ */
  function initMisc() {
    const yearEl = document.getElementById("current-year");
    if (yearEl) {
      yearEl.textContent = new Date().getFullYear();
    }

    // 更新页面标题
    if (config.site && config.site.title) {
      document.title = config.site.title;
    }
  }

  /* ============================================================
      初始化入口
     ============================================================ */
  function init() {
    initSearch();
    renderNav();
    initCategoryTabs();
    restoreActiveCategory();
    injectBaiduAnalytics();
    injectGoogleAdsense();
    initMisc();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
