#!/usr/bin/python
# -*- coding: UTF-8 -*-
from package_update.ready import ready
from package_update.tool import frinfo, fwinfo



if ready():
    path = './txt/dict.txt'
    mydict = {}
    with open(path, 'r', encoding='utf-8') as fr:
        lines = fr.readlines()
    for i in range(0, int(len(lines)/2)):
        dictkey = lines[i*2].strip()
        dictvalue = lines[i*2+1].strip()
        mydict[dictkey] = dictvalue
    # mydict = {'导航网站':'<div class="imga"><img src="https://zhengxie.info/common/image/favicon.ico"><a href="https://zhengxie.info/">正协信息客栈</a></div>'}
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
        site, word, keyword, favicon, other = line.split(',', 4)
        if keywords==keyword:
            img = '<img src="' + favicon + '">'
            a = '                    <a href="' + site + '">' + word +'</a>'
            imga = '                    <div class="imga">' + img + a + '</div>'
            info = info + imga
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
            img = '<img src="' + favicon + '">'
            a = '                    <a href="' + site + '">' + word +'</a>'
            imga = '                    <div class="imga">' + img + a + '</div>'
            info = info + imga
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
    
