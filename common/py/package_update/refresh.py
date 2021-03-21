#!/usr/bin/python
# -*- coding: UTF-8 -*-
from package_update.ready import ready
import time
from package_update.tool import linkpath, fwinfo, frinfo
import os
from package_update.htmls import htmls

def unit(txtfolder):
# 更新目录
    n = 999
    htmlfolder = '../../unit/' + str(n) +'/'
    info = ''
    info = info + '\n            <table class="contents"><!-- 目录列表 -->\n'
    while not n==0:
        if os.path.exists(htmlfolder):
            indexfolder = linkpath('index', htmlfolder)
            # info = info + '                <tr>\n                    <td nowrap="nowrap">'
            info = info + '                <tr>\n                    <td class="date">'
            gmtime = time.localtime(int(frinfo('gmtime.txt', indexfolder)))
            gmtime = time.strftime('%Y-%m-%d', gmtime)
            info = info + gmtime
            info = info + '</td>\n'
            info = info + '                    <td class="contents"><a href="https://zhengxie.info/unit/' + str(n) +'/"'
            # info = info + ' title="" target="_blank">'
            info = info + ' title="">'
            info = info + frinfo('title.txt', indexfolder)
            info = info + '</a></td>\n                </tr>\n'            
        n = n - 1
        htmlfolder = '../../unit/' + str(n) +'/'
    info = info + '            </table><!-- // 目录列表 <table class="contents"> -->'
    path = linkpath('main.html', '../../base/sitemap/index/')
    fwinfo(path, info)
    htmls(htmlfolder='../../base/sitemap/', indexfolder='../../base/sitemap/index/', txtfolder=txtfolder, gmtime=time.gmtime())

def refresh(txtfolder):
# 刷新，例如目录、sitemap.xml
    unit(txtfolder)

if __name__ == '__main__':
    if ready():
        print('执行程序', 'refresh.py')
else:
    print('导入模块', 'refresh.py')