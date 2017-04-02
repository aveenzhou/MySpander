#coding=utf-8
'''
Created on 2017-3-26

@author: chowpeng
'''

#质因数分解法：把每个数分别分解质因数，再把各数中的全部公有质因数提取出来连乘，所得的积就是这几个数的最大公约数。
#from math import *
#from operator import mul
##判断n是否为素数
#def isPrime(n):
#    if n <= 1:
#        return 0
#    m = int(sqrt(n))+1
#    for x in range(2,m):
#        if n%x == 0:
#            return 0
#    return 1
##利用递归分解n,返回n的质因数列表
#def getPrimeList(n):
#    temp=[]
#    def bprime(n):
#        if isPrime(n):
#            temp.append(n)
#        else:
#            x = 2
#            while x <= int(n/2):
#                if n%x == 0:
#                    temp.append(x)
#                    return bprime(n/x)
#                x = x + 1
#    bprime(n)
#    return temp


#def getMaxCD(n,m):
#    n_primelst=getPrimeList(n)
#    print n_primelst
#    m_primelst=getPrimeList(m)
#    print m_primelst
#    c_primelst=list(set(n_primelst) & set(m_primelst))
#    print c_primelst
#    return reduce(mul, c_primelst)
#
#
#print getMaxCD(24,60)



#def getMaxCD(m,n):
#    return m if n==0 else getMaxCD(n,m%n)
#
#
#print getMaxCD(10,2)
#
#def bubbleSort(lst):
#    flag=True
#    while flag:
#        flag=False
#        for i in range(len(lst)-1):
#            if lst[i]>lst[i+1]:
#                temp=lst[i]
#                lst[i]=lst[i+1]
#                lst[i+1]=temp
#                flag=True
#    return lst
    
import sys
class A(object):
    def __init__(self):
        print "A %s born" % str(hex(id(self)))
    def __del__(self):
        print "A delete %s" % str(hex(id(self)))
class B(object):
    def __init__(self):
        print "B %s born" % str(hex(id(self)))
    def __del__(self):
        print "B delete %s" % str(hex(id(self)))
#a=A()
#print sys.getrefcount(a)
#b=B()
#a.B=b
#b.A=a
#import gc
#import time
#
#def f3():
#  # print gc.collect()
#    c1= A()
#    c2= B()
#    c1.t=c2
#    c2.t=c1
#    del c1
#    del c2
#    print "lajilst",gc.garbage
#    print "collect:",gc.collect() #显式执行垃圾回收
#    print "lajilst",gc.garbage
#    time.sleep(10)
#if __name__ == '__main__':
#    gc.set_debug(gc.DEBUG_LEAK) #设置gc模块的日志
#    f3()

import weakref
class Man:
    def __init__(self, name):
            self.name = name
def callback(self):
    print "callback"
    
o=Man('Jim')
p=weakref.proxy(o,callback)
print p.name
o=None
print p.name
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
