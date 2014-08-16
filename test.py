#!/usr/bin/python

import mymod

print mymod.__name__
print mymod.S
print 'S is: {0}'.format(mymod.S)
print 'S is: %s, age is : %d' % (mymod.S , 18)

print '{0:_^11}'.format('hello')
print r'raw string\n'

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
print dir(mymod)

#dict 
print '\n===== dict test =======\n'
for key,value in mymod.D.items():
#for key,value in mymod.D.iteritems():
    print key, value

#get value by key
for key,value in mymod.D.items():
    if  value == 25:
        print key

print '\n===== slice test =======\n'
print mymod.L[::2]
print mymod.L[::3]
print mymod.L[::-1]

print '\n===== references test =======\n'
ll = mymod.L
print ll
del mymod.L[0]
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

print '\n===== io test =======\n'

inputs = raw_input('what do you want?\n')
if  inputs in ['money', 'girl', 'happy']:
    print 'good idea'
else:
    print 'you wanna :', inputs

f = open('./test.txt', 'w')
f.write('hi txt')
f.close()
