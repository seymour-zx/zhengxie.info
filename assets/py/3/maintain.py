#!/usr/bin/python
# -*- coding: UTF-8 -*-


def maintain():
    from lib.steps import assembly
    assembly()
    

if __name__ == '__main__':
    from lib.settings import get_ready
    if get_ready():
        print('get_ready')
        maintain()
else:
    pass