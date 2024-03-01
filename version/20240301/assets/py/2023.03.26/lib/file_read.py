#!/usr/bin/python
# -*- coding: UTF-8 -*-


def file_read(file, folder=""):
    import os
    from lib.set_path import set_path
    # 读取信息
    path = set_path(file, folder)
    if not os.path.exists(path):
        info = '\n'
        print('信息读取失败:\n', os.path.abspath(path))
    else:
        with open(path, 'r', encoding='utf-8') as fr:
            info = fr.read()
    return info


if __name__ == '__main__':
    pass
else:
    pass