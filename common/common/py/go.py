"""
  操作流程：
01. 检查路径
02. 当前时间
"""
# coding: utf-8
import os
import urllib.request
import webbrowser
import time
from ready import checkpath, folders, linkpath, frinfo, fwinfo
from ready import reset_footer
from ready import info_title, info_keywords, info_description, info_link





def info_article(file, indexfolder, txtfolder, htmlfolder, gmtime):
# 'article.html'
    info = ''
    info = info + '\n            <h1>' + frinfo('title.txt', indexfolder) + '</h1>'
    if htmlfolder=='../../':
        # 首页
        pass
    elif not htmlfolder.find('/private/')==-1:
        # 私有
        if not htmlfolder.find('bookmark')==-1:
            # 书签
            pass
        else:
            pass
    elif not htmlfolder.find('/base/')==-1:
        # 基础
        if not htmlfolder.find('sitemap')==-1:
            # 主页
            pass
        else:
            pass
    elif not htmlfolder.find('/unit/')==-1:
        # 信息
        info = info + '\n            <h6>华朝颐亲王 | 正协信息客栈 | '
        info = info + time.strftime('%Y-%m-%dT%H:%MZ', gmtime)
        info = info + '</h6>'
    else:
        pass
    info = info + '\n            <hr />'    
    path = linkpath(file, indexfolder)
    if os.path.exists(path):
        info = info + frinfo(file, indexfolder)
    else:
        message = '\n            <article>\n'
        message = message + '\n<!--'
        message = message + '\n                <h2>  </h2>'
        message = message + '\n                <p>&nbsp;&nbsp;  </p>'
        message = message + '\n                <h3>  </h3>'
        message = message + '\n                <h4>  </h4>'
        message = message + '\n                <pre class="code" >  </pre>'
        message = message + '\n                <hr />'
        message = message + '\n                <br />'
        message = message + '\n                <h2>参考 / Reference</h2>'
        message = message + '\n                <a href="  " title="  " >  </a><br />'
        message = message + '\n-->'
        message = message + '\n            </article>'
        fwinfo(path, message)
        info = info + message
    return info






























def htmls(htmlfolder, indexfolder, txtfolder, gmtime):
# 刷新index.html
    # 创建时间
    path = linkpath('gmtime.txt', indexfolder)
    if not os.path.exists(path):
        fwinfo(path, str(int(time.mktime(gmtime))))
    else:
        gmtime = time.localtime(int(frinfo('gmtime.txt', indexfolder)))
    info = ''
    # 通用
    info = info + frinfo('head.txt', txtfolder)
    # 差异化different
    info = info + info_title('title.txt', indexfolder, txtfolder)
    # 差异化different
    info = info + info_keywords('keywords.txt', indexfolder, txtfolder)
    # 差异化different
    info = info + info_description('description.txt', indexfolder, txtfolder)
    # 通用
    info = info + frinfo('author.txt', txtfolder)
    # 差异化different
    info = info + info_link('link.txt', indexfolder, txtfolder, htmlfolder)
    # 通用
    info = info + frinfo('body.txt', txtfolder)
    # 通用
    info = info + frinfo('header.txt', txtfolder)
    # 标签<main>个性化
    if htmlfolder=='../../':
        # 首页
        info = info + '\n        <main class="welcome">\n'
        info = info + frinfo('article.html', indexfolder)
    elif not htmlfolder.find('/private/')==-1:        
        # 私有
        # 书签
        info = info + '\n        <main class="bookmark">\n'
        info = info + frinfo('article.html', indexfolder)
    elif not htmlfolder.find('/base/')==-1:
        # 基础
        if not htmlfolder.find('sitemap')==-1:
            # 主页
            info = info + '\n        <main class="base sitemap">\n'
            info = info + info_article('article.html', indexfolder, txtfolder, htmlfolder, gmtime)
        else:
            info = info + '\n        <main class="base">\n'
            info = info + info_article('article.html', indexfolder, txtfolder, htmlfolder, gmtime)
    elif not htmlfolder.find('/unit/')==-1:
        # 信息
        info = info + '\n        <main class="unit">\n'
        info = info + info_article('article.html', indexfolder, txtfolder, htmlfolder, gmtime)
    else:
        info = info + '\n        <main>\n'
        info = info + info_article('article.html', indexfolder, txtfolder, htmlfolder, gmtime)
    # 通用
    info = info + '\n        </main>\n'
    # 通用
    info = info + frinfo('footer.txt', txtfolder)
    # 通用
    info = info + frinfo('html.txt', txtfolder)
    html = linkpath('index.html', htmlfolder)
    # 在默认浏览器中打开html文件  
    with open(html, 'w', encoding='utf-8') as fw:
        fw.writelines(info)  
    html = os.path.abspath(html)
    # webbrowser.open(html,new = 0, autoraise=True)




