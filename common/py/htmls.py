# coding: utf-8
from ready import ready
from info_self import div_main, info_title, info_keywords, info_description, info_link
from tool import linkpath, fwinfo, frinfo
import time
import os
import webbrowser

def htmls(htmlfolder, indexfolder, txtfolder, gmtime):
# 制作index.html
    if True: # 记录初次创建的时间
        path = linkpath('gmtime.txt', indexfolder)
        if not os.path.exists(path):
            fwinfo(path, str(int(time.mktime(gmtime))))
        else:
            gmtime = time.localtime(int(frinfo('gmtime.txt', indexfolder)))
    info = ''
    # 通用
    info = info + frinfo('head.txt', txtfolder)
    if True:
        info = info + info_title('title.txt', indexfolder, txtfolder)
    if True:
        info = info + info_keywords('keywords.txt', indexfolder, txtfolder)
    if True:
        info = info + info_description('description.txt', indexfolder, txtfolder)
    # 通用
    info = info + frinfo('author.txt', txtfolder)
    if True:
        info = info + info_link('link.txt', indexfolder, txtfolder, htmlfolder)
    # 通用
    info = info + frinfo('body.txt', txtfolder)
    # 通用
    info = info + frinfo('header.txt', txtfolder)
    if True:
        info = info + div_main(htmlfolder, indexfolder, txtfolder, gmtime)
    # 通用
    info = info + frinfo('footer.txt', txtfolder)
    # 通用
    info = info + frinfo('html.txt', txtfolder)
    if True: # 写入信息'index.html'
        html = linkpath('index.html', htmlfolder)      
        with open(html, 'w', encoding='utf-8') as fw:
            fw.writelines(info)
    if True: # 在默认浏览器中打开html文件        
        html = os.path.abspath(html)
        # webbrowser.open(html,new = 0, autoraise=True)


if __name__ == '__main__':
    if ready():
        print('执行程序', 'htmls.py')
else:
    print('导入模块', 'htmls.py')