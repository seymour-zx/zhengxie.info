#!/usr/bin/python
# -*- coding: UTF-8 -*-


def get_ready():
    import os
    cmdfolder = 'D:\\301 VS Code'
    pyfolder = 'D:\\301 VS Code\\zhengxie.info\\assets\\py'
    print(os.getcwd())
    if os.getcwd()==cmdfolder or os.getcwd()==pyfolder:
        os.chdir(pyfolder)
        return True
    else:
        print('......运行目录错误，运行中断！......')
        return False


if __name__ == '__main__':
    print('执行程序', 'get_ready.py')
else:
    print('导入模块', 'get_ready.py')