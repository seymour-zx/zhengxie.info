#!/usr/bin/python
# -*- coding: UTF-8 -*-


def html_catalog():
    from lib.set_path import set_path
    html_folder = '../../public/catalog2'
    index_folder = set_path('index', html_folder)
    txt_folder = set_path('txt', index_folder)
    # path = set_path('index.txt',html_foler)
    # print(path)
    # from lib.file_write import file_write
    # file_write(path,'good boy !')

    # # 当前格林尼治时间
    # gmtime = time.gmtime()
    # datetime = time.strftime('%Y-%m-%dT%H:%MZ', gmtime)

    from lib.file_read import file_read
    info = ''
    info = info + file_read('1.txt', txt_folder)

    info = info + """            <table class="contents"><!-- 目录列表 -->"""
    for i in range(0,10):
        num = str(i)
        info = info + """
        <tr>
                        <td class="contents"><a href="https://zhengxie.info/unit/"""

        
        info = info + num

        info = info + """/" title="">测试100</a></td>
                            <td class="date">2023-03-12</td>
                        </tr>
                        """
    info = info + """ </table><!-- // 目录列表 <table class="contents"> --> """










    info = info + file_read('2.txt', txt_folder)

    # 写入信息'index.html'
    if True:
        html = set_path('index.html', html_folder)      
        with open(html, 'w', encoding='utf-8') as fw:
            fw.writelines(info)

    # 在默认浏览器中打开index.html
    if True:
        import os
        html = os.path.abspath(html)
        import webbrowser
        webbrowser.open(html,new = 0, autoraise=True)


if __name__ == '__main__':
    from lib.ready import ready
    cmd1 = 'C:\\WINDOWS\system32'
    cmd2 = 'D:\\301 VS Code'
    cmd3 = 'D:\\301 VS Code\\zhengxie.info\\assets\\py\\2023.03.26'
    if  ready(cmd1,cmd2,cmd3) :
        html_catalog()
        pass
    else:
        pass
else:
    pass