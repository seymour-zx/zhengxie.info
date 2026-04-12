import pandas as pd
from jinja2 import Template
import json

# 读取配置表
site_df = pd.read_excel('站点配置表.xlsx', sheet_name='站点信息表')
category_df = pd.read_excel('站点配置表.xlsx', sheet_name='分类配置表')
global_config = dict(pd.read_excel('站点配置表.xlsx', sheet_name='全局配置表').values.tolist())

# 处理站点数据
sites = []
for _, row in site_df.iterrows():
    row = row.where(pd.notnull(row), None)
    site = {
        'id': row['站点ID'],
        'name': row['站点名称'],
        'logo': row['logo链接'],
        'desc': row['站点描述'],
        'category': row['所属分类'].split(',') if row['所属分类'] else [],
        'tags': row['标识标签'].split(',') if row['标识标签'] else [],
        'links': {
            '官网': row['官网链接'],
            '小红书': row['小红书链接'],
            '知乎': row['知乎链接'],
            '微信公众号': row['微信公众号链接'],
            '抖音': row['抖音链接'],
            'GitHub': row['GitHub链接'],
            '百度贴吧': row['百度贴吧链接'],
            '其他': row['其他平台链接']
        },
        'keywords': row['关键词标签'].split(',') if row['关键词标签'] else [],
        'is_new': row['是否最新收录'] == 1,
        'is_fav': row['是否默认收藏'] == 1
    }
    # 过滤空链接
    site['links'] = {k:v for k,v in site['links'].items() if v}
    sites.append(site)

# 处理分类数据
categories = []
for _, row in category_df.iterrows():
    row = row.where(pd.notnull(row), None)
    categories.append({
        'id': row['分类ID'],
        'name': row['分类名称'],
        'order': row['排序优先级'],
        'show': row['是否在顶部导航显示'] == 1
    })
categories.sort(key=lambda x: x['order'])

