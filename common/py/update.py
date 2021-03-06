#!/usr/bin/python
# -*- coding: UTF-8 -*-
from package_update.ready import ready
import os
import urllib.request
import webbrowser
import time
from package_update.ready import ready
from package_update.reset import reset
from package_update.tool import folders
from package_update.refresh import refresh
from package_update.htmls import htmls


if __name__ == '__main__':
    if ready():
        print('执行程序', 'update.py')
        # 当前格林尼治时间
        gmtime = time.gmtime()
        datetime = time.strftime('%Y-%m-%dT%H:%MZ', gmtime)
        # 通用的txt/html组件存放于此文件夹：
        txtfolder = '../txt/'
        # 重置，例如通用的素材，footer.txt
        reset(txtfolder, gmtime)
        # 读取文件夹目录
        htmlfolders, indexfolders = folders('directory.txt', txtfolder)
        # 制作index.html
        for n in range(len(htmlfolders)):
            htmls(htmlfolder=htmlfolders[n], indexfolder=indexfolders[n], txtfolder=txtfolder, gmtime=gmtime)
        # 刷新，例如目录、sitemap.xml
        refresh(txtfolder)


else:
    print('导入模块', 'update.py')

