#!/usr/bin/python

import urllib
import re
import os
import pprint

#data
base_url = 'http://www.ttkzm.com/html/pic/'
base_host = 'http://www.ttkzm.com/'
down_dir = './pic/'

star_list_file = './star_list.data'
each_star_file = './star_single.data'

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

def formatNum(num, digit = 4):
    '''
    format number to string with specify digit
    i.e format 1 to '0001'
    '''
    num2str = str(num)
    if len(num2str) >= digit:
        return str(num)
    else:
        return '0'*(digit - len(num2str)) + num2str

#test
#print formatNum(0)

#get all star
def getAllStar(url):
    '''
    return {list} i.e ['urlx', 'urly']
    '''
    url_content = wget(url)
    #<UL class="zx_channel_ul"> <LI><A title="x" href="/html/pic/2014/8/26215440.html" target="_blank"><IMG alt="x" src="/uploadfile/small/20140826dc174538126/228x342.jpg" onerror="src='/images/err_pic.jpg'"></A> <DIV class="chan_text"> <P><A href="/html/pic/2014/8/26215440.html" target="_blank">x</A></P> <DIV class="time_user_div"><A style="color: rgb(153, 153, 153);">2014/08/26</A> </DIV></DIV></LI>

    result = re.findall(r'<LI>[^>]*href="(.*.html)".*', url_content)

    for i,v in enumerate(result):
        result[i] = base_host + v

    #save data
    #y don't need set star_list_file as global
    save_data(star_list_file, result )
    print 'star list saved in: ', star_list_file
    return result

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

#find img rule for all star
def findImgRule(urls):
    '''
    return {list} of {dict}
    e.g. [{img: img_url, dir: number, current: number}]
    '''
    result = []
    for url in urls:
        url_content = wget(url)
        #<p style="text-align: center"><img onload="size(this)" alt="" src="/uploadfile/201408/20/4C234321823.jpg" />

        imgs = re.findall(r'onload="size\(this\)"[^>]*src="([^>]*\.jpg)".*?', url_content)
        for i,v in enumerate(imgs):
            if i == 0:
                imgs_year = v.split('/')
                dir_year = str(imgs_year[2]) + str(imgs_year[3])
            imgs[i] = base_host[:-1] + v

        result.append({'img_url': imgs, 'dir':dir_year, 'current': 0})
        
    save_data(each_star_file, result )
    print 'star Rule saved in: ', each_star_file
    return result

#try to load img rule of each star 
star_rule = load_data(each_star_file)
if  star_rule:
    print 'got star Rule from Local data'
else:
    print 'starting to get star Rule data.'
    star_rule = findImgRule(star_urls)
    print 'got star Rule from Remote service'
pprint.pprint(star_rule, width=10)
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

    for index, single in enumerate(star_data):
        #img_prefix = os.path.dirname(single['img_url']) + '/'
        #python is a strong type language
        #start = int(single['current'])
        #end = int(single['total']) + 1

        #for order in range(start, end):
        for url in single['img_url']:
            sub_dir = target + single['dir'] + '/'
            if not os.path.exists(sub_dir):
                os.mkdir(sub_dir, 0744)

            names = url.split('/')
            fname = names[-1]
            print '\n';
            print '{0:-^39}'.format('Fetch ' + single['dir'] + '/' + fname );
            urllib.urlretrieve(url, sub_dir + fname, rp_fn)

        #del star_data[index]
        print '\nGot this group, Now fetch next group \n';


fetchImg(star_rule, down_dir)
