#!/usr/bin/python
# -*- coding: UTF-8 -*-
from package_update.ready import ready
from package_update.tool import linkpath, fwinfo, frinfo
import time
import os
import webbrowser
  


def container(lines):
    if True:
    # info初始化
        info = ''
        info = info + '\n'
    if True:
    # 列标题设置
        # 分割成多少列？
        column = 16
        # 简称
        name = 5
        # 网址
        site = name + 1
        # 描述title
        title = site + 1
        # 图标网址
        favicon = title + 1
        # 层级划分
        stage = favicon + 1
        if True:
            # 根关键词
            deep_start = stage + 1
            # 分类深度
            deep = 3
            # 关键词串联
            pre_keywords = []
        # 网址是否链接
        siteif = deep_start + deep
        # 图标是否可用
        faviconif = siteif + 1
        # 其他无关内容
        other = faviconif + 1
    if True:
    # 读取与处理网址列表
        for i in range(len(lines)):
            keyword = ''
            keywords = []
            line = lines[i]
            if True:
            # 关键词串联
                for j in range(deep):
                    keywords.append(line[deep_start + j])
                    keyword = keyword + line[deep_start + j]
                    if not line[deep_start + j]=='':
                        depth = j + 1 
            if True:
            # 制作链接盒子
                if line[siteif]=='':
                # 无链接
                    img = ''
                    a = line[name]
                    imga = '<div class="div_img-a">' + img + a + '</div>'
                elif line[faviconif]=='':
                # 无图标
                    img = ''
                    a = '<a href="' + line[site] + '" title="' + line[title] +  '" " target="_blank" >' + line[name] + '</a>'
                    imga = '<div class="div_img-a">' + img + a + '</div>'
                else:
                    img = '<img src="' + line[favicon] + '">'
                    a = '<a href="' + line[site] + '" title="' + line[title] +  '" target="_blank" >' + line[name] + '</a>'
                    imga = '<div class="div_img-a">' + img + a + '</div>'
            if keywords==pre_keywords:
                info = info + '        ' * (depth + 2)
                info = info + imga
                info = info + '\n'
            elif i==0 :
                pre_keywords = keywords
                pre_depth = depth
                info = info + '            <div class="portal-container">\n'
                label = '<label for="' + line[stage] + '">' + line[stage] + '</label>'                
                info = info + '            <div class="portal-label">' + label + '</div>\n'
                info = info + '            <input checked id="' + line[stage] + '" class="" type="checkbox" />\n'
                info = info + '            <div class="portal-wrapper">\n'
                info = info + '    ' * (2 + 2 * depth)
                info = info + '<div class="box-lv1 portal-box">'
                info = info + '\n'
                info = info + '    ' * (3 + 2 * depth)
                label = '<label for="' + line[stage] + keyword + '">' + keywords[depth-1] + '</label>'
                info = info + '<div class="portal-label">' + label + imga + '</div>'
                info = info + '\n'
                info = info + '    ' * (3 + 2 * depth)
                info = info + '<input id="' + line[stage] + keyword + '" class="" type="checkbox" />'
                info = info + '\n'
                info = info + '    ' * (3 + 2 * depth)
                info = info + '<div class="content-lv1 portal-content">'
                info = info + '\n'
            else:
                if True:
                # 判断从第几层不同
                    for j in range(deep):
                        if not keywords[j]==pre_keywords[j]:
                            branch = j + 1
                            break
                if (branch==depth) and (pre_keywords[depth-1]==''):
                    pre_keywords = keywords
                    pre_depth = depth
                    info = info + '    ' * (2 + 2 * depth)
                    info = info + '<div class="box-lv' + str(depth) + ' portal-box">'
                    info = info + '\n'
                    info = info + '    ' * (3 + 2 * depth)
                    label = '<label for="' + line[stage] + keyword + '">' + keywords[depth-1] + '</label>'
                    info = info + '<div class="portal-label">' + label + imga + '</div>'
                    info = info + '\n'
                    info = info + '    ' * (3 + 2 * depth)
                    info = info + '<input id="' + line[stage] + keyword + '" class="" type="checkbox" />'
                    info = info + '\n'
                    info = info + '    ' * (3 + 2 * depth)
                    info = info + '<div class="content-lv' + str(depth) + ' portal-content">'
                    info = info + '\n'
                else:
                    if True:
                    # 先补</div>
                        n = pre_depth - branch + 1
                        for j in range(n):
                            info = info + '    ' * (3 + 2 * (pre_depth-j))
                            info = info + '</div>'
                            info = info + '\n'
                            info = info + '    ' * (2 + 2 * (pre_depth-j))
                            info = info + '</div>'
                            info = info + '\n'
                    if True:
                        pre_keywords = keywords
                        pre_depth = depth
                        info = info + '    ' * (2 + 2 * depth)
                        info = info + '<div class="box-lv' + str(depth) + ' portal-box">'
                        info = info + '\n'
                        info = info + '    ' * (3 + 2 * depth)
                        label = '<label for="' + line[stage] + keyword + '">' + keywords[depth-1] + '</label>'
                        info = info + '<div class="portal-label">' + label + imga + '</div>'
                        info = info + '\n'
                        info = info + '    ' * (3 + 2 * depth)
                        info = info + '<input id="' + line[stage] + keyword + '" class="" type="checkbox" />'
                        info = info + '\n'
                        info = info + '    ' * (3 + 2 * depth)
                        info = info + '<div class="content-lv' + str(depth) + ' portal-content">'
                        info = info + '\n'
    if True:
    # 先补</div>
        for j in range(depth):
            info = info + '    ' * (3 + 2 * (depth-j))
            info = info + '</div>'
            info = info + '\n'
            info = info + '    ' * (2 + 2 * (depth-j))
            info = info + '</div>'
            info = info + '\n'
    info = info + '            </div>'
    info = info + '\n'
    info = info + '            </div>'
    info = info + '\n'
    return info
        

