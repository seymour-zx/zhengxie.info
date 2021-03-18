# coding: utf-8
from ready import ready
import time
from tool import linkpath, fwinfo, frinfo




def footer(txtfolder, gmtime):
# 'footer.txt'
    file = 'footer.txt'
    infolist = []
    infolist.append('\n    <footer>')
    infolist.append('\n        <!-- 上次维护 -->')
    infolist.append('\n        <div>')
    infolist.append('\n            |&nbsp;')
    infolist.append('\n            &lt;&nbsp;')
    infolist.append('\n            上次维护：')
    infolist.append(time.strftime('%Y-%m-%dT%H:%MZ', gmtime))
    infolist.append('\n            &nbsp;&gt;')
    infolist.append('\n            &nbsp;|')
    infolist.append('\n        </div>')
    infolist.append('\n        <!-- /上次维护 -->')
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