#!/usr/bin/python
print '\n===== python challenge test =======\n'

print '\n===== channel =======\n'

import zipfile, re

cmts, count, f = [], '90052', '%s.txt'
myfile = zipfile.ZipFile('channel.zip')
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

