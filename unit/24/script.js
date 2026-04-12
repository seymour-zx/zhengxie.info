// 全局变量：当前激活的搜索标签
let activeSearchTags = [];

// 页面加载完成后初始化
window.addEventListener('load', () => {
    // 初始化logo生成
    initSiteLogos();
    // 初始化事件绑定
    initEvents();
    // 默认触发一级分类切换
    document.querySelector('.cate-tab.active').click();
})

// 生成站点首字logo
function initSiteLogos() {
    const gradients = [
        'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
        'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
        'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
        'linear-gradient(135deg, #fa709a 0%, #fee140 100%)'
    ];
    document.querySelectorAll('.site-card').forEach(card => {
        const logoWrap = card.querySelector('.site-logo');
        if (!logoWrap.querySelector('img')) {
            const siteName = card.querySelector('.site-name').textContent.trim();
            const firstChar = siteName.charAt(0);
            logoWrap.textContent = firstChar;
            logoWrap.style.background = gradients[Math.floor(Math.random() * gradients.length)];
        }
    })
}

// 初始化所有事件
function initEvents() {
    // 搜索按钮/回车事件
    document.getElementById('search-btn').addEventListener('click', addSearchTag);
    document.getElementById('search-input').addEventListener('keydown', e => {
        if (e.key === 'Enter') addSearchTag();
    });

    // 一级分类切换
    document.querySelectorAll('.cate-tab').forEach(tab => {
        tab.addEventListener('click', () => {
            document.querySelectorAll('.cate-tab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            const targetCate = tab.dataset.cate;
            if (targetCate === 'all') {
                document.querySelectorAll('.cate-content').forEach(content => {
                    content.style.display = 'block';
                    const level2AllTab = content.querySelector('.level2-tab[data-level2="all"]');
                    if (level2AllTab) level2AllTab.click();
                });
            } else {
                document.querySelectorAll('.cate-content').forEach(content => {
                    content.style.display = content.id === `${targetCate}-content` ? 'block' : 'none';
                });
                const firstLevel2Tab = document.querySelector(`#${targetCate}-content .level2-tab`);
                if (firstLevel2Tab) firstLevel2Tab.click();
            }
            globalFilterSites();
        });
    });

    // 二级分类切换
    document.addEventListener('click', e => {
        if (!e.target.classList.contains('level2-tab')) return;
        const tab = e.target;
        const targetLevel2 = tab.dataset.level2;
        const currentCate = tab.closest('[id$="-content"]');
        if (!currentCate) return;
        currentCate.querySelectorAll('.level2-tab').forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        if (targetLevel2 === 'all') {
            currentCate.querySelectorAll('.category-level2').forEach(el => el.style.display = 'block');
        } else {
            currentCate.querySelectorAll('.category-level2').forEach(el => {
                el.style.display = el.dataset.level2 === targetLevel2 ? 'block' : 'none';
            });
        }
        globalFilterSites();
    });

    // 站点搜索标签点击事件
    document.addEventListener('click', e => {
        if (e.target.classList.contains('search-tag-item')) {
            const tagText = e.target.textContent.trim();
            const searchInput = document.getElementById('search-input');
            searchInput.value = tagText;
            addSearchTag();
        }
    });

    // 横向滚动行滚轮控制
    const horizontalScrollContainers = document.querySelectorAll(
        '.site-name-scroll, .site-desc-scroll, .site-platforms, .site-search-tags'
    );
    horizontalScrollContainers.forEach(container => {
        container.addEventListener('wheel', e => {
            e.preventDefault();
            container.scrollLeft += e.deltaY > 0 ? 30 : -30;
        });
    })
}

// 添加搜索标签
function addSearchTag() {
    const input = document.getElementById('search-input');
    const keyword = input.value.trim().toLowerCase();
    if (!keyword || activeSearchTags.includes(keyword)) {
        input.value = '';
        return;
    }
    activeSearchTags.push(keyword);
    renderSearchTags();
    input.value = '';
    globalFilterSites();
}

// 渲染搜索标签
function renderSearchTags() {
    const tagsBar = document.getElementById('search-tags-bar');
    const tagsList = document.getElementById('tags-list');
    if (activeSearchTags.length === 0) {
        tagsBar.style.display = 'none';
        return;
    }
    tagsBar.style.display = 'flex';
    tagsList.innerHTML = '';
    activeSearchTags.forEach((tag, index) => {
        const tagEl = document.createElement('div');
        tagEl.className = 'search-tag';
        tagEl.innerHTML = `
            <span>${tag}</span>
            <span class="tag-close" data-index="${index}">×</span>
        `;
        tagsList.appendChild(tagEl);
    });
    document.querySelectorAll('.tag-close').forEach(closeBtn => {
        closeBtn.addEventListener('click', e => {
            const index = parseInt(e.target.dataset.index);
            activeSearchTags.splice(index, 1);
            renderSearchTags();
            globalFilterSites();
        });
    });
}

// 全局筛选函数
function globalFilterSites() {
    if (activeSearchTags.length === 0) {
        document.querySelectorAll('.site-card').forEach(card => {
            card.style.display = 'flex';
        });
        checkEmptyResult();
        return;
    }
    document.querySelectorAll('.site-card').forEach(card => {
        // 👇 修改：新增站点搜索标签内容加入匹配字段
        const nameDescText = (card.querySelector('.site-name').textContent + card.querySelector('.site-desc').textContent).toLowerCase();
        const tagText = Array.from(card.querySelectorAll('.search-tag-item')).map(tag => tag.textContent).join('').toLowerCase();
        const siteText = nameDescText + tagText;
        const isMatch = activeSearchTags.every(tag => siteText.includes(tag));
        card.style.display = isMatch ? 'flex' : 'none';
    });
    checkEmptyResult();
}



// 空结果检查
function checkEmptyResult() {
    document.querySelectorAll('.empty-result').forEach(el => el.remove());
    const visibleSites = Array.from(document.querySelectorAll('.site-card')).filter(card => getComputedStyle(card).display !== 'none').length;
    if (visibleSites === 0) {
        const emptyEl = document.createElement('div');
        emptyEl.className = 'empty-result';
        emptyEl.textContent = '没有找到匹配的站点，请尝试删除部分筛选标签~';
        document.querySelector('.cate-content-wrapper').appendChild(emptyEl);
    }
}