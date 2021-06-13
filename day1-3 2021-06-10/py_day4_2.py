"""
输入两个正整数计算它们的最大公约数和最小公倍数

Version: 0.1
Author: rebecca
Date: 2018-03-01
"""
a, b= input("please input two positive integer: ").split()
a = int(a)
b = int(b)
for i in range(min(a,b),0,-1):
    if a%i==0 and b%i==0:
        print("%d is the highest common factor of %d and %d" %(i,a,b))
        print("%d is the least common multiple of %d and %d" %(a*b//i,a,b))
        break
