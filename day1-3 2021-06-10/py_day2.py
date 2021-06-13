"""
PJ1:华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。
"""

f=float(input('Please enter a temp in Fahrenheit: '))
c=(f-32)/1.8
print('The temp %.1f Fahrenheit is %.1f Celsius' %(f, c))

"""
PJ2:输入圆的半径计算计算周长和面积。
"""

r=float(input('please enter a radiu: '))
s=2*3.14*r
a=3.14*r*r
print("the circumference is %.2f, and the area is %.2f" % (s,a))

"""
练习3：输入年份判断是不是闰年。
"""

year1=int(input('Please enter a year: '))
is_leap= year1%4==0 and year1%100!=0 or \
    year1%400==0
print(is_leap)

year2=int(input('Please enter a year: '))
if year2%4==0 and year2%100!=0 or year2%4000==0:
    print("%d is a leap year" % year2)
else:
    print("%d is not a leap year" % year2)