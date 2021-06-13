"""
check a input number is a prime number or not 

Version: 0.1
Author: rebecca
Date: 2021-06-18

number = int(input('Please input a positive integer: '))
count = 0
if number < 2:
    number = int(input("Please reinput a positive integer："))
else:
    for i in range(2,number):
        if number % i == 0:
            count +=1
    if count == 0:
        print("%d is a prime number" % number)
    else:
        print("%d is not a prime number" % number)
"""


"""
check a input number is a prime number or not 

答案 method: 1.先开根号，计算需要除以的次数
2. 然后再一个个除以各个数字，
3.用一个是true和false来做储存和计算，这样用时间少，
而我自己是用count来算数字，如果数字计算其实是会变的存储量很大的，运行时间也很长，同时他用了一个break这样就不会继续消耗计算时间了

Version: 0.2
Author: rebecca
Date: 2021-06-18
"""
from math import sqrt
number = int(input('Please input a positive integer: '))
count = True
end = int(sqrt(number))
if number < 2:
    print("The number you input is neither prime nor composite numbers")
    number = int(input("Please reinput a positive integer："))
else:
    for i in range(2,end+1):
        if number % i == 0:
            count = False
            break
    if count:
        print("%d is a prime number" % number)
    else:
        print("%d is not a prime number" % number)

"""
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
"""