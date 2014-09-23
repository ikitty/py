#!/usr/bin/python
#python challenge code

print '\n===== 6. channel: collect comment of each file in zip =======\n'

def channel():
    import zipfile, re
    cmts, count, f = [], '90052', '%s.txt'
    myfile = zipfile.ZipFile('shannel.zip')
    rStr = 'Next nothing is (\d+)'

    while True:
        ff = f % count
        cmts.append(myfile.getinfo(ff).comment)
        try:
            count = re.search(rStr, myfile.read(ff)).group(1)
        except:
            print myfile.read(ff)
            break
    print ''.join(cmts)
#channel()

print '\n===== 7. oxygen: get info by analysising gray color =======\n'

def oxygen():
    import re, Image

    i = Image.open("oxygen.png") 
    row = [i.getpixel((x, 50)) for x in range(0, i.size[0], 7)]
    ords = [r for r, g, b, a in row if r == g == b]

    print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords))))))
#oxygen()

print '\n===== 8. intergrity: bz compress =======\n'
#todo

print '\n===== 9. good: connect the dots =======\n'
#todo
