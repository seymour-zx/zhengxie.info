from ready import frinfo, fwinfo, checkpath

if checkpath():
    path = 'sitepath.txt'
    info = ''
    # message = ''
    with open(path, 'r', encoding='utf-8') as fr:
        lines = fr.readlines()
        for line in lines:
            # line = line.strip()
            s1, s2, s3, s4 =line.split(', ',3)
            print(s1.strip(), s2.strip(), s3.strip())
            if not s3.find('\n')==-1:
                s3=''
            # s = '<a href="' + s1 + '" title="' + s3 + '">' + s2 +'</a>\n'  
            s = '<a href="' + s1 + '">' + s2 +'</a>\n'  
            print(s)
            info = info + s
            # message = message + s1 + ', ' + s2 + ', ' + s3 + ', \n' 
    fwinfo('new.txt', info)
    # fwinfo('old.txt', message)