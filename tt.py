#!/usr/bin/python
# coding:utf-8

import mm
import pprint

#print 'S is: {0}'.format(mm.S)
#print 'S is: %s, age is : %d' % (mm.S , 18)

#print '{0:_^11}'.format('hello')
#print r'raw string\n'

#global
g=1
def fn():
    global g
    g=2
    print g

fn()
print g

#default arg
def repeatStr(s, times = 2):
    print s*times

repeatStr('hi')
repeatStr('hi', 5)

def keyArg(a,b=0,c=0):
    print a, b, c
keyArg(b=2,a=3)

#varArg
def varArg(i, *num, **key):
    print i
    print num
    print key

varArg(10,1,2,3,a=1,b=2)

#dir
print '\n===== dir msg =======\n'
print dir(mm)

#dict 
print '\n===== dict test =======\n'
for key,value in mm.D.items():
#for k, v in enumerate(list):
#for key,value in mm.D.iteritems():
    print key, value

#get value by key
for key,value in mm.D.items():
    if  value == 25:
        print key

print '\n===== slice test =======\n'
print mm.L[::2]
print mm.L[::3]
print mm.L[::-1]

print '\n===== references test =======\n'
ll = mm.L
print ll
del mm.L[0]
print ll

lll = ll[:]
print lll
del ll[0]
print lll

print '\n===== class test =======\n'
class Person:
    def __init__(self, name):
        print name, 'has beed inited'
        self.name = name
    def say(self):
        print 'hi', self.name

p = Person('jack')
p.say()

print '\n===== trans code test =======\n'
def transCode(s):
    ret = ''
    for key in s:
        if ord(key) >= ord('a') and ord(key) <= ord('z'):
            od = ord('a') + (ord(key)+2 - ord('a'))%26
            ret += chr(od)
        else:
            ret += key
    print ret

s = 'a xyz apple '
transCode(s)

print '\n===== class var code test =======\n'

class Toy:
    #class var
    count = 0

    def __init__(self, name):
        self.name = name 
        # here use class. as prefix
        # also, we can use : self.__class__.count +=1
        Toy.count +=1

    def gone(self):
        print self.name, 'gone'
        # here use class. as prefix
        Toy.count -=1

    @classmethod
    def howmany(cls):
        print 'class count is: ', cls.count

toy1 = Toy('aa')
toy2 = Toy('bb')
Toy.howmany()
toy1.gone()
Toy.howmany()

print '\n===== class inheritance test =======\n'

class Girl:
    def __init__(self,name):
        self.name = name
        print name, 'inited'
    def show(self):
        print 'name is: %s ' % self.name

#notice ,remember pass base class as a arg
class Beautygirl(Girl):
    def __init__(self,name, leg):
        #first init base class
        Girl.__init__(self, name)
        #self point to ?
        self.leg = leg
        print 'beautygirl inited named:', self.name
    def show(self):
        Girl.show(self)
        print 'my leg is: %s ' % self.leg

bg1 = Beautygirl('michelle', 'white, long')
bg1.show()

mm.wfile('./test.txt', '\n'.join([mm.S]*3))
print mm.rfile('./test.txt')


print '\n===== pickle test =======\n'
import pickle

#use write and binary mode
f = open('./temp.data', 'wb' )
pickle.dump(mm.D, f)
f.close()

f = open('./temp.data', 'rb' )
getData = pickle.load(f)
print getData

print '\n===== unicode test =======\n'
import io

f = io.open('./text_cn.txt', 'wt', encoding = 'utf-8')
f.write(u'origin ascii code, \u8000\u8001')
f.close()
print  io.open('./text_cn.txt',  encoding = 'utf-8').read()

print '\n===== exception test =======\n'

#try:
    #inputs = raw_input('what do you want?\n')
#except (KeyboardInterrupt, EOFError):
    #print 'keyboardInterrupt or eofError'
#else:
    #print inputs
#finally:
    #print 'finally print, you will see it whatever'

print '\n===== with test =======\n'
with open('./test.txt') as f:
    for line in f:
        print line

print '\n===== project euler test =======\n'
x=0
for k in range(100):
    if  k % 3==0 or k%5 == 0:
        x += k
print x
print sum(key for key in range(1,100) if key%3==0 or key%5==0)



print '\n===== recursion test =======\n'

