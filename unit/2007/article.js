// 文章详情页交互脚本
document.addEventListener('DOMContentLoaded', function() {
    // 移动端菜单切换
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    
    mobileMenuBtn.addEventListener('click', function() {
        navLinks.classList.toggle('show');
    });
    
    // 点击页面其他区域关闭菜单
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.mobile-menu-btn') && !e.target.closest('.nav-links')) {
            navLinks.classList.remove('show');
        }
    });
    
    // 窗口大小变化时重置菜单
    window.addEventListener('resize', function() {
        if (window.innerWidth > 992) {
            navLinks.classList.remove('show');
        }
    });
    
    // 代码复制功能
    const copyButtons = document.querySelectorAll('.copy-code');
    copyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const codeBlock = this.closest('.code-block');
            const code = codeBlock.querySelector('code').textContent;
            
            navigator.clipboard.writeText(code).then(() => {
                const originalText = this.innerHTML;
                this.innerHTML = '<i class="fas fa-check"></i> 已复制';
                this.style.backgroundColor = 'var(--success-color)';
                this.style.borderColor = 'var(--success-color)';
                
                setTimeout(() => {
                    this.innerHTML = originalText;
                    this.style.backgroundColor = '';
                    this.style.borderColor = '';
                }, 2000);
            }).catch(err => {
                console.error('复制失败: ', err);
                alert('复制失败，请手动复制代码');
            });
        });
    });
    
    // 评论表单提交
    const commentForm = document.getElementById('commentForm');
    const cancelBtn = document.querySelector('.cancel-btn');
    
    commentForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const comment = document.getElementById('comment').value;
        
        if (name && email && comment) {
            // 在实际应用中，这里应该发送数据到服务器
            alert('评论提交成功！感谢您的参与。');
            commentForm.reset();
            
            // 模拟添加新评论
            addNewComment(name, comment);
        } else {
            alert('请填写所有必填字段！');
        }
    });
    
    cancelBtn.addEventListener('click', function() {
        commentForm.reset();
    });
    
    // 添加新评论函数
    function addNewComment(name, content) {
        const commentsList = document.querySelector('.comments-list');
        const commentCount = document.querySelector('.section-title');
        
        // 更新评论数量
        const currentCount = parseInt(commentCount.textContent.match(/\d+/)) || 0;
        commentCount.textContent = `评论 (${currentCount + 1})`;
        
        // 创建新评论元素
        const newComment = document.createElement('div');
        newComment.className = 'comment';
        newComment.innerHTML = `
            <div class="comment-header">
                <div class="comment-avatar">${name.charAt(0)}</div>
                <div>
                    <div class="comment-author">${name}</div>
                    <div class="comment-time"><i class="far fa-clock"></i> 刚刚</div>
                </div>
            </div>
            <div class="comment-content">${content}</div>
            <div class="comment-actions">
                <button class="comment-action like-btn">
                    <i class="far fa-thumbs-up"></i> 0
                </button>
                <button class="comment-action reply-btn">
                    <i class="far fa-comment"></i> 回复
                </button>
            </div>
        `;
        
        // 插入到评论列表顶部
        commentsList.insertBefore(newComment, commentsList.firstChild);
        
        // 为新评论的点赞按钮添加事件
        const newLikeBtn = newComment.querySelector('.like-btn');
        newLikeBtn.addEventListener('click', handleLike);
        
        // 滚动到新评论
        newComment.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    
    // 点赞功能
    const likeButtons = document.querySelectorAll('.like-btn');
    
    function handleLike() {
        const currentCount = parseInt(this.textContent.match(/\d+/)) || 0;
        this.innerHTML = `<i class="fas fa-thumbs-up"></i> ${currentCount + 1}`;
        this.style.color = 'var(--accent-color)';
        
        // 防止重复点击
        this.removeEventListener('click', handleLike);
    }
    
    likeButtons.forEach(button => {
        button.addEventListener('click', handleLike);
    });
    
    // 目录导航
    const tocLinks = document.querySelectorAll('.toc-link');
    const sections = document.querySelectorAll('.article-content h2');
    
    // 为章节添加ID（如果还没有）
    sections.forEach((section, index) => {
        if (!section.id) {
            section.id = `section${index + 1}`;
        }
    });
    
    // 滚动时更新目录激活状态
    function updateActiveToc() {
        let currentSection = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (window.pageYOffset >= sectionTop - 150) {
                currentSection = section.id;
            }
        });
        
        tocLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSection}`) {
                link.classList.add('active');
            }
        });
    }
    
    // 目录链接点击事件
    tocLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 100,
                    behavior: 'smooth'
                });
                
                // 更新URL哈希（不滚动页面）
                history.pushState(null, null, targetId);
                
                // 更新目录激活状态
                tocLinks.forEach(l => l.classList.remove('active'));
                this.classList.add('active');
            }
        });
    });
    
    window.addEventListener('scroll', updateActiveToc);
    updateActiveToc(); // 初始调用
    
    // 分享功能
    const shareButtons = {
        copyLink: document.getElementById('copy-link'),
        shareTwitter: document.getElementById('share-twitter'),
        shareWechat: document.getElementById('share-wechat')
    };
    
    // 复制链接
    if (shareButtons.copyLink) {
        shareButtons.copyLink.addEventListener('click', function() {
            const url = window.location.href;
            navigator.clipboard.writeText(url).then(() => {
                const originalText = this.innerHTML;
                this.innerHTML = '<i class="fas fa-check"></i> 已复制';
                this.style.backgroundColor = 'var(--success-color)';
                
                setTimeout(() => {
                    this.innerHTML = originalText;
                    this.style.backgroundColor = '';
                }, 2000);
            }).catch(err => {
                console.error('复制失败: ', err);
                alert('复制失败，请手动复制链接');
            });
        });
    }
    
    // 分享到Twitter
    if (shareButtons.shareTwitter) {
        shareButtons.shareTwitter.addEventListener('click', function() {
            const url = encodeURIComponent(window.location.href);
            const text = encodeURIComponent(document.title);
            const twitterUrl = `https://twitter.com/intent/tweet?url=${url}&text=${text}`;
            window.open(twitterUrl, '_blank', 'width=600,height=400');
        });
    }
    
    // 订阅功能
    const subscribeBtn = document.querySelector('.subscribe-btn');
    const subscribeInput = document.querySelector('.subscribe-input');
    
    if (subscribeBtn && subscribeInput) {
        subscribeBtn.addEventListener('click', function() {
            if (subscribeInput.value && subscribeInput.value.includes('@')) {
                alert('订阅成功！感谢您的订阅。');
                subscribeInput.value = '';
            } else {
                alert('请输入有效的邮箱地址！');
            }
        });
        
        subscribeInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                subscribeBtn.click();
            }
        });
    }
    
    // 返回顶部按钮
    const backToTopBtn = document.getElementById('backToTop');
    
    if (backToTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTopBtn.classList.add('visible');
            } else {
                backToTopBtn.classList.remove('visible');
            }
        });
        
        backToTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // 评论分页
    const pageButtons = document.querySelectorAll('.page-btn');
    pageButtons.forEach(button => {
        button.addEventListener('click', function() {
            if (this.classList.contains('active')) return;
            
            // 移除所有active类
            pageButtons.forEach(btn => btn.classList.remove('active'));
            // 为当前按钮添加active类
            this.classList.add('active');
            
            // 实际应用中这里会加载对应页面的评论
            const pageNum = this.textContent;
            if (pageNum !== '...' && !this.classList.contains('next-btn')) {
                console.log(`加载第 ${pageNum} 页评论`);
            }
        });
    });
    
    // 页面加载完成后的初始化
    console.log('文章详情页加载完成');
});