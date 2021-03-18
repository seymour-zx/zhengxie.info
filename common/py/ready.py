# coding: utf-8
import os
import urllib.request
import webbrowser
import time

def ready():
# 检查路径
    cmdfolder = 'D:\\Workspace'
    pyfolder = 'D:\\Workspace\\html\\zhengxie.info\\common\\py'
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


if __name__ == '__main__':
    if ready():
        print('执行程序', 'ready.py')
else:
    print('导入模块', 'ready.py')