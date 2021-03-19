#!/usr/bin/python
# -*- coding: UTF-8 -*-
from package_update.ready import ready
from package_update.tool import frinfo, fwinfo



if ready():
    path = './csv/utf-8.csv'
    info = ''
    with open(path, 'r', encoding='utf-8') as fr:
        lines = fr.readlines()
        # print(lines)
        for i in range(1,len(lines)):
            line = lines[i]
            line = line.strip()
            site, word, other = line.split(',', 2)
            # print(site, word)
            a = '<a href="' + site + '">' + word +'</a>\n'
            # print(a)
            info = info + a
    fwinfo('./txt/site_anchor.txt', info)