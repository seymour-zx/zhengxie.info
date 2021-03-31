#!/usr/bin/python
# -*- coding: UTF-8 -*-
from package_update.ready import ready
from package_update.tool import frinfo, fwinfo

if ready():
    if True:
        message='''
            <div class="search-container"><!-- 搜索框 -->
                <div class="search-label">
                    <label for="search-网页">网页</label>
                    <label for="search-视频">视频</label>
                    <label for="search-MP3">MP3</label>
                </div><!-- <div // class="search-label"> -->
                <input value="欢迎光临正协信息客栈！" id="search-input" type="search" />

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
        info = ''
        info = info + message + '\n'
        info = info + '            <!-- 导航首页 -->\n'
        info = info + '            <div class="portal-box">\n'
    if True:
    # 列标题设置
        # 分割成多少列？            
        column = 15
        # 简称
        name = 5
        # 网址
        site = 6
        # 描述title
        title = 7
        # 图标网址
        favicon = 8
        if True:
            # 分类深度
            deep = 3
            # 根关键词
            deep_start = 9
            # 关键词串联
            pre_keywords = []
        # 网址是否链接
        siteif = 12
        # 图标是否可用
        faviconif = 13
        # 其他无关内容
        other = 14
    if True:
    # 读取与处理网址列表
        path = './csv/网址_UTF-8.csv'        
        with open(path, 'r', encoding='utf-8') as fr:
            lines = fr.readlines()
        for i in range(1,len(lines)):
            keyword = ''
            keywords = []
            line = lines[i].strip().split(',', column-1)
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
                    a = '<a href="' + line[site] + '" title="' + line[title] +  '" >' + line[name] + '</a>'
                    imga = '<div class="div_img-a">' + img + a + '</div>'
                else:
                    img = '<img src="' + line[favicon] + '">'
                    a = '<a href="' + line[site] + '" title="' + line[title] +  '" >' + line[name] + '</a>'
                    imga = '<div class="div_img-a">' + img + a + '</div>'
            if keywords==pre_keywords:
                info = info + '        ' * (depth + 2)
                info = info + imga
                info = info + '\n'
            elif i==1 :
                pre_keywords = keywords
                pre_depth = depth
                info = info + '    ' * (2 + 2 * depth)
                info = info + '<div class="portal-wrapper-lv1 portal-wrapper">'
                info = info + '\n'
                info = info + '    ' * (3 + 2 * depth)
                info = info + '<label for="' + keyword + '">' + keywords[depth-1] + imga + '</label>'
                info = info + '\n'
                info = info + '    ' * (3 + 2 * depth)
                info = info + '<input id="' + keyword + '" class="on-next-off" type="checkbox" />'
                info = info + '\n'
                info = info + '    ' * (3 + 2 * depth)
                info = info + '<div class="portal-box">'
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
                    info = info + '<div class="portal-wrapper-lv' + str(depth) + ' portal-wrapper">'
                    info = info + '\n'
                    info = info + '    ' * (3 + 2 * depth)
                    info = info + '<label for="' + keyword + '">' + keywords[depth-1] + imga + '</label>'
                    info = info + '\n'
                    info = info + '    ' * (3 + 2 * depth)
                    info = info + '<input id="' + keyword + '" class="on-next-off" type="checkbox" />'
                    info = info + '\n'
                    info = info + '    ' * (3 + 2 * depth)
                    info = info + '<div class="portal-box">'
                    info = info + '\n'
                else:
                    if True:
                    # 先补</div>
                        n = pre_depth - branch + 1
                        for j in range(n):
                            info = info + '    ' * (5 + 2 * (depth-j))
                            info = info + '</div>'
                            info = info + '\n'
                            info = info + '    ' * (4 + 2 * (depth-j))
                            info = info + '</div>'
                            info = info + '\n'
                    if True:
                        pre_keywords = keywords
                        pre_depth = depth
                        info = info + '    ' * (2 + 2 * depth)
                        info = info + '<div class="portal-wrapper-lv' + str(depth) + ' portal-wrapper">'
                        info = info + '\n'
                        info = info + '    ' * (3 + 2 * depth)
                        info = info + '<label for="' + keyword + '">' + keywords[depth-1] + imga + '</label>'
                        info = info + '\n'
                        info = info + '    ' * (3 + 2 * depth)
                        info = info + '<input id="' + keyword + '" class="on-next-off" type="checkbox" />'
                        info = info + '\n'
                        info = info + '    ' * (3 + 2 * depth)
                        info = info + '<div class="portal-box">'
                        info = info + '\n'
    if True:
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
        info = info + '\n            <!-- // 导航首页 -->\n'
    fwinfo('../../base/link/index/main.html', info)

        