if __name__ == '__main__':
    if ready():
        message = '''
            <div class="search-container"><!-- 搜索框 -->
                <div class="search-label">
                    <label for="search-网页">网页</label>
                    <label for="search-视频">视频</label>
                    <label for="search-MP3">MP3</label>
                </div><!-- <div // class="search-label"> -->
                <input id="search-input" placeholder="欢迎光临正协信息客栈！" value="" type="search" />

                <input checked id="search-网页" name="search-label" class="on-next-off" type="radio">
                    <div class="search-wrapper">
                        <button>谷歌</button>
                            <form action="https://www.google.com/search" method="get" target="_blank">
                                <input value="正协信息客栈" name="q" type="search" />
                                <input value="谷歌网页" type="submit" />
                            </form>
                        <button>百度</button>
                            <form action="https://baidu.com/s" method="get" target="_blank">
                                <input value="华朝颐亲王" name="wd" type="search" />
                                <input value="百度网页" type="submit" />
                            </form>
                    </div><!-- <div // class="search-wrapper"> -->

                <input id="search-视频" name="search-label" class="on-next-off" type="radio">
                    <div class="search-wrapper">
                        <button>Youtube</button>
                            <form action="https://www.youtube.com/results" method="get" target="_blank">
                                <input value="颐亲王" name="search_query" type="search" />
                                <input value="Youtube" type="submit" />
                            </form>         
                    </div><!-- <div // class="search-wrapper"> -->

                <input id="search-MP3" name="search-label" class="on-next-off" type="radio">
                    <div class="search-wrapper">
                        <button>千千音乐</button>
                        <form action="https://music.taihe.com/search" method="get" target="_blank" accept-charset="UTF-8">
                            <input value="new_mp3" name="from" type="hidden" />
                            <input value="夜曲" name="key" type="search" />
                            <input value="千千音乐" type="submit" />
                        </form>
                    </div><!-- <div // class="search-wrapper"> -->        
            </div><!-- <div // 搜索框 class="search-container"> -->

            '''
        if True:
        # info初始化
            info = ''
            info = info + message
            info = info + '\n'
            info = info + '            <!-- 导航首页 -->\n'
        if True:
        # 读取与处理网址列表
            x = 0
            pre_stage = '不可能什么层级都不是'
            path = './csv/网址_UTF-8.csv'        
            with open(path, 'r', encoding='utf-8') as fr:
                utf8s = fr.readlines()
            for i in range(1,len(utf8s)):
                utf8 = utf8s[i].strip().split(',', 15)
                if not pre_stage==utf8[9]:
                    x=x+1
                    pre_stage=utf8[9]
            array = [[] for k in range(x)]
            n = -1
            for i in range(1,len(utf8s)):
                utf8 = utf8s[i].strip().split(',', 15)
                if not pre_stage==utf8[9]:
                    n = n+1
                    pre_stage=utf8[9]
                    array[n].append(utf8)
                else:
                    array[n].append(utf8)
            for i in range(x):
                info = info + container(array[i])

        info = info + '\n            <!-- // 导航首页 -->\n'        
        fwinfo('../../index/main.html', info)
    print('wangzheng')

else:
    print('模块包初始化', 'test_new.py')