#!/usr/bin/python
# -*- coding: UTF-8 -*-


def ready(cmd1,cmd2,cmd3):
    import os
    cmd = os.getcwd()
    if cmd == cmd1 or cmd == cmd2 or cmd == cmd3 :
        print('\n\n')
        print('当前运行环境:\n',cmd)
        os.chdir(cmd3)
        print('运行环境切换到:\n',cmd)
        print('\n\n')
        return True
    import time
    time.sleep(5)
    pass


if __name__ == '__main__':
    pass
else:
    pass