def update(txtfolder):
# 更新目录
    n = 999
    htmlfolder = '../../unit/' + str(n) +'/'
    info = ''
    info = info + '      <table>\n'
    while not n==0:
        if os.path.exists(htmlfolder):
            indexfolder = linkpath('index', htmlfolder)
            info = info + '        <tr>\n          <td nowrap="nowrap">'
            gmtime = time.localtime(int(frinfo('gmtime.txt', indexfolder)))
            gmtime = time.strftime('%Y-%m-%d', gmtime)
            info = info + gmtime
            info = info + '</td>\n'
            info = info + '          <td><a href="https://zhengxie.info/unit/' + str(n) +'/"'
            info = info + ' title="" target="_blank">'
            info = info + frinfo('title.txt', indexfolder)
            info = info + '</a></td>\n        </tr>\n'            
        n = n - 1
        htmlfolder = '../../unit/' + str(n) +'/'
    info = info + '      </table>'
    path = linkpath('article.html', '../../base/sitemap/index/')
    fwinfo(path, info)
    htmls(htmlfolder='../../base/sitemap/', indexfolder='../../base/sitemap/index/', txtfolder=txtfolder, gmtime=time.gmtime())

if __name__ == '__main__':
# 主程序
    # cmdfolder = 'D:\\Workspace'
    # pyfolder = 'D:\\Workspace\\Html\\zhengxie.info\\common\\py'
    # pyfolder = 'D:\\Workspace\\znew\\common\\py'
    # 初始化
    if checkpath(): 
        # 当前格林尼治时间
        gmtime = time.gmtime()
        datetime = time.strftime('%Y-%m-%dT%H:%MZ', gmtime)
        # 通用txt/html组件存放于文件夹：
        txtfolder = '../txt/'
        # 更新通用txt/html组件
        reset_footer('footer.txt', txtfolder, gmtime)
        # 读取文件夹目录
        htmlfolders, indexfolders = folders('directory.txt', txtfolder)
        # 更新index.html
        for n in range(len(htmlfolders)):
            htmls(htmlfolder=htmlfolders[n], indexfolder=indexfolders[n], txtfolder=txtfolder, gmtime=gmtime)        
        # 更新目录
        update(txtfolder)

else:
    print('导入模块', 'html_support.py')


























"""
  from urllib.parse import urljoin
  a = urljoin("https://zhengxie.info/folder/currentpage.html", "../")  
  b = urljoin("https://zhengxie.info/folder/currentpage.html", "folder2/anotherpage.html")  
  c = urljoin("https://zhengxie.info/folder/currentpage.html", "/folder3/anotherpage.html")  
  d = urljoin("https://zhengxie.info/folder/currentpage.html", "./folder4/anotherpage.html")
  e = urljoin("https://zhengxie.info/folder/currentpage.html", "../folder5/anotherpage.html")  
  f = urljoin("https://zhengxie.info/folder/currentpage.html", "../finalpage.html")  
  print (a)
  print (b)
  print (c)
  print (d)
  print (e)
  print (f)
"""