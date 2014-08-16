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

def wget(url):
    f = urllib.urlopen(url)
    return f.read()

if __name__ == '__main__':
    print 'mymod ' , __version__
