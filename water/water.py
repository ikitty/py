#!/usr/bin/python

import urllib
import re
import os
import pprint

'''
get pic of water story
'''
#data
base_url = 'http://tieba.baidu.com/p/1663301114?pn='
down_dir = './pic/'

star_list_file = './star_list.data'

import pickle
#one default arguments I gived, the other arguments should be given?
def save_data(data_path , data):
    f = open(data_path, 'wb' )
    pickle.dump(data, f)
    f.close()

def load_data(data_path):
    try:
        f = open(data_path, 'rb' )
        result = pickle.load(f)
        return result
    except(IOError, EOFError):
        print data_path, ' does not exist.'
        return False


#basic module
def wget(url, proxy=None):
    f = urllib.urlopen(url, proxies = proxy )
    return f.read()

def wfile(f, content=''):
    '''
    A simple module for writting file
    '''
    rf = open(f, 'w')
    rf.write(content)
    rf.close()

#get all star
def getAllStar(url):
    ret = []
    count = 1
    for key in xrange(1,6):
        url_content = wget(url + str(key))
        #<cc><div id="post_content_20848306019" class="d_post_content j_d_post_content ">005 name<br><br><img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=f05d33c3252dd42a5f0901a3333a5b2f/0dfed32a6059252df35d7bae349b033b5ab5b9dd.jpg" width="420" height="584"><br>desp<br></div><br></cc>

        result = re.findall(r'<cc><div[^>]*>[^<]*(?:<br>)*<img[^>]*src="(.*.jpg)"[^>]*>', url_content)

        for i,v in enumerate(result):
            ret.append({'src': result[i], 'order': count})
            count += 1

    save_data(star_list_file, ret )

    print 'star list saved in: ', star_list_file
    return ret

#try to load data
star_urls = load_data(star_list_file)
if  star_urls:
    print 'got star list from Local data'
else:
    print 'starting to get star list data.'
    star_urls = getAllStar(base_url)
    print 'got star list from Remote service'
#type:list
#pprint.pprint(star_urls, width=10, indent=2)
#exit(1)

import sys
rp_count = 0
def rp_fn(blocknum, blocksize, totalsize):
    global rp_count
    percent = 20.0 * blocknum * blocksize / totalsize
    percent = 20 if int(percent)>20 else int(percent)
    #time.sleep(1)
    for i in range(percent - rp_count):
        print '>',
    rp_count = percent

def fetchImg(star_data, target):
    if not os.path.exists(target):
        os.mkdir(target, 0744)

    for single in star_data:
        url = single['src']
        fname = str(single['order']) + '.jpg'

        print '\n';
        print '{0:-^39}'.format('Fetch ' + target + '/' + fname );
        urllib.urlretrieve(url, target + fname, rp_fn)

        #del star_data[index]
        print '\nGot this group, Now fetch next group \n';


fetchImg(star_urls, down_dir)