def xsum(v):
    #for 3 situation: define , structure
    #boundary, exit
    #condition
    #rule
    return 0 if v == 0 else xsum(v-1)+v

#python r deepth should less thn 1000
print xsum(100)

def fib(v):
    if v == 1 or v == 2:
        return 1
    else:
        #the rule
        return fib(v-2) + fib (v-1)

print fib(5)

print '\n===== temp test =======\n'
#str = mm.rfile('./str.txt')

proxies = {'http': 'http://proxy.tencent.com:8080'}

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
#url = 'http://www.baidu.com'
#str = mm.wget(url, proxies);
#print str

### solution for linkedlist
#import re
#baseurl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
#def testlinked(n):
    #count = 0
    #for key in range(401):
        #count +=1 
        #ss = mm.wget(baseurl + str(n), proxies)
        #_find = re.search('\d+', ss)
        #if _find:
            #n = _find.group()
            #print count, 'is', n
        #else:
            #print 'cannot find numer at :', n
            #n = raw_input(ss)
    #print 'loop to ', count

#x = 16044
#testlinked(x)

print '\n===== lambda test =======\n'
#anonymous function
_f = lambda x: x**2
print _f(2)
print map(lambda x: x**2, [1,2,3] )
print map(lambda x: x > 1 and x**2 or x +1, [1,2,3] )
print 1 and 'a' or 'b'
print 'a'.isalpha()

print '\n===== leetcode test =======\n'
def strReverse(s = ''):
    l = s.split(' ')
    l.reverse()
    return ''.join(l)
print 'x' + strReverse(' 1') +'x'


def reverseWords(s=''):
    import re
    s = s.strip()
    s = re.sub(r'\s+', ' ',s)
    if s == '':
        return ''
    else:
        l = s.split(' ')
        l.reverse()
        return ' '.join(l).strip()
print reverseWords('a bb   c')

print '\n===== fetch img test =======\n'


def load_data(data_path = './x.data'):
    f = open(data_path, 'rb' )
    try:
        result = pickle.load(f)
        return result
    except(EOFError):
        print 'pickle.load error'
        return False

def save_data(data_path , data):
    f = open(data_path, 'wb' )
    pickle.dump(data, f)
    f.close()

import urllib, pickle
myurl="http://www.pythonchallenge.com/pc/def/banner.p"
handle= urllib.urlopen(myurl)
object = pickle.load(handle)
handle.close()
for item in object:
    print "".join(i[0] * i[1] for i in item) #print characters

print '\n===== n-queens test =======\n'

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.res = []
        self.solve(n, 0, [-1 for i in xrange(n)])
        return self.res
     
    def solve(self, n, currQueenNum, board):
        if currQueenNum == n:
            oneAnswer = [ ['.' for j in xrange(n)] for i in xrange(n) ]
            for i in xrange(n): 
                oneAnswer[i][board[i]] = 'Q'
                oneAnswer[i] = ''.join(oneAnswer[i])
            self.res.append(oneAnswer)
            return
        # try to put a Queen in (currQueenNum, 0), (currQueenNum, 1), ..., (currQueenNum, n-1)
        for i in xrange(n):
            valid = True  # test whether board[currQueenNum] can be i or not
            for k in xrange(currQueenNum):
                # check column
                if board[k] == i: valid = False; break
                # check dianogal
                if abs(board[k] - i) == currQueenNum - k: valid = False; break
            if valid:
                board[currQueenNum] = i
                self.solve(n, currQueenNum + 1, board)

solution = Solution()
print solution.solveNQueens(4)

print '\n===== hyphen2underline test =======\n'

def hyphenTounderline(path = './index.htm'):
    htmlStr = mm.rfile(path)
    def rep(m):
        #print m.group(0)
        return m.group(0).replace('-', '_')

    retStr = re.sub(r'(id|class)="[^"]*"', rep, htmlStr)
    output = './index_output.htm'
    mm.wfile(output, retStr )

    #cssStr = mm.rfile('./style.css')
    #retStr = re.sub(r'\.[^{\n]*{', rep, cssStr)
    #output = './style_m.css'
    #mm.wfile(output, retStr )

print '\n===== flush test =======\n'
import sys, time
for xx in range(10) :
    sys.stdout.write('\r%s' % xx)
    sys.stdout.flush()

cnStr = '中文'
print cnStr
