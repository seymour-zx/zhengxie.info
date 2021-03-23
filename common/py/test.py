#!/usr/bin/python
# -*- coding: UTF-8 -*-
from package_update.ready import ready
from package_update.tool import frinfo, fwinfo

if ready():
    message='''
            <div class="searchBox"><!-- 搜索框 -->    
                <form action="https://www.google.com/search" method="GET" target="_blank">
                    <input class='inputBox' name="q" type="search" value="正协信息客栈">
                    <input class='searchBtn' type="submit" value="谷歌一下"  />
                </form>
                <form action="http://baidu.com/s" method="GET" target="_blank">
                    <input class='inputBox' name="wd" type="search" value="华朝颐亲王">
                    <input class='searchBtn' type="submit" value="百度一下"  />
                </form>
                <form action="https://www.youtube.com/results" method="GET" target="_blank">
                    <input class='inputBox' name="search_query" type="search" value="坂井泉水">
                    <input class='searchBtn' type="submit" value="Youtube搜索"  />
                </form>
                <!-- <form action="https://music.taihe.com/search" method="GET" target="_blank" accept-charset="UTF-8">
                <input type="hidden" name="from" value="new_mp3">
                <input class='inputBox' type="search" name="key" value='夜曲'>
                <input class='searchBtn' type="submit" value="千千音乐"  />
                </form>  -->
            </div><!-- <div class="searchBox">搜索框 --> 
'''
    path = './csv/temp utf-8.csv'    
    prekeyword = '关键词'
    presubword = ''
    info = message + '\n'
    info = info + '            <!-- 导航首页 -->\n'
    info = info + '            <div class="portal-box">'
    info = info + '\n'
    with open(path, 'r', encoding='utf-8') as fr:
        lines = fr.readlines()
    for i in range(1,len(lines)):
        line = lines[i]
        line = line.strip()
        s1, s2, name, site, favicon, keyword, subword, siteif, faviconif, other = line.split(',', 9)
        # print(s1, s2, name, site, favicon, keyword, subword, other)
        # print( subword=='')
        if True:
            if siteif=='':
                img = ''
                a = name
                imga = '<div class="div_img-a">' + img + a + '</div>'
            elif faviconif=='':
                img = ''
                a = '<a href="' + site + '">' + name +'</a>'
                imga = '<div class="div_img-a">' + img + a + '</div>'
            else:
                img = '<img src="' + favicon + '">'
                a = '<a href="' + site + '">' + name +'</a>'
                imga = '<div class="div_img-a">' + img + a + '</div>'
        if (prekeyword + presubword) == (keyword + subword):
            info = info + '                            '
            info = info + imga
            info = info + '\n'   
        else:
            if i==1:
                prekeyword=keyword
                info = info + '                <div class="portal-wrapper">'
                info = info + '\n'
                info = info + '                    <label for="' + keyword + '">' + keyword + imga + '</label>'
                info = info + '\n'
                info = info + '                    <input id="' + keyword + '" class="on-off" type="checkbox"  />'
                info = info + '\n'
                info = info + '                    <div class="portal-box">'
                info = info + '\n'
            else:
                if prekeyword == keyword:
                    if presubword =='':
                        presubword=subword                        
                        info = info + '                        <div class="portal-wrapper">'
                        info = info + '\n'
                        info = info + '                        <label for="' + keyword + subword + '">' + subword + imga + '</label>'
                        info = info + '\n'
                        info = info + '                        <input id="' + keyword + subword + '" class="on-off" type="checkbox"  />'
                        info = info + '\n'
                        info = info + '                        <div class="portal-box">'
                        info = info + '\n'
                    else:
                        info = info + '                            </div>'
                        info = info + '\n'
                        info = info + '                        </div>'
                        info = info + '\n'
                        presubword=subword                        
                        info = info + '                        <div class="portal-wrapper">'
                        info = info + '\n'
                        info = info + '                        <label for="' + keyword + subword + '">' + subword + imga + '</label>'
                        info = info + '\n'
                        info = info + '                        <input id="' + keyword + subword + '" class="on-off" type="checkbox"  />'
                        info = info + '\n'
                        info = info + '                        <div class="portal-box">'
                        info = info + '\n'
                else:
                    if presubword =='':
                        info = info + '                    </div>'
                        info = info + '\n'
                        info = info + '                </div>'
                        info = info + '\n'
                        prekeyword=keyword
                        presubword=subword
                        info = info + '                        <div class="portal-wrapper">'
                        info = info + '\n'
                        info = info + '                        <label for="' + keyword + '">' + keyword + imga + '</label>'
                        info = info + '\n'
                        info = info + '                        <input id="' + keyword + '" class="on-off" type="checkbox"  />'
                        info = info + '\n'
                        info = info + '                        <div class="portal-box">'
                        info = info + '\n'
                    else:
                        info = info + '                            </div>'
                        info = info + '\n'
                        info = info + '                        </div>'
                        info = info + '\n'
                        info = info + '                    </div>'
                        info = info + '\n'
                        info = info + '                </div>'
                        info = info + '\n'
                        prekeyword=keyword
                        presubword=subword
                        info = info + '                        <div class="portal-wrapper">'
                        info = info + '\n'
                        info = info + '                        <label for="' + keyword + '">' + keyword + imga + '</label>'
                        info = info + '\n'
                        info = info + '                        <input id="' + keyword + '" class="on-off" type="checkbox"  />'
                        info = info + '\n'
                        info = info + '                        <div class="portal-box">'
                        info = info + '\n'
    if presubword=='':
        info = info + '                    </div>'
        info = info + '\n'
        info = info + '                </div>'
        info = info + '\n'
        info = info + '            </div>'
        info = info + '\n'
    else:
        info = info + '                            </div>'
        info = info + '\n'
        info = info + '                        </div>'
        info = info + '\n'
        info = info + '                    </div>'
        info = info + '\n'
        info = info + '                </div>'
        info = info + '\n'
        info = info + '            </div>'
        info = info + '\n'
    info = info + '            <!-- // 导航首页 -->\n'
    fwinfo('../../index/main.html', info)