# 前端模板
html_template = Template('''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ global_config['网站标题'] }}</title>
    <meta name="description" content="{{ global_config['网站描述'] }}">
    <meta name="keywords" content="{{ global_config['网站关键词'] }}">
    <link rel="shortcut icon" href="{{ global_config['网站logo链接'] }}">
    <link rel="canonical" href="https://{{ global_config['网站域名'] }}">
    <meta property="og:title" content="{{ global_config['网站标题'] }}">
    <meta property="og:description" content="{{ global_config['网站描述'] }}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://{{ global_config['网站域名'] }}">
    {{ global_config['Google统计代码'] | safe if global_config.get('Google统计代码') else '' }}
    {{ global_config['百度统计代码'] | safe if global_config.get('百度统计代码') else '' }}
    <style>
        * {margin: 0;padding: 0;box-sizing: border-box;font-family: system-ui, -apple-system, sans-serif;}
        :root {--primary: #2563eb;--gray: #f3f4f6;--gray-dark: #6b7280;--border: #e5e7eb;--radius: 8px;}
        body {background-color: #f9fafb;color: #111827;padding-top: 180px;}
        /* 置顶区域 */
        .sticky-header {position: fixed;top: 0;left: 0;right: 0;background: white;box-shadow: 0 2px 10px rgba(0,0,0,0.05);z-index: 999;}
        /* 标题板块 */
        .header-top {display: flex;justify-content: space-between;align-items: center;padding: 12px 20px;border-bottom: 1px solid var(--border);max-width: 1200px;margin: 0 auto;width: 100%;}
        .logo-area {display: flex;align-items: center;gap: 10px;}
        .logo-icon {width: 36px;height: 36px;background: var(--primary);color: white;border-radius: var(--radius);display: flex;align-items: center;justify-content: center;font-size: 18px;font-weight: bold;overflow: hidden;}
        .logo-icon img {width: 100%;height: 100%;object-fit: cover;}
        .logo-text h1 {font-size: 20px;font-weight: 600;}
        .logo-text p {font-size: 12px;color: var(--gray-dark);}
        .submit-btn {width: 36px;height: 36px;border: 1px solid var(--border);border-radius: var(--radius);display: flex;align-items: center;justify-content: center;cursor: pointer;transition: 0.2s;}
        .submit-btn:hover {background: var(--gray);border-color: var(--primary);}
        /* 搜索板块 */
        .search-area {padding: 12px 20px;border-bottom: 1px solid var(--border);max-width: 1200px;margin: 0 auto;width: 100%;}
        .search-box {display: flex;gap: 8px;}
        .search-input {flex: 1;padding: 10px 14px;border: 1px solid var(--border);border-radius: var(--radius);font-size: 14px;outline: none;transition: 0.2s;}
        .search-input:focus {border-color: var(--primary);box-shadow: 0 0 0 3px rgba(37,99,235,0.1);}
        .search-btn {padding: 0 20px;background: var(--primary);color: white;border: none;border-radius: var(--radius);cursor: pointer;transition: 0.2s;}
        .search-btn:hover {background: #1d4ed8;}
        .search-tags {display: flex;flex-wrap: wrap;gap: 8px;margin-top: 10px;min-height: 28px;}
        .tag-item {display: flex;align-items: center;gap: 6px;padding: 4px 8px;background: var(--gray);border-radius: 6px;font-size: 13px;}
        .tag-close {cursor: pointer;color: var(--gray-dark);font-size: 16px;line-height: 1;}
        .tag-close:hover {color: #ef4444;}
        /* 分类板块 */
        .category-area {padding: 12px 20px;border-bottom: 1px solid var(--border);max-width: 1200px;margin: 0 auto;width: 100%;}
        .category-header {display: flex;justify-content: space-between;align-items: center;margin-bottom: 10px;}
        .category-title {display: flex;align-items: center;gap: 6px;font-size: 15px;font-weight: 500;}
        .category-count {font-size: 13px;color: var(--gray-dark);display: flex;align-items: center;gap: 8px;}
        .export-btn {cursor: pointer;color: var(--primary);transition: 0.2s;}
        .export-btn:hover {color: #1d4ed8;}
        .category-tabs {display: flex;gap: 8px;overflow-x: auto;padding-bottom: 2px;}
        .category-tab {padding: 6px 14px;border: 1px solid var(--border);border-radius: 20px;font-size: 14px;cursor: pointer;transition: 0.2s;white-space: nowrap;}
        .category-tab.active {background: var(--primary);color: white;border-color: var(--primary);}
        .category-tab:hover {border-color: var(--primary);}
        /* 广告板块 */
        .ad-section {max-width: 1200px;margin: 20px auto;padding: 0 20px;}
        .ad-container {width: 100%;min-height: 100px;background: white;border-radius: var(--radius);border: 1px solid var(--border);padding: 10px;position: relative;}
        .ad-label {position: absolute;top: 10px;left: 10px;background: #f59e0b;color: white;padding: 2px 6px;border-radius: 4px;font-size: 12px;z-index: 10;}
        /* 轮播板块 */
        .carousel-section {max-width: 1200px;margin: 20px auto;padding: 0 20px;}
        .carousel {width: 100%;height: 200px;background: white;border-radius: var(--radius);border: 1px solid var(--border);display: flex;align-items: center;justify-content: center;color: var(--gray-dark);position: relative;overflow: hidden;}
        .carousel-item {width: 100%;height: 100%;position: absolute;top: 0;left: 0;opacity: 0;transition: 0.5s;display: flex;align-items: center;justify-content: center;}
        .carousel-item.active {opacity: 1;}
        /* 站点列表 */
        .site-list {max-width: 1200px;margin: 20px auto;padding: 0 20px;display: grid;grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));gap: 16px;}
        .site-card {background: white;border-radius: var(--radius);border: 1px solid var(--border);padding: 16px;transition: 0.2s;}
        .site-card:hover {box-shadow: 0 4px 12px rgba(0,0,0,0.05);}
        /* 卡片第一层 */
        .site-header {display: flex;gap: 12px;align-items: center;margin-bottom: 12px;min-height: 48px;overflow-x: auto;position: relative;scrollbar-width: none;}
        .site-header::-webkit-scrollbar {display: none;}
        .site-logo {width: 40px;height: 40px;border-radius: var(--radius);display: flex;align-items: center;justify-content: center;font-weight: bold;color: white;background: var(--primary);flex-shrink: 0;overflow: hidden;}
        .site-logo img {width: 100%;height: 100%;object-fit: cover;}
        .site-info {flex: 1;min-width: 0;}
        .site-name {font-weight: 600;font-size: 15px;white-space: nowrap;overflow: hidden;text-overflow: ellipsis;}
        .site-desc {font-size: 13px;color: var(--gray-dark);white-space: nowrap;overflow: hidden;text-overflow: ellipsis;margin-top: 2px;}
        .site-header:hover .scroll-arrow {opacity: 1;}
        .scroll-arrow {position: absolute;top: 50%;transform: translateY(-50%);background: rgba(255,255,255,0.9);width: 24px;height: 24px;border-radius: 50%;display: flex;align-items: center;justify-content: center;opacity: 0;transition: 0.2s;z-index: 2;cursor: pointer;}
        .scroll-arrow.left {left: 0;}
        .scroll-arrow.right {right: 0;}
        /* 卡片第二层 */
        .site-category {display: flex;gap: 6px;margin-bottom: 10px;min-height: 24px;overflow-x: auto;scrollbar-width: none;}
        .site-category::-webkit-scrollbar {display: none;}
        .cate-tag {padding: 3px 8px;background: var(--gray);border-radius: 4px;font-size: 12px;white-space: nowrap;}
        .tag-icon {font-size: 12px;margin-left: 4px;}
        /* 卡片第三层 */
        .site-links {display: flex;gap: 6px;margin-bottom: 10px;min-height: 24px;overflow-x: auto;scrollbar-width: none;}
        .site-links::-webkit-scrollbar {display: none;}
        .link-tag {padding: 3px 8px;border: 1px solid var(--border);border-radius: 4px;font-size: 12px;white-space: nowrap;cursor: pointer;transition: 0.2s;}
        .link-tag:hover {border-color: var(--primary);color: var(--primary);}
        /* 卡片第四层 */
        .site-keywords {display: flex;gap: 6px;min-height: 24px;overflow-x: auto;scrollbar-width: none;}
        .site-keywords::-webkit-scrollbar {display: none;}
        .keyword-tag {padding: 3px 8px;background: #eff6ff;color: var(--primary);border-radius: 4px;font-size: 12px;white-space: nowrap;cursor: pointer;transition: 0.2s;}
        .keyword-tag:hover {background: #dbeafe;}
        /* 附加板块 */
        .tools-section {max-width: 1200px;margin: 20px auto;padding: 20px;background: white;border-radius: var(--radius);border: 1px solid var(--border);display: flex;gap: 30px;flex-wrap: wrap;justify-content: space-around;}
        .tool-item {text-align: center;}
        .tool-value {font-size: 24px;font-weight: 600;margin-bottom: 4px;}
        .tool-label {font-size: 13px;color: var(--gray-dark);}
        /* 页脚 */
        footer {max-width: 1200px;margin: 40px auto;padding: 20px;text-align: center;color: var(--gray-dark);font-size: 13px;border-top: 1px solid var(--border);}
        .footer-links {display: flex;gap: 20px;justify-content: center;margin-bottom: 10px;flex-wrap: wrap;}
        .footer-links a {color: var(--gray-dark);text-decoration: none;}
        .footer-links a:hover {color: var(--primary);}
        /* 移动端适配 */
        @media (max-width: 768px) {
            body {padding-top: 200px;}
            .site-list {grid-template-columns: 1fr;}
            .header-top, .search-area, .category-area {padding: 10px 16px;}
        }
    </style>
</head>
<body>
    <div class="sticky-header">
        <!-- 标题板块 -->
        <div class="header-top">
            <div class="logo-area">
                <div class="logo-icon">
                    {% if global_config.get('网站logo链接') %}
                    <img src="{{ global_config['网站logo链接'] }}" alt="{{ global_config['网站名称'] }}" onerror="this.parentElement.innerHTML='{{ global_config['网站logo占位文字'] }}'">
                    {% else %}
                    {{ global_config['网站logo占位文字'] }}
                    {% endif %}
                </div>
                <div class="logo-text">
                    <h1>{{ global_config['网站名称'] }}</h1>
                    <p>{{ global_config['网站域名'] if global_config.get('网站域名') else '' }}</p>
                </div>
            </div>
            <div class="submit-btn" onclick="window.open('{{ global_config['收录提交WPS表单链接'] if global_config.get('收录提交WPS表单链接') else '#' }}', '_blank')">✍️</div>
        </div>
        <!-- 搜索板块 -->
        <div class="search-area">
            <div class="search-box">
                <input type="text" class="search-input" id="searchInput" placeholder="输入关键词搜索站点">
                <button class="search-btn" id="searchBtn">搜索</button>
            </div>
            <div class="search-tags" id="searchTags"></div>
        </div>
        <!-- 分类板块 -->
        <div class="category-area">
            <div class="category-header">
                <div class="category-title">
                    <span>🔍</span>
                    <span>网站分类</span>
                </div>
                <div class="category-count">
                    <span>当前筛选: <span id="siteCount">0</span> 个站点</span>
                    <span class="export-btn" onclick="exportExcel()">📥 导出</span>
                </div>
            </div>
            <div class="category-tabs" id="categoryTabs">
                {% for cate in categories %}
                {% if cate.show %}
                <div class="category-tab" data-cate="{{ cate.name }}">{{ cate.name }}</div>
                {% endif %}
                {% endfor %}
            </div>
        </div>
    </div>
    <!-- 广告板块 -->
    <div class="ad-section">
        {{ global_config['Google广告代码'] | safe if global_config.get('Google广告代码') else '' }}
    </div>
    <!-- 轮播板块 -->
    <div class="carousel-section">
        <div class="carousel" id="carousel">
            <div class="carousel-item active">轮播图1</div>
            <div class="carousel-item">轮播图2</div>
            <div class="carousel-item">轮播图3</div>
        </div>
    </div>
    <!-- 站点列表 -->
    <div class="site-list" id="siteList"></div>
    <!-- 附加板块 -->
    <div class="tools-section">
        <div class="tool-item">
            <div class="tool-value" id="currentTime"></div>
            <div class="tool-label">当前时间</div>
        </div>
        <div class="tool-item">
            <div class="tool-value" id="currentDate"></div>
            <div class="tool-label">当前日期</div>
        </div>
        <div class="tool-item">
            <div class="tool-value" id="weather">--℃</div>
            <div class="tool-label">本地天气</div>
        </div>
    </div>
    <!-- 页脚 -->
    <footer>
        <div class="footer-links">
            <a href="/">首页</a>
            <a href="/directory">目录</a>
            <a href="/about">关于我们</a>
            <a href="/privacy">隐私政策</a>
        </div>
        <p>{{ global_config['页脚版权信息'] | safe }}</p>
    </footer>
    <script>
        const siteData = {{ sites | safe }};
        let activeCate = '全部';
        let activeKeywords = [];

        // 渲染站点
        function renderSites() {
            const filtered = siteData.filter(site => {
                // 分类筛选
                if (activeCate !== '全部' && !site.category.includes(activeCate)) return false;
                // 关键词筛选（且关系）
                if (activeKeywords.length > 0 && !activeKeywords.every(k => site.keywords.includes(k) || site.name.includes(k) || site.desc.includes(k))) return false;
                return true;
            });
            document.getElementById('siteCount').textContent = filtered.length;
            const list = document.getElementById('siteList');
            list.innerHTML = filtered.map(site => `
                <div class="site-card">
                    <div class="site-header" onwheel="handleScroll(event, this)">
                        <div class="scroll-arrow left" onclick="scrollLeft(this.parentElement)">←</div>
                        <div class="site-logo">
                            ${site.logo ? `<img src="${site.logo}" alt="${site.name}" onerror="this.parentElement.innerHTML='${site.name[0]}'">` : site.name[0]}
                        </div>
                        <div class="site-info">
                            <div class="site-name">${site.name}</div>
                            <div class="site-desc">${site.desc || ''}</div>
                        </div>
                        <div class="scroll-arrow right" onclick="scrollRight(this.parentElement)">→</div>
                    </div>
                    <div class="site-category">
                        ${site.category.map(c => `<span class="cate-tag">${c}</span>`).join('')}
                        ${site.tags.map(t => `<span class="cate-tag">${t}</span>`).join('')}
                        ${site.is_new ? '<span class="cate-tag" style="background:#fef2f2;color:#dc2626">新</span>' : ''}
                    </div>
                    <div class="site-links">
                        ${Object.entries(site.links).map(([name, url]) => `<span class="link-tag" onclick="window.open('${url}', '_blank')">${name}</span>`).join('')}
                    </div>
                    <div class="site-keywords">
                        ${site.keywords.map(k => `<span class="keyword-tag" onclick="addKeyword('${k}')">${k}</span>`).join('')}
                    </div>
                </div>
            `).join('');
        }

        // 横向滚动逻辑
        function handleScroll(e, el) {
            e.preventDefault();
            el.scrollLeft += e.deltaY;
        }
        function scrollLeft(el) {
            el.scrollBy({left: -100, behavior: 'smooth'});
        }
        function scrollRight(el) {
            el.scrollBy({left: 100, behavior: 'smooth'});
        }

        // 搜索逻辑
        document.getElementById('searchBtn').addEventListener('click', () => {
            const val = document.getElementById('searchInput').value.trim();
            if (val && !activeKeywords.includes(val)) {
                addKeyword(val);
                document.getElementById('searchInput').value = '';
            }
        });
        document.getElementById('searchInput').addEventListener('keydown', e => {
            if (e.key === 'Enter') document.getElementById('searchBtn').click();
        });

        function addKeyword(key) {
            if (!activeKeywords.includes(key)) {
                activeKeywords.push(key);
                renderSearchTags();
                renderSites();
            }
        }

        function renderSearchTags() {
            const tagsEl = document.getElementById('searchTags');
            tagsEl.innerHTML = activeKeywords.map((k, i) => `
                <span class="tag-item">
                    ${k}
                    <span class="tag-close" onclick="removeKeyword(${i})">×</span>
                </span>
            `).join('');
        }

        function removeKeyword(index) {
            activeKeywords.splice(index, 1);
            renderSearchTags();
            renderSites();
        }

        // 分类切换
        document.querySelectorAll('.category-tab').forEach(tab => {
            tab.addEventListener('click', () => {
                document.querySelectorAll('.category-tab').forEach(t => t.classList.remove('active'));
                tab.classList.add('active');
                activeCate = tab.dataset.cate;
                renderSites();
            });
        });
        // 默认选中全部
        document.querySelector('.category-tab[data-cate="全部"]').classList.add('active');

        // 导出Excel逻辑
        function exportExcel() {
            window.open('https://kdocs.cn/l/your-excel-export-link', '_blank');
        }

        // 轮播逻辑
        let carouselIndex = 0;
        const carouselItems = document.querySelectorAll('.carousel-item');
        setInterval(() => {
            carouselItems.forEach(i => i.classList.remove('active'));
            carouselIndex = (carouselIndex + 1) % carouselItems.length;
            carouselItems[carouselIndex].classList.add('active');
        }, 3000);

        // 工具板块逻辑
        function updateTime() {
            const now = new Date();
            document.getElementById('currentTime').textContent = now.toLocaleTimeString('zh-CN');
            document.getElementById('currentDate').textContent = now.toLocaleDateString('zh-CN', {year:'numeric', month:'2-digit', day:'2-digit', weekday:'long'});
        }
        setInterval(updateTime, 1000);
        updateTime();

        // 初始化
        renderSites();
    </script>
</body>
</html>
''')

# 渲染HTML
html_content = html_template.render(
    global_config=global_config,
    categories=categories,
    sites=json.dumps(sites, ensure_ascii=False)
)

# 保存文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('✅ 站点生成完成，已生成index.html文件，直接打开即可预览')
print('📌 后续更新站点仅需要修改「站点配置表.xlsx」，重新运行本脚本即可')