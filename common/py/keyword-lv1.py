#!/usr/bin/python
# -*- coding: UTF-8 -*-
from package_update.ready import ready
from package_update.tool import frinfo, fwinfo


if ready():
    list = ['中央媒体']
    info = ''
    for i in range(60):
        name = str(i)
        if i < len(list):
            name = list[i]        
        info = info + '\n'
        info = info + '            <div class="keyword-lv1">'
        info = info + '\n'
        info = info + '                <label for="' + name + '">'+ name + '</label>'
        info = info + '\n'
        info = info + '                <div class="ad">  </div>'
        info = info + '\n'
        info = info + '                <input id="' + name + '" name="box_lv1" type="radio" />'
        info = info + '\n'
        info = info + '                <div class="box_lv1">'
        info = info + '\n'
        info = info + '\n'
        info = info + '                </div>'
        info = info + '\n'
        info = info + '            </div><!-- / ' + name + ' -->'
        info = info + '\n'
    fwinfo('./txt/keyword-lv1.txt', info)
    fwinfo('../../index/main.html', info)