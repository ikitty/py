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

print '\n===== x. find largest factor of a number =======\n'
hugeNo = 600851475143
def factors(n):
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
    return fs + [n]
x = factors(hugeNo)
print x

def Euler3(n=600851475143):
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

print Euler3(27)

print '\n===== 5. find latest common multiple =======\n'

import math
def isPrime(n):
    """
    
    """
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
    """get muti num of n
    n=num1*num2...*numx for num1...numx are all prime numbers
    """
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
    #print(primelists)
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
 
print(getMutil(getLeastCommonMutible([8,12,20])))
