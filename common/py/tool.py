# coding: utf-8
from ready import ready
import os
import urllib.request



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



if __name__ == '__main__':
    if ready():
        print('执行程序', 'tool.py')
else:
    print('导入模块', 'tool.py')