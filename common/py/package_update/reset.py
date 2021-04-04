#!/usr/bin/python
# -*- coding: UTF-8 -*-
from package_update.ready import ready
import time
from package_update.tool import linkpath, fwinfo, frinfo

def footer(txtfolder, gmtime):
# 'footer.txt'
    file = 'footer.txt'
    infolist = []
    infolist.append('\n    <!-- 页底 -->')
    infolist.append('\n    <footer>')
    infolist.append('\n')
    infolist.append('\n        <!-- 正协信息客栈（zhengxie.info）版权所有 -->')
    infolist.append('\n        <div class="in-footer-box">')
    infolist.append('\n            正协信息客栈（zhengxie.info）版权所有')
    infolist.append('\n        </div>')
    infolist.append('\n')
    infolist.append('\n        <!-- Copyright © 2020-2021 All Rights Reserved. -->')
    infolist.append('\n        <div class="in-footer-box">')
    infolist.append('\n            Copyright © 2020-2021 All Rights Reserved')
    infolist.append('\n        </div>')
    infolist.append('\n')
    infolist.append('\n        <!-- 举报中心 -->')
    infolist.append('\n        <div class="in-footer-box">')
    infolist.append('\n            <a href="https://www.12377.cn/" target="_blank">违法信息举报中心</a>&nbsp;&nbsp;')
    infolist.append('\n            <a href="https://www.12321.cn/" target="_blank">垃圾信息举报中心</a>')
    infolist.append('\n        </div>')
    infolist.append('\n')
    infolist.append('\n        <!-- 上次维护 -->')
    infolist.append('\n        <div class="in-footer-box">')
    infolist.append('\n            |&nbsp;&lt;&nbsp;')
    infolist.append('\n            上次维护：<time datetime="')
    infolist.append(time.strftime('%Y-%m-%dT%H:%MZ', gmtime))
    infolist.append('">')
    infolist.append(time.strftime('%Y-%m-%dT%H:%MZ', gmtime))
    infolist.append('</time>')
    infolist.append('\n            &nbsp;&gt;&nbsp;|')
    infolist.append('\n        </div>')
    infolist.append('\n')
    infolist.append('\n    </footer>')
    info = ''
    for i in range(len(infolist)):
        info = info + infolist[i]
    path = linkpath(file, txtfolder)
    fwinfo(path, info)

def reset(txtfolder, gmtime):
# 重置，例如通用的素材，footer.txt
    footer(txtfolder, gmtime)


if __name__ == '__main__':
    if ready():
        print('执行程序', 'reset.py')
else:
    print('导入模块', 'reset.py')