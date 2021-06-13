"""
打印三角形图案

Version: 0.1
Author: rebecca
"""
row = int(input("please input the number of row: "))
for i in range(row):
    for j in range(i+1):
        print("*", end=" ") #end='' control to be in the same line "end is equal to empty string"
    print() # I want to change line for every single line. so I just print nothing and print have a property that print something just change a line


for i in range(row):
    for j in range(row):
        if j< row-i-1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

for i in range(row):
    for j in range(row-i):
        print(" ",end=" ")
    for j in range(row-i+1,row+i):
        print("*",end=" ")
    print()
