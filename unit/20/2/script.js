// 分类折叠展开功能
const level1Titles = document.querySelectorAll('.level1-title');
level1Titles.forEach(title => {
    title.addEventListener('click', () => {
        const cate = title.dataset.cate;
        const content = document.getElementById(`${cate}-content`);
        const icon = title.querySelector('.toggle-icon');
        
        if (content.style.display === 'none') {
            content.style.display = 'block';
            icon.style.transform = 'rotate(0deg)';
        } else {
            content.style.display = 'none';
            icon.style.transform = 'rotate(-90deg)';
        }
    });
});

// 搜索功能
const searchInput = document.getElementById('searchInput');
const searchBtn = document.getElementById('searchBtn');
const siteCards = document.querySelectorAll('.site-card');

function searchSites() {
    const keyword = searchInput.value.trim().toLowerCase();
    if (!keyword) {
        siteCards.forEach(card => {
            card.style.display = 'flex';
        });
        // 恢复分类显示
        document.querySelectorAll('.category-level1-content').forEach(content => {
            content.style.display = 'block';
        });
        document.querySelectorAll('.toggle-icon').forEach(icon => {
            icon.style.transform = 'rotate(0deg)';
        });
        return;
    }

    siteCards.forEach(card => {
        const siteName = card.querySelector('.site-name').textContent.toLowerCase();
        const siteDesc = card.querySelector('.site-desc').textContent.toLowerCase();
        if (siteName.includes(keyword) || siteDesc.includes(keyword)) {
            card.style.display = 'flex';
            // 展开对应分类
            const level1Content = card.closest('.category-level1-content');
            if (level1Content) {
                level1Content.style.display = 'block';
                const icon = level1Content.previousElementSibling.querySelector('.toggle-icon');
                icon.style.transform = 'rotate(0deg)';
            }
        } else {
            card.style.display = 'none';
        }
    });
}

searchBtn.addEventListener('click', searchSites);
searchInput.addEventListener('keyup', e => {
    if (e.key === 'Enter') {
        searchSites();
    }
});


// 一键更换背景功能
const bgColorBtn = document.getElementById('bgColorBtn');
const bgImageBtn = document.getElementById('bgImageBtn');
const bgResetBtn = document.getElementById('bgResetBtn');

// 柔和渐变配色库
const gradientList = [
    'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
    'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
    'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
    'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
    'linear-gradient(135deg, #30cfd0 0%, #330867 100%)',
    'linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)',
    'linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)'
];

// 随机渐变背景切换
bgColorBtn.addEventListener('click', () => {
    document.body.classList.remove('has-bg-image');
    const randomGrad = gradientList[Math.floor(Math.random() * gradientList.length)];
    document.body.style.background = randomGrad;
    localStorage.setItem('nav_bg_type', 'color');
    localStorage.setItem('nav_bg_value', randomGrad);
});

// 随机图片背景切换（用免费无版权的Unsplash随机图API）
bgImageBtn.addEventListener('click', () => {
    document.body.classList.add('has-bg-image');
    const randomImgUrl = `https://picsum.photos/1920/1080?random=${Date.now()}`;
    document.body.style.background = `url(${randomImgUrl}) center/cover no-repeat fixed`;
    localStorage.setItem('nav_bg_type', 'image');
    localStorage.setItem('nav_bg_value', randomImgUrl);
});

// 重置背景
bgResetBtn.addEventListener('click', () => {
    document.body.classList.remove('has-bg-image');
    document.body.style.background = '#f5f7fa';
    localStorage.removeItem('nav_bg_type');
    localStorage.removeItem('nav_bg_value');
});

// 页面加载时恢复用户之前选择的背景
window.addEventListener('load', () => {
    const bgType = localStorage.getItem('nav_bg_type');
    const bgValue = localStorage.getItem('nav_bg_value');
    if (bgType && bgValue) {
        if (bgType === 'image') {
            document.body.classList.add('has-bg-image');
        }
        document.body.style.background = bgValue;
    }
});


