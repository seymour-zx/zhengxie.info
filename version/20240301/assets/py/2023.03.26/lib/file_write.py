#!/usr/bin/python
# -*- coding: UTF-8 -*-


def file_write(file, info):
    import os
# 写入信息
    if os.path.exists(file):
        print('覆写信息:\n', os.path.abspath(file))
    else:
        print('新写信息:\n', os.path.abspath(file))
    with open(file, 'w', encoding='utf-8') as fw:
        fw.writelines(info)
    pass


if __name__ == '__main__':
    pass
else:
    pass