#!/usr/bin/python

print '\n===== clear bad file =======\n'

import os
def clearBadFile(folder):
    for dirname, dirnames, filenames in os.walk(folder):
        #for subdirname in dirnames:
            #print os.path.join(dirname, subdirname)

        for filename in filenames:
            if  '.DS_Store' != filename:
                each_file = os.path.join(dirname, filename)
                each_size = os.path.getsize(each_file)/1000
                if  each_size < 100:
                    os.remove(each_file)
                    print each_file , ' has been deleted.'


        # Advanced usage:
        # editing the 'dirnames' list will stop os.walk() from recursing into there.
        if '.git' in dirnames:
            dirnames.remove('.git')

clearBadFile('./pic/')


