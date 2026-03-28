// 政协网站交互脚本
document.addEventListener('DOMContentLoaded', function() {
    // 移动端菜单切换
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileNavOverlay = document.getElementById('mobileNavOverlay');
    const mobileNavClose = document.querySelector('.mobile-nav-close');
    
    if (mobileMenuBtn && mobileNavOverlay) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileNavOverlay.classList.add('active');
            document.body.style.overflow = 'hidden'; // 防止背景滚动
        });
        
        mobileNavClose.addEventListener('click', function() {
            mobileNavOverlay.classList.remove('active');
            document.body.style.overflow = 'auto';
        });
        
        // 点击遮罩层关闭菜单
        mobileNavOverlay.addEventListener('click', function(e) {
            if (e.target === mobileNavOverlay) {
                mobileNavOverlay.classList.remove('active');
                document.body.style.overflow = 'auto';
            }
        });
        
        // ESC键关闭菜单
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && mobileNavOverlay.classList.contains('active')) {
                mobileNavOverlay.classList.remove('active');
                document.body.style.overflow = 'auto';
            }
        });
    }
    
    // 搜索表单提交
    const searchForm = document.querySelector('.search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const searchInput = this.querySelector('.search-input');
            const searchTerm = searchInput.value.trim();
            
            if (searchTerm) {
                alert(`搜索关键词: "${searchTerm}"\n在实际应用中，这里会执行搜索功能并跳转到搜索结果页。`);
                // 在实际应用中，这里应该跳转到搜索页面或显示搜索结果
                // window.location.href = `/search?q=${encodeURIComponent(searchTerm)}`;
            } else {
                searchInput.focus();
            }
        });
    }
    
    // 订阅表单提交
    const subscribeForm = document.querySelector('.subscribe-form');
    if (subscribeForm) {
        subscribeForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const emailInput = this.querySelector('.subscribe-input');
            const email = emailInput.value.trim();
            
            if (email && validateEmail(email)) {
                alert(`感谢订阅！我们将发送政协新闻到您的邮箱: ${email}`);
                emailInput.value = '';
                
                // 在实际应用中，这里应该发送订阅请求到服务器
                // fetch('/api/subscribe', { method: 'POST', body: JSON.stringify({ email }) });
            } else {
                alert('请输入有效的邮箱地址！');
                emailInput.focus();
            }
        });
    }
    
    // 邮箱验证函数
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
    
    // 返回顶部按钮
    const backToTopBtn = document.getElementById('backToTop');
    
    if (backToTopBtn) {
        // 显示/隐藏返回顶部按钮
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTopBtn.classList.add('visible');
            } else {
                backToTopBtn.classList.remove('visible');
            }
        });
        
        // 点击返回顶部
        backToTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // 轮播指示器交互
    const indicators = document.querySelectorAll('.indicator');
    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', function() {
            // 移除所有active类
            indicators.forEach(ind => ind.classList.remove('active'));
            // 为当前点击的指示器添加active类
            this.classList.add('active');
            
            // 在实际应用中，这里会切换横幅内容
            console.log(`切换到横幅 ${index + 1}`);
        });
    });
    
    // 模拟轮播自动切换
    let currentIndicatorIndex = 0;
    function rotateCarousel() {
        currentIndicatorIndex = (currentIndicatorIndex + 1) % indicators.length;
        indicators.forEach(ind => ind.classList.remove('active'));
        indicators[currentIndicatorIndex].classList.add('active');
    }
    
    // 每5秒切换一次横幅
    // setInterval(rotateCarousel, 5000);
    
    // 快速入口点击效果
    const quickItems = document.querySelectorAll('.quick-item');
    quickItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const title = this.querySelector('h3').textContent;
            console.log(`快速入口被点击: ${title}`);
            
            // 在实际应用中，这里会跳转到对应页面
            // window.location.href = this.getAttribute('href');
            
            // 添加点击反馈效果
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
        });
    });
    
    // 新闻项点击效果
    const newsItems = document.querySelectorAll('.news-item');
    newsItems.forEach(item => {
        item.addEventListener('click', function(e) {
            // 防止点击链接时触发父元素的事件
            if (e.target.tagName === 'A' || e.target.closest('a')) {
                return;
            }
            
            const link = this.querySelector('a');
            if (link) {
                console.log(`打开新闻: ${link.textContent}`);
                // 在实际应用中，这里会跳转到新闻详情页
                // window.location.href = link.getAttribute('href');
            }
        });
    });
    
    // 通知项点击效果
    const noticeItems = document.querySelectorAll('.notice-link');
    noticeItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const title = this.querySelector('.notice-title').textContent;
            console.log(`打开通知: ${title}`);
            
            // 在实际应用中，这里会跳转到通知详情页
            // window.location.href = this.getAttribute('href');
        });
    });
    
    // 提案项点击效果
    const proposalItems = document.querySelectorAll('.proposal-title a');
    proposalItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const title = this.textContent;
            console.log(`查看提案: ${title}`);
            
            // 在实际应用中，这里会跳转到提案详情页
            // window.location.href = this.getAttribute('href');
        });
    });
    
    // 专题栏目点击效果
    const columnLinks = document.querySelectorAll('.column-link');
    columnLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const columnTitle = this.closest('.column-item').querySelector('h3').textContent;
            console.log(`进入专题栏目: ${columnTitle}`);
            
            // 在实际应用中，这里会跳转到专题栏目页面
            // window.location.href = this.getAttribute('href');
        });
    });
    
    // 底部链接点击效果
    const footerLinks = document.querySelectorAll('.footer a');
    footerLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // 如果是外部链接，在实际应用中会直接跳转
            // 这里只是模拟效果
            console.log(`导航到: ${this.textContent}`);
        });
    });
    
    // 网站统计数字动画效果
    const statNumbers = document.querySelectorAll('.stat-number');
    function animateNumbers() {
        statNumbers.forEach(stat => {
            const target = parseInt(stat.textContent.replace(/,/g, ''));
            const duration = 2000; // 动画持续时间
            const step = target / (duration / 16); // 每16ms增加的值
            let current = 0;
            
            const timer = setInterval(() => {
                current += step;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                stat.textContent = Math.floor(current).toLocaleString();
            }, 16);
        });
    }
    
    // 当统计区域进入视口时触发动画
    const statsWidget = document.querySelector('.stats-widget');
    if (statsWidget) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateNumbers();
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        
        observer.observe(statsWidget);
    }
    
    // 页面加载完成后的初始化
    console.log('政协信息网站加载完成');
    
    // 模拟数据加载
    setTimeout(() => {
        console.log('页面数据加载完成');
    }, 1000);
});