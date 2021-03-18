from ready import frinfo, fwinfo, checkpath

if checkpath(): 
    info = '            <div class="container">'
    info = info + '\n'
    for i in range(24):
        info = info + '                <div class="wrapper">'
        info = info + '\n'
        info = info + '                    <label for="box_'
        n = str(i+1)
        s = n.zfill(3)
        info = info + s + '">测试一下</label>'
        info = info + '\n'
        info = info + '                    <input type="radio" name="lv_1" id="box_' + s + '">'
        info = info + '\n'
        info = info + '                    <div class="box">'
        info = info + '\n'
        info = info + '                        <a href="  " title="  " >  </a><br />'
        info = info + '\n'
        info = info + '                        <a href="  " title="  " >  </a><br />'
        info = info + '\n'
        info = info + '                        <a href="  " title="  " >  </a><br />'
        info = info + '\n'
        info = info + '                        <a href="  " title="  " >  </a><br />'
        info = info + '\n'
        info = info + '                    </div>'
        info = info + '\n'
        info = info + '                </div>'
        info = info + '\n'
    info = info + '            </div>'
    fwinfo('temp.txt', info)
