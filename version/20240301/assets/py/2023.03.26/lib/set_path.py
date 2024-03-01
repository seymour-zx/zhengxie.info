#!/usr/bin/python
# -*- coding: UTF-8 -*-


def set_path(child, parent=''):
    import os
    import urllib.request
    # 相对链接路径 relative path
    # 链接 \ 或 /
    path = os.path.join(parent, child)
    # 统一转为 /
    path = urllib.request.pathname2url(path)
    # 如果目标路径不存在，则报错
    if not os.path.exists(path):
        print('错误报告！目标路径不存在:')
        print(os.path.abspath(path))
        # a = input('!是否创建文件夹？ yes/no ')
        # if not a == 'no' :
        #     print('创建:\n',path)
        #     os.makedirs(path)
    else:
        print('目标路径正确:')
        print(os.path.abspath(path))
    return path


if __name__ == '__main__':
    pass
else:
    pass