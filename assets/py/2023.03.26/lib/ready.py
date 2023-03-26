#!/usr/bin/python
# -*- coding: UTF-8 -*-


def ready(cmd1,cmd2,cmd3):
    import os
    cmd = os.getcwd()
    if cmd == cmd1 or cmd == cmd2 or cmd == cmd3 :
        print(cmd)
        os.chdir(cmd3)
        return True
    print(cmd3)
    import time    
    time.sleep(5)


if __name__ == '__main__':
    pass
else:
    pass