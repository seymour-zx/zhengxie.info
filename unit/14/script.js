        // 站点数据 - 已补充5个新标签，每个站点7-8个标签
        const sitesData = [
            {
                id: 1,
                name: "正协导航",
                logo: "正协",
                logoUrl: "https://zhengxie.info/favicon.ico",
                description: "全网网站通讯录",
                category: "资讯媒体",
                isFavorite: true,
                isRecommended: true,
                tags: ["导航网站", "网站收录", "上网入口", "资源整合", "站点分享", "实用工具", "网址大全"],
                links: [
                    { name: "官网", url: "https://zhengxie.info" }
                ]
            },
            {
                id: 2,
                name: "WPS 灵犀",
                logo: "WPS",
                logoUrl: "",
                description: "WPS",
                category: "其他",
                isFavorite: false,
                isRecommended: false,
                tags: ["AI", "办公助手", "金山办公", "智能工具", "文档处理", "国产软件", "生产力"],
                links: [
                    { name: "官网", url: "https://365.kdocs.cn/3rd/lingxi/aioffice/chat/10830185741025407" }
                ]
            },
            {
                id: 3,
                name: "表单",
                logo: "表单",
                logoUrl: "",
                description: "123",
                category: "工具资源",
                isFavorite: false,
                isRecommended: false,
                tags: ["123", "在线表单", "数据收集", "问卷调查", "信息登记", "表单工具", "数据统计"],
                links: [
                    { name: "官网", url: "https://f.kdocs.cn/ksform/w/write/0VFr3AsF#routePromt" }
                ]
            },
            {
                id: 4,
                name: "WPS 灵犀",
                logo: "WPS",
                logoUrl: "",
                description: "AI办公助手，支持文档处理、智能写作",
                category: "工具资源",
                isFavorite: false,
                isRecommended: true,
                tags: ["AI工具", "办公", "免费", "智能写作", "文档编辑", "表格处理", "演示制作", "效率提升"],
                links: [
                    { name: "官网", url: "https://365.kdocs.cn/3rd/lingxi/aioffice/chat" }
                ]
            },
            {
                id: 5,
                name: "在线格式转换",
                logo: "格式",
                logoUrl: "",
                description: "支持超过300种文件格式的在线转换",
                category: "工具资源",
                isFavorite: false,
                isRecommended: false,
                tags: ["格式转换", "在线工具", "免费", "文件处理", "文档转换", "视频转换", "音频转换", "图片转换"],
                links: [
                    { name: "官网", url: "https://convertio.co/zh/" }
                ]
            },
            {
                id: 6,
                name: "TinyPNG",
                logo: "Tiny",
                logoUrl: "",
                description: "智能PNG和JPEG图片压缩工具",
                category: "工具资源",
                isFavorite: false,
                isRecommended: false,
                tags: ["图片处理", "在线工具", "免费", "图片压缩", "无损压缩", "Web优化", "设计工具", "批量处理"],
                links: [
                    { name: "官网", url: "https://tinypng.com/" }
                ]
            },
            {
                id: 7,
                name: "SmallPDF",
                logo: "PDF",
                logoUrl: "",
                description: "一站式PDF处理工具，支持压缩、转换、编辑",
                category: "工具资源",
                isFavorite: false,
                isRecommended: false,
                tags: ["PDF处理", "在线工具", "效率", "PDF编辑", "PDF转换", "PDF压缩", "文档工具", "办公辅助"],
                links: [
                    { name: "官网", url: "https://smallpdf.com/cn" }
                ]
            },
            {
                id: 8,
                name: "百度翻译",
                logo: "翻译",
                logoUrl: "",
                description: "支持200多种语言的在线翻译服务",
                category: "工具资源",
                isFavorite: false,
                isRecommended: false,
                tags: ["翻译工具", "免费", "在线", "多语言", "文本翻译", "文档翻译", "语音翻译", "学习辅助"],
                links: [
                    { name: "官网", url: "https://fanyi.baidu.com/" }
                ]
            },
            {
                id: 9,
                name: "二维码生成器",
                logo: "二维码",
                logoUrl: "",
                description: "免费在线二维码生成和识别工具",
                category: "工具资源",
                isFavorite: false,
                isRecommended: false,
                tags: ["二维码", "工具", "免费", "二维码生成", "二维码识别", "自定义二维码", "营销工具", "信息分享"],
                links: [
                    { name: "官网", url: "https://cli.im/" }
                ]
            }
        ];

        // 当前筛选状态
        let currentCategory = "all";
        let searchTags = []; // 存储所有搜索标签
        let filteredSites = [...sitesData]; // 存储当前筛选结果
        const allCategories = [...new Set(sitesData.map(site => site.category))];

        // 初始化页面
        function initPage() {
            renderCategories();
            renderSites();
        }

        // 更新结果计数
        function updateResultCount() {
            document.getElementById('resultCount').textContent = filteredSites.length;
        }

        // 渲染分类按钮
        function renderCategories() {
            const container = document.getElementById('categoryButtons');
            
            // 先添加「最新推荐」分类按钮
            const recommendedButton = document.createElement('button');
            recommendedButton.className = 'category-btn recommended';
            recommendedButton.textContent = '🔥 最新推荐';
            recommendedButton.dataset.category = 'recommended';
            recommendedButton.onclick = () => filterByCategory('recommended');
            container.appendChild(recommendedButton);
            
            // 再添加「我的收藏」分类按钮
            const favoriteButton = document.createElement('button');
            favoriteButton.className = 'category-btn favorite';
            favoriteButton.textContent = '⭐ 我的收藏';
            favoriteButton.dataset.category = 'favorite';
            favoriteButton.onclick = () => filterByCategory('favorite');
            container.appendChild(favoriteButton);
            
            // 最后添加其他分类按钮
            allCategories.forEach(category => {
                const button = document.createElement('button');
                button.className = 'category-btn';
                button.textContent = category;
                button.dataset.category = category;
                button.onclick = () => filterByCategory(category);
                container.appendChild(button);
            });
        }

        // 渲染搜索标签
        function renderSearchTags() {
            const container = document.getElementById('searchTags');
            container.innerHTML = searchTags.map((tag, index) => `
                <div class="search-tag">
                    ${tag}
                    <button class="tag-close" onclick="removeSearchTag(${index})">×</button>
                </div>
            `).join('');
        }

        // 处理搜索框回车键
        function handleSearchKeydown(event) {
            if (event.key === 'Enter') {
                addSearchTag();
            }
        }

        // 添加搜索标签
        function addSearchTag() {
            const input = document.getElementById('searchInput');
            const keyword = input.value.trim();
            
            if (!keyword) return;
            if (searchTags.includes(keyword)) {
                alert('该搜索标签已存在');
                input.value = '';
                return;
            }

            searchTags.push(keyword);
            input.value = '';
            renderSearchTags();
            renderSites();
        }

        // 移除搜索标签
        function removeSearchTag(index) {
            searchTags.splice(index, 1);
            renderSearchTags();
            renderSites();
        }

        // 渲染站点卡片
        function renderSites() {
            const container = document.getElementById('sitesGrid');
            filteredSites = sitesData.filter(site => {
                let matchCategory;
                if (currentCategory === 'recommended') {
                    // 最新推荐分类：只显示isRecommended为true的站点
                    matchCategory = site.isRecommended === true;
                } else if (currentCategory === 'favorite') {
                    // 我的收藏分类：只显示isFavorite为true的站点
                    matchCategory = site.isFavorite === true;
                } else {
                    // 普通分类：按原有分类匹配
                    matchCategory = currentCategory === "all" || site.category === currentCategory;
                }
                
                // 所有搜索标签必须同时满足（AND关系）
                const matchAllTags = searchTags.every(tag => {
                    const lowerTag = tag.toLowerCase();
                    return site.name.toLowerCase().includes(lowerTag) ||
                           site.description.toLowerCase().includes(lowerTag) ||
                           site.tags.some(t => t.toLowerCase().includes(lowerTag));
                });
                
                return matchCategory && matchAllTags;
            });

            updateResultCount();

            if (filteredSites.length === 0) {
                if (currentCategory === 'recommended') {
                    container.innerHTML = `
                        <div class="empty-state">
                            <h3>🔥 暂无最新推荐站点</h3>
                            <p>在提交模板中标记「最新推荐」为"是"，即可在这里展示精选网站</p>
                        </div>
                    `;
                } else if (currentCategory === 'favorite') {
                    container.innerHTML = `
                        <div class="empty-state">
                            <h3>❤️ 还没有收藏的站点</h3>
                            <p>在提交模板中标记「我的收藏」为"是"，即可在这里显示常用网站</p>
                        </div>
                    `;
                } else {
                    container.innerHTML = `
                        <div class="empty-state">
                            <h3>🔍 没有找到匹配的站点</h3>
                            <p>试试调整搜索关键词或筛选条件，或者点击上方按钮清空所有筛选</p>
                        </div>
                    `;
                }
                return;
            }

            container.innerHTML = filteredSites.map(site => `
                <div class="site-card">
                    <div class="site-header">
                        <div class="site-logo">
                            ${site.logoUrl ? `<img src="${site.logoUrl}" alt="${site.name} logo" loading="lazy">` : site.logo}
                        </div>
                        <div class="site-info">
                            <h3 class="site-name">
                                ${site.name} 
                                ${site.isRecommended ? '🔥' : ''}
                                ${site.isFavorite ? '⭐' : ''}
                            </h3>
                            <p class="site-desc" title="${site.description}">${site.description}</p>
                        </div>
                    </div>
                    <div class="visit-links">
                        ${site.links.map(link => 
                            `<a href="${link.url}" target="_blank" class="visit-link">${link.name}</a>`
                        ).join('')}
                    </div>
                    <div class="site-tags">
                        ${site.tags.map(tag => 
                            `<span class="tag" onclick="addTagToSearch('${tag}')">${tag}</span>`
                        ).join('')}
                    </div>
                </div>
            `).join('');
        }

        // 点击卡片标签添加到搜索
        function addTagToSearch(tag) {
            if (!searchTags.includes(tag)) {
                searchTags.push(tag);
                renderSearchTags();
                renderSites();
            }
        }

        // 按分类筛选
        function filterByCategory(category) {
            currentCategory = category;
            
            // 更新按钮状态
            document.querySelectorAll('.category-btn').forEach(btn => {
                btn.classList.toggle('active', btn.dataset.category === category);
            });
            
            renderSites();
        }

        // 清空所有筛选
        function clearAllFilters() {
            currentCategory = "all";
            searchTags = [];
            
            document.getElementById('searchInput').value = "";
            document.querySelectorAll('.category-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            
            renderSearchTags();
            renderSites();
        }

        // 导出当前筛选结果
        function exportFilteredSites() {
            if (filteredSites.length === 0) {
                alert("没有可导出的站点数据");
                return;
            }

            // 生成CSV内容
            const headers = ["网站名称", "网站描述", "所属分类", "最新推荐", "我的收藏", "标签", "访问链接"];
            const rows = filteredSites.map(site => {
                const links = site.links.map(link => `${link.name}: ${link.url}`).join("；");
                const tags = site.tags.join("，");
                return [
                    `"${site.name}"`,
                    `"${site.description}"`,
                    `"${site.category}"`,
                    `"${site.isRecommended ? '是' : '否'}"`,
                    `"${site.isFavorite ? '是' : '否'}"`,
                    `"${tags}"`,
                    `"${links}"`
                ];
            });

            const csvContent = [
                headers.join(","),
                ...rows.map(row => row.join(","))
            ].join("\n");

            // 创建下载链接
            const blob = new Blob(["\ufeff" + csvContent], { type: "text/csv;charset=utf-8;" });
            const url = URL.createObjectURL(blob);
            const link = document.createElement("a");
            link.href = url;
            
            // 生成文件名（包含筛选条件）
            let fileName = "正协导航站点导出";
            if (currentCategory !== "all") fileName += `_${currentCategory}`;
            if (searchTags.length > 0) fileName += `_${searchTags.join('_')}`;
            fileName += `_${new Date().toLocaleDateString()}.csv`;
            
            link.download = fileName;
            link.click();
            URL.revokeObjectURL(url);

            alert(`成功导出 ${filteredSites.length} 个站点数据`);
        }

        // 标签切换功能
        function switchTab(tabName) {
            // 移除所有标签的激活状态
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
            
            // 激活选中的标签
            document.querySelector(`.tab-btn:nth-child(${tabName === 'wps' ? 1 : 2})`).classList.add('active');
            document.getElementById(`${tabName}Tab`).classList.add('active');
        }

        // 提交模态框操作
        function openSubmitModal() {
            document.getElementById('submitModal').style.display = 'flex';
        }

        function closeSubmitModal() {
            document.getElementById('submitModal').style.display = 'none';
            // 重置iframe，清除用户已填写的内容
            const iframe = document.querySelector('.form-iframe');
            iframe.src = iframe.src;
            // 切换回默认标签
            switchTab('wps');
        }

        // 分享模态框操作
        function openShareModal() {
            document.getElementById('shareModal').style.display = 'flex';
            // 自动填充当前页面链接
            document.getElementById('shareLinkInput').value = window.location.href;
        }

        function closeShareModal() {
            document.getElementById('shareModal').style.display = 'none';
        }

        // 分享功能
        function shareToWechat() {
            alert("请截图保存二维码或复制链接，在微信中分享");
        }

        function shareToWeibo() {
            const url = encodeURIComponent(window.location.href);
            const title = encodeURIComponent("正协导航 - 全网优质网站通讯录，发现更多好用的新网站！");
            window.open(`https://service.weibo.com/share/share.php?url=${url}&title=${title}`, '_blank');
        }

        function shareToQQ() {
            const url = encodeURIComponent(window.location.href);
            const title = encodeURIComponent("正协导航 - 全网优质网站通讯录");
            window.open(`https://connect.qq.com/widget/shareqq/index.html?url=${url}&title=${title}`, '_blank');
        }

        function copyShareLink() {
            const input = document.getElementById('shareLinkInput');
            input.select();
            document.execCommand('copy');
            alert("链接已复制到剪贴板，快去分享给朋友吧！");
        }

        // 点击模态框外部关闭
        window.onclick = function(event) {
            const submitModal = document.getElementById('submitModal');
            const shareModal = document.getElementById('shareModal');
            
            if (event.target == submitModal) {
                closeSubmitModal();
            }
            if (event.target == shareModal) {
                closeShareModal();
            }
        }

        // 页面加载完成后初始化
        document.addEventListener('DOMContentLoaded', initPage);





// 轮播功能逻辑
const carouselWrapper = document.getElementById('carouselWrapper');
const carouselItems = document.querySelectorAll('.carousel-item');
const carouselPrev = document.getElementById('carouselPrev');
const carouselNext = document.getElementById('carouselNext');
const carouselDots = document.getElementById('carouselDots');
let currentIndex = 0;
let autoPlayTimer = null;
 
// 生成底部指示器
carouselItems.forEach((_, index) => {
    const dot = document.createElement('div');
    dot.className = `carousel-dot ${index === 0 ? 'active' : ''}`;
    dot.onclick = () => goToSlide(index);
    carouselDots.appendChild(dot);
});
const dots = document.querySelectorAll('.carousel-dot');
 
// 切换到指定轮播页
function goToSlide(index) {
    carouselItems[currentIndex].classList.remove('active');
    dots[currentIndex].classList.remove('active');
    currentIndex = index;
    if (currentIndex >= carouselItems.length) currentIndex = 0;
    if (currentIndex < 0) currentIndex = carouselItems.length - 1;
    carouselItems[currentIndex].classList.add('active');
    dots[currentIndex].classList.add('active');
}
 
// 前后切换
carouselPrev.onclick = () => goToSlide(currentIndex - 1);
carouselNext.onclick = () => goToSlide(currentIndex + 1);
 
// 自动轮播（间隔4秒，可自行修改时间）
function startAutoPlay() {
    autoPlayTimer = setInterval(() => goToSlide(currentIndex + 1), 4000);
}
startAutoPlay();
 
// 鼠标悬浮暂停轮播，离开继续
carouselWrapper.onmouseenter = () => clearInterval(autoPlayTimer);
carouselWrapper.onmouseleave = startAutoPlay;



