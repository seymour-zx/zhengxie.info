#!/usr/bin/python
# -*- coding: UTF-8 -*-


def get_ready():
    import os
    cmdfolder = 'D:\\Program Files\\VS Code'
    pyfolder = 'D:\\Program Files\\VS Code\\zhengxie.info\\assets\\py'
    print(os.getcwd())
    if os.getcwd()==cmdfolder or os.getcwd()==pyfolder:
        os.chdir(pyfolder)
        return True
    else:
        print('......运行目录错误，运行中断！......')
        return False
        

def settings():
    pass


if __name__ == '__main__':
    print('执行程序', 'settings.py')
else:
    print('导入模块', 'settings.py')