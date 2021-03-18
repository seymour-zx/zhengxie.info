# coding: utf-8
import os
import urllib.request
import webbrowser
import time









def info_title(file, indexfolder, txtfolder):
# 'title.txt'
    info = '\n'
    infolist = []
    infolist.append('    <title>')
    path = linkpath(file, indexfolder)
    if os.path.exists(path):
        infolist.append(frinfo(file, indexfolder))
    else:
        fwinfo(path, '')
        # infolist.append('')
    infolist.append(frinfo(file, txtfolder))
    for i in range(len(infolist)):
       info = info + infolist[i]
    return info

def info_keywords(file, indexfolder, txtfolder):
# 'keywords.txt'
    info = '\n'
    infolist = []
    infolist.append(frinfo(file, txtfolder))
    path = linkpath(file, indexfolder)
    if os.path.exists(path):
        infolist.append(frinfo(file, indexfolder))
    else:
        fwinfo(path, '华朝颐亲王, 正协信息客栈')
        infolist.append('华朝颐亲王, 正协信息客栈')
    infolist.append('" />')    
    for i in range(len(infolist)):
       info = info + infolist[i]
    return info

def info_description(file, indexfolder, txtfolder):
# 'description.txt'
    info = '\n'
    infolist = []
    infolist.append(frinfo(file, txtfolder))
    path = linkpath(file, indexfolder)
    if os.path.exists(path):
        infolist.append(frinfo(file, indexfolder))
    else:
        fwinfo(path, '')
        # infolist.append('')
    infolist.append('" />')    
    for i in range(len(infolist)):
       info = info + infolist[i]
    return info

def info_link(file, indexfolder, txtfolder, htmlfolder):
# 'link.txt'
    info = ''
    path = linkpath(file, indexfolder)
    if os.path.exists(path):
        info = info + frinfo(file, indexfolder)
    else:
        rel_ico = os.path.relpath("../image/favicon.ico", htmlfolder)
        rel_ico = urllib.request.pathname2url(rel_ico)
        rel_css = os.path.relpath("../css/mystyle.css", htmlfolder)
        rel_css = urllib.request.pathname2url(rel_css)
        infolist = []        
        infolist.append('\n    <link href="')
        infolist.append(rel_ico)
        infolist.append('" rel="shortcut icon" type="image/x-icon" />\n        <!--调用网页图标-->')
        infolist.append('\n    <link href="')
        infolist.append(rel_css)
        infolist.append('" rel="stylesheet" type="text/css" />\n        <!--调用css样式-->\n')
        for i in range(len(infolist)):
            info = info + infolist[i]
        fwinfo(path, info)
    return info









def folders(directory, txtfolder):
# 读取文件夹目录
    htmlfolders = []
    indexfolders = []
    path = linkpath(directory, txtfolder)
    with open(path, 'r', encoding='utf-8') as fr:
        lines = fr.readlines()
        for line in lines:
            line = line.strip()
            htmlfolders.append(line)        
            path = linkpath('index', line)
            if not os.path.exists(path):
                os.makedirs(path)
                print('......新建目录：\n', os.path.abspath(path))
            indexfolders.append(path)
    return htmlfolders, indexfolders

def checkpath():
# 检查路径
    cmdfolder = 'D:\\Workspace'
    pyfolder = 'D:\\Workspace\\Html\\zhengxie.info\\common\\py'
    if os.getcwd()==cmdfolder or os.getcwd()==pyfolder:
        print('......运行目录正确！......')
        # 运行目录必须切换至存放py文件的文件夹
        os.chdir(pyfolder)
        return True
    else:
        print('......运行目录错误！......')
        print('......cmd命令目录：')
        print(cmdfolder)
        print('......py存放于文件夹：')       
        print(pyfolder)
        print('......当前运行目录：')
        print(os.getcwd())
        return False

def fwinfo(file, info):
# 写入信息
    if os.path.exists(file):
        print('覆写信息:\n', os.path.abspath(file))
    else:
        print('新写信息:\n', os.path.abspath(file))
    with open(file, 'w', encoding='utf-8') as fw:
        fw.writelines(info)

def frinfo(file, folder=""):
# 读取信息
    path = linkpath(file, folder)
    if not os.path.exists(path):
        info = '\n'
        print('信息读取失败:\n', os.path.abspath(path))
    else:
        with open(path, 'r', encoding='utf-8') as fr:
            info = fr.read()
    return info


def linkpath(children, parents=''):
# 相对链接路径
    path = os.path.join(parents, children)
    path = urllib.request.pathname2url(path)
    if not os.path.exists(path):
        print('......目标不存在:\n', os.path.abspath(path))
    return path


def reset_footer(file, txtfolder, gmtime):
# 'footer.txt'      
    infolist = []
    infolist.append('    </div>')
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

if __name__ == '__main__':
    print('执行程序', 'ready.py')
else:
    print('导入模块', 'ready.py')