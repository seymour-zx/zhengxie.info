#!/usr/bin/python
# -*- coding: UTF-8 -*-
from package_update.ready import ready
from package_update.tool import linkpath, fwinfo, frinfo
import time
import os
import urllib.request
import webbrowser

def div_main(htmlfolder, indexfolder, txtfolder, gmtime):
    if True: # 简化条件判断语句
        x=0
        if htmlfolder=='../../':
            x=100
        elif not htmlfolder.find('../../private/')==-1:
            x=200
            if not htmlfolder.find('/bookmark/')==-1:
                x=201
        elif not htmlfolder.find('../../base/')==-1:
            x=300
            if not htmlfolder.find('/sitemap/')==-1:
                x=301
        elif not htmlfolder.find('../../unit/')==-1:
            x=400
        print(x,htmlfolder)    
    info = '\n\n    <!-- 页面核心 -->\n    <div class="core">'
    if True:
        if x==0:
            info = info + '\n        <main>\n'
        elif x==100:
            info = info + '\n        <main>\n'
        elif x==200:
            info = info + '\n        <main>\n'
        elif x==300:
            info = info + '\n        <main>\n'
        elif x==301:
            info = info + '\n        <main>\n'
        elif x==400:
            info = info + '\n        <main>\n'
        else:
            info = info + '\n        <main>\n'
    if True:
        if x==300 or x==301 or x==400:
            info = info + '\n            <div style="text-align: center;"><h1>' + frinfo('title.txt', indexfolder) + '</h1></div>'
            if x==400:
                info = info + '\n            <h6 style="text-indent: 2em;">编著：华朝颐亲王 | 正协信息客栈 | '
                datetime1 = time.strftime('%Y-%m-%dT%H:%MZ', gmtime)
                datetime2 = time.strftime('%Y年%m月%d日', gmtime)
                datetime = '<time datetime="' + datetime1 + '" pubtime >' + datetime2 + '</time>'
                info = info + datetime
                info = info + '</h6>'
            info = info + '\n            <hr />'
    if True:
        file = 'main.html'
        path = linkpath(file, indexfolder)
        if os.path.exists(path):
            info = info + frinfo(file, indexfolder)
        else:
            message = ''
            message = message + '\n<!--'
            message = message + '\n            <article>'
            message = message + '\n                <h2>  </h2>'
            message = message + '\n                <p style="text-indent: 2em;">  </p>'
            message = message + '\n                <h3>  </h3>'
            message = message + '\n                <h4>  </h4>'
            message = message + '\n                <pre class="code" >  </pre>'
            message = message + '\n                <hr />'
            message = message + '\n                <br />'
            message = message + '\n                <h2>参考 / Reference</h2>'
            message = message + '\n                <p style="text-indent: 2em;">1. <a href="" ></a></p>'
            message = message + '\n            </article>'
            message = message + '\n-->'
            fwinfo(path, message)
            info = info + message
    message = '''

            <hr />
            <br />
            <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
            <!-- Google广告——横向展示 -->
            <ins class="adsbygoogle"
                style="display:block"
                data-ad-client="ca-pub-6434243103158481"
                data-ad-slot="4856101005"
                data-ad-format="auto"
                data-full-width-responsive="true"></ins>
            <script>
                (adsbygoogle = window.adsbygoogle || []).push({});
            </script>
            <br />
            <hr />

'''
    info = info + message
    info = info + '\n        </main>'
    info = info + '\n    </div>\n\n'
    return info

def info_title(file, indexfolder, txtfolder):
# 'title.txt'
    info = '\n'
    infolist = []
    infolist.append('    <title>')
    path = linkpath(file, indexfolder)
    if os.path.exists(path):
        infolist.append(frinfo(file, indexfolder))
    else:
        fwinfo(path, '')
        # infolist.append('')
    infolist.append(frinfo(file, txtfolder))
    for i in range(len(infolist)):
       info = info + infolist[i]
    return info

def info_keywords(file, indexfolder, txtfolder):
# 'keywords.txt'
    info = '\n'
    infolist = []
    infolist.append(frinfo(file, txtfolder))
    path = linkpath(file, indexfolder)
    if os.path.exists(path):
        infolist.append(frinfo(file, indexfolder))
    else:
        fwinfo(path, '信息,目录,导航,网页,网址导航,网站大全,客栈,亲王,网站导航,网站搜索,导航网站,网站收录,信息分类,网站分类,网址收录,颐亲王,华朝颐亲王,正协信息,正协信息客栈,视频,直播')
        infolist.append('信息,目录,导航,网页,网址导航,网站大全,客栈,亲王,网站导航,网站搜索,导航网站,网站收录,信息分类,网站分类,网址收录,颐亲王,华朝颐亲王,正协信息,正协信息客栈,视频,直播')
    infolist.append('" />')    
    for i in range(len(infolist)):
       info = info + infolist[i]
    return info

def info_description(file, indexfolder, txtfolder):
# 'description.txt'
    info = '\n'
    infolist = []
    infolist.append(frinfo(file, txtfolder))
    path = linkpath(file, indexfolder)
    if os.path.exists(path):
        infolist.append(frinfo(file, indexfolder))
    else:
        fwinfo(path, '')
        # infolist.append('')
    infolist.append('" />')    
    for i in range(len(infolist)):
       info = info + infolist[i]
    return info

def info_link(file, indexfolder, txtfolder, htmlfolder):
# 'link.txt'
    info = ''
    path = linkpath(file, indexfolder)
    if os.path.exists(path):
        info = info + frinfo(file, indexfolder)
    else:
        rel_ico = os.path.relpath("../image/favicon.ico", htmlfolder)
        rel_ico = urllib.request.pathname2url(rel_ico)
        rel_css = os.path.relpath("../css/mystyle.css", htmlfolder)
        rel_css = urllib.request.pathname2url(rel_css)
        infolist = []        
        infolist.append('\n    <link href="')
        infolist.append(rel_ico)
        infolist.append('" rel="shortcut icon" type="image/x-icon" />\n        <!--调用网页图标-->')
        infolist.append('\n    <link href="')
        infolist.append(rel_css)
        infolist.append('" rel="stylesheet" type="text/css" />\n        <!--调用css样式-->\n')
        for i in range(len(infolist)):
            info = info + infolist[i]
        fwinfo(path, info)
    return info


if __name__ == '__main__':
    if ready():
        print('执行程序', 'info_self.py')
else:
    print('导入模块', 'info_self.py')