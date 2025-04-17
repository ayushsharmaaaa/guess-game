""" def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def prod(a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b
def triangle(h,b):
    return 0.5*h*b """


""" while(True):
    a=float(input("Enter a number :"))
    b=float(input("Enter other number:"))
    try:
        print(a/b)
        exit(0)
    except ValueError:
        print("Please enter a valid number")
        continue
    except ZeroDivisionError:
        print("Please do not input zero as divisor")
        continue """

""" import os
current_dir=os.getcwd()
print(current_dir)
p1=os.listdir()
print(p1)
p2="www.txt"
os.remove(p2) """
""" 
class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

s1=student("Ayush",20,89)
print(s1.name,s1.age)
print(s1.marks) """


""" a=int(input("Enter no. of rows: "))
for i in range(a,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
 """
""" print("1")
print("2 2")   
print("3 3 3")
print("4 4 4 4")   
print("5 5 5 5 5") """

""" rows=int(input("Enter number of rows:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print() """

print("    *    ")
print("   ***   ")
print("  *****  ")
print(" ******* ")
print("*********")

for i in range(0,6):
    for j in range(0,i+1):
        for k in range(i-2,0,-1):
            print(" ")
            print("*",end="")
    print()


 