// 一级分类切换
document.querySelectorAll('.cate-tab').forEach(tab => {
    tab.addEventListener('click', () => {
        // 切换tab选中状态
        document.querySelectorAll('.cate-tab').forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        const targetCate = tab.dataset.cate;

        if (targetCate === 'all') {
            // 全部分类：显示所有一级分类内容
            document.querySelectorAll('.cate-content').forEach(content => {
                content.style.display = 'block';
                // 全部分类下默认显示每个一级分类的所有二级内容
                const level2AllTab = content.querySelector('.level2-tab[data-level2="all"]');
                if (level2AllTab) level2AllTab.click();
            });
        } else {
            // 普通分类：只显示对应一级分类内容，隐藏其他
            document.querySelectorAll('.cate-content').forEach(content => {
                content.style.display = content.id === `${targetCate}-content` ? 'block' : 'none';
            });
            // 切换到普通分类时默认选中该分类下第一个二级tab
            const firstLevel2Tab = document.querySelector(`#${targetCate}-content .level2-tab`);
            if (firstLevel2Tab) firstLevel2Tab.click();
        }
    });
});


// ========== 轮播功能 ==========
const carousel = document.getElementById('carousel');
const wrapper = carousel.querySelector('.carousel-wrapper');
const items = carousel.querySelectorAll('.carousel-item');
const prevBtn = carousel.querySelector('.carousel-prev');
const nextBtn = carousel.querySelector('.carousel-next');
const indicators = carousel.querySelectorAll('.indicator');
let currentIndex = 0;
const totalItems = items.length;
let autoPlayTimer;

// 切换轮播
function goToSlide(index) {
    if (index < 0) index = totalItems - 1;
    if (index >= totalItems) index = 0;
    currentIndex = index;
    wrapper.style.transform = `translateX(-${currentIndex * 100}%)`;
    // 更新指示器
    indicators.forEach((ind, i) => {
        ind.classList.toggle('active', i === currentIndex);
    });
}

// 自动轮播
function startAutoPlay() {
    autoPlayTimer = setInterval(() => {
        goToSlide(currentIndex + 1);
    }, 3000);
}

// 暂停轮播
function stopAutoPlay() {
    clearInterval(autoPlayTimer);
}

// 事件绑定
prevBtn.addEventListener('click', () => goToSlide(currentIndex - 1));
nextBtn.addEventListener('click', () => goToSlide(currentIndex + 1));
indicators.forEach(ind => {
    ind.addEventListener('click', () => goToSlide(parseInt(ind.dataset.index)));
});
carousel.addEventListener('mouseenter', stopAutoPlay);
carousel.addEventListener('mouseleave', startAutoPlay);
startAutoPlay();

// ========== 吸顶功能 ==========
const stickyContainer = document.getElementById('stickyContainer');
const stickyPlaceholder = document.getElementById('stickyPlaceholder');
const headerHeight = document.querySelector('.fixed-header').offsetHeight;

function handleScroll() {
    const containerTop = stickyContainer.getBoundingClientRect().top;
    if (containerTop <= headerHeight) {
        stickyContainer.classList.add('sticky');
        stickyPlaceholder.style.display = 'block';
        stickyPlaceholder.style.height = `${stickyContainer.offsetHeight}px`;
    } else {
        stickyContainer.classList.remove('sticky');
        stickyPlaceholder.style.display = 'none';
    }
}

window.addEventListener('scroll', handleScroll);


// 二级分类切换
document.querySelectorAll('.level2-tab').forEach(tab => {
    tab.addEventListener('click', () => {
        const parentCate = tab.closest('.cate-content');
        const targetLevel2 = tab.dataset.level2;
        // 切换当前一级分类下的二级tab选中状态
        parentCate.querySelectorAll('.level2-tab').forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        if (targetLevel2 === 'all') {
            // 二级全部：显示当前一级分类下所有二级内容
            parentCate.querySelectorAll('.category-level2').forEach(level2 => {
                level2.style.display = 'block';
            });
        } else {
            // 普通二级分类：只显示对应二级内容，隐藏其他
            parentCate.querySelectorAll('.category-level2').forEach(level2 => {
                level2.style.display = level2.dataset.level2 === targetLevel2 ? 'block' : 'none';
            });
        }
    });
});

// 页面加载默认触发一级分类的切换（兼容初始化）
document.querySelector('.cate-tab.active').click();