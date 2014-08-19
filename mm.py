#!/usr/bin/python

import sys
import os
import re
import urllib

__version__ = 1

#define some test var
S = 'Python is a powerful programming language, and easy to learn'
L = ['Kevin', 'Nick', 'LJ', 'Brain']
T = ('smart', 'creative', 'passion')
D = {'name': 'BackstreetsBoys', 'age': 25, 'type': 'loving'}

def rfile(f):
    '''
    A simple module for reading file
    '''
    rf = open(f, 'r')
    text = rf.read()
    rf.close()
    return text

def wfile(f, content=''):
    '''
    A simple module for writting file
    '''
    rf = open(f, 'w')
    rf.write(content)
    rf.close()
    print 'some content has been written'

def wget(url, proxy=None):
    f = urllib.urlopen(url, proxies = proxy )
    return f.read()

if __name__ == '__main__':
    print 'mm ' , __version__
