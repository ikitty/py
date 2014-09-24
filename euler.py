#!/usr/bin/python
#euler project code

print '\n===== 1. sum for multiple =======\n'

def sumForMultiple():
    print sum([i for i in xrange(1000) if i % 3 == 0 or i % 5 == 0])
#sumForMultiple()

print '\n===== x. fibonacci =======\n'

def Fib():
    orglist = [1,1];
    f = -1
    maxV = 4000000
    while True:
        temp = orglist[f+1]+ orglist[f+2]
        if  temp < maxV:
            orglist.append(temp)
        else:
            break;
        f += 1

    print sum([i for i in orglist if i % 2 == 0])
#Fib()

print '\n===== x. find largest Factor =======\n'
hugeNo = 600851475143
def findFactor(n):
    fs = []
    while n % 2 == 0:
        fs += [2]
        n /= 2
    if n == 1:
        return fs
    f = 3
    while f * f <= n:
        if n % f == 0:
            fs += [f]
            n /= f
        else:
            f += 2
    resultArr = fs + [n]
    print resultArr[-1]
    #return resultArr[-1]
#findFactor(hugeNo)

def findFactor2(n=600851475143):
    ret = []
    i = 2
    while n > 1:
        while n % i == 0:
            ret.append(i)
            n /= i
        i += 1
        if i*i > n:
            if n > 1 : ret.append(n)
            break
    return ret
#print findFactor2()

print '\n===== 5. find latest common multiple =======\n'

import math
def isPrime(n):
    if n==2:
        return True
    if n==1 or n%2==0:
        return False
    p = int(math.sqrt(n))+1
    i = 3
    while i<p:
        if n%i==0:
            return False
        i+=2
    return True
         
def getMutiPrime(n):
    if n==2:
        resultlist = [2]
    else:
        list1 = [i for i in range(2,int(math.sqrt(n))+1) if isPrime(i)]
        #print(list1)
        resultlist=[]
        tmp = n
        while not isPrime(tmp) and tmp!=1:
            for i in list1:
                if tmp%i==0:
                    resultlist.append(i)
                    tmp=tmp//i
                    #print(tmp)
                    #print(resultlist)
        if tmp!=1:
            resultlist.append(tmp)
    return resultlist
 
def isMutillistFill(mutilLsit):
    for row in mutilLsit:
        if len(row)>0:
            return True
    return False
 
def getLeastCommonMutible(numList):
    primelists=[]
    set1=set({})
    mutilResult = []
    for i in numList:
        primelists.append(getMutiPrime(i))
        set1.update(set(i1 for i1 in getMutiPrime(i)))
    flag = True
    flag1 = False
    while flag:
        for i in set1:
            for row in primelists:
                if i in row:
                    row.remove(i)
                    flag1 = True
            if flag1:
                mutilResult.append(i)
                flag1 = False
        flag = isMutillistFill(primelists)
    #print(mutilResult)        
    return mutilResult
 
def getMutil(numList):
    result = 1
    for i in numList:
        result*=i
    return result
 
print(getMutil(getLeastCommonMutible([i for i in xrange(1,100)])))

#by chris
def getPrimeFactor(n):
    primfac = {}
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            dStr = str(d)
            primfac[dStr] = (primfac[dStr] + 1) if dStr in primfac else  1
            n /= d
        d += 1
    if n > 1:
       primfac[str(n)] = 1
    return primfac

def getLcm(seq):
    primfacs = []
    for i in seq:
        primfacs.append(getPrimeFactor(i))

    #print primfacs
    ret = {}
    for obj in primfacs:
        for attr in obj:
            if attr not in ret:
                ret[attr] = obj[attr]
            else:
                if obj[attr] > ret[attr]:
                    ret[attr] = obj[attr]

    #todo use reduce and lambda
    final = 1
    for p in ret:
        final *= math.pow(int(p), ret[p])

    print int(final)

getLcm([i for i in xrange(1,101)])

from timeit import timeit
solutionChris = """
import math
def getPrimeFactor(n):
    primfac = {}
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            dStr = str(d)
            primfac[dStr] = (primfac[dStr] + 1) if dStr in primfac else  1
            n /= d
        d += 1
    if n > 1:
       primfac[str(n)] = 1
    return primfac

def getLcm(seq):
    primfacs = []
    for i in seq:
        primfacs.append(getPrimeFactor(i))

    #print primfacs
    ret = {}
    for obj in primfacs:
        for attr in obj:
            if attr not in ret:
                ret[attr] = obj[attr]
            else:
                if obj[attr] > ret[attr]:
                    ret[attr] = obj[attr]

    final = 1
    for p in ret:
        final *= math.pow(int(p), ret[p])

    return int(final)

getLcm([i for i in xrange(1,100)])
"""
print 'use_chris:', timeit(solutionChris,  number=100)
    
print '\n===== 5. find latest common multiple By Recursion =======\n'

#TODO check timestart and timeend

def getLcmByRecursion(seq):
    def gcd(a, b):
        r = a % b
        if r:
            return gcd(b, r)
        else: 
            return b

    def lcm(a,b):
        return a * b/ gcd(a,b)

    def lcmAll(seq):
        return reduce(lcm, seq)

    print lcmAll(seq)

seq = [i for i in xrange(1,11)]
getLcmByRecursion(seq)

solution = '''
def getLcmByRecursion(seq):
    def gcd(a, b):
        r = a % b
        if r:
            return gcd(b, r)
        else: 
            return b

    def lcm(a,b):
        return a * b/ gcd(a,b)

    def lcmAll(seq):
        return reduce(lcm, seq)

    lcmAll(seq)

seq = [i for i in xrange(1,100)]
getLcmByRecursion(seq)
'''
print 'use_recursion:', timeit(solution,  number=100)

print '\n===== x. check Palindrome =======\n'

def palindrome():
    def checkPalindrome(n):
        n = str(n)
        le = len(n)
        mid_pos = le/2
        part1 = n[:mid_pos]
        if le % 2 != 0:
            mid_pos += 1
        part2 = n[mid_pos:]
        if part1 == part2[::-1]:
            return True
        else:
            return False

    x = 999
    y = 999
    count = 0
    ret = []
    retObj = {}
    while x > 100:
        while y > 100:
            z = x * y
            if checkPalindrome(z):
                retObj[z] = [x, y]
                ret += [z]
                break
            y -= 1
        x -= 1
        count += 1
        y = 999 - count
    print max(ret)

#palindrome()
