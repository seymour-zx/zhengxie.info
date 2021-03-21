#!/usr/bin/python
# -*- coding: UTF-8 -*-
from package_update.ready import ready
from package_update.tool import frinfo, fwinfo



if ready():
    mydict = {'导航网站':'<a href="https://zhengxie.info/"><img src="./common/image/favicon.ico">正协信息客栈</a>'}
    path = './csv/utf-8.csv'
    info = '\n'
    info = info + '            <!-- 导航首页 -->'
    info = info + '\n'
    info = info + '            <div id="portal-box" class="portal-box">'
    info = info + '\n'
    keywords = '第一关键词'
    with open(path, 'r', encoding='utf-8') as fr:
        lines = fr.readlines()
    for i in range(1,len(lines)):
        line = lines[i]
        line = line.strip()
        site, word, keyword, other = line.split(',', 3)
        if keywords==keyword:
            a = '                    <a href="' + site + '">' + word +'</a>'
            info = info + a
            info = info + '\n'
        else:            
            if not i==1:
                info = info + '                    </div>'
                info = info + '\n'
                info = info + '                </div>'
                info = info + '\n'
            keywords=keyword
            info = info + '                <div class="portal-wrapper">'
            info = info + '\n'
            if True:                        
                if keyword in mydict:
                    label = '                    <label for="' + keyword + '">' + keyword + mydict[keyword] + '</label>'
                else:
                    label = '                    <label for="' + keyword + '">' + keyword + '</label>'
            info = info + label
            info = info + '\n'
            check = '                    <input id="' + keyword + '" class="on-off" type="checkbox"  />'
            info = info + check
            info = info + '\n'
            info = info + '                    <div class="portal-box">'
            info = info + '\n'
            a = '                    <a href="' + site + '">' + word +'</a>'
            info = info + a
            info = info + '\n'    
    info = info + '                    </div>'
    info = info + '\n'
    info = info + '                </div>'
    info = info + '\n'
    info = info + '            </div>'
    info = info + '\n'
    info = info + '            <!-- // 导航首页 -->'
    fwinfo('./txt/newmain.txt', info)
    fwinfo('../../index/main.html', info)
    
