#!/usr/bin/python
# -*- coding: UTF-8 -*-


def maintain():
    pass


if __name__ == '__main__':
    from lib.settings.get_ready import get_ready
    if get_ready():
        print('get_ready')
        maintain()
else:
    pass