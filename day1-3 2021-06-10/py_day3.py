"""
PJ1: 英制单位英寸与公制单位厘米互换
"""

number = float(input("Please enter a length: "))
unit = input('please indictate the length unit: ')
if unit == "in" or "inch":
    print('the length you given is %.1f inch, which equal to %.1f cm' %(number, number/2.54))
else:
    print('the length you given is %.1f cm, which equal to %.1f inch'  %(number, number*2.54))
"""
PJ2: 百分制成绩转换为等级制成绩。
要求：如果输入的成绩在90分以上（含90分）输出A；
80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；
60分-70分（不含70分）输出D；60分以下输出E。
"""

score=float(input('please enter a score: '))
if score >= 90:
    grade='A'
elif score >= 80:
    grade='B'
elif score >= 70:
    grade='c'
elif score >= 60:
    grade='D'
else:
    grade='E'
print("The grade of %.1f is: "% score, grade)

"""
练习3：输入三条边长，如果能构成三角形就计算周长和面积。
"""
a,b,c= input('please enter 3 number: ').split()
a = float(a)
b = float(b)
c = float(c)

if a+b > c and a+c > b and b+c >a:
    cir = a+b+c
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print('the perimeter of the triangle is', cir ,'and the area is', area)
else:
    print('these three sides can not form a triangle')
   
