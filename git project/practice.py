""""""
import datetime
import random
import os
print("!!!Welcome to guessing game!!!")
x=datetime.datetime.now()
print("Game started at",end="")
print(x.strftime("%c"))
name=input("Enter your name:")
age=input("Enter age:")
with open("C:/Users/ayush/python/git project/task.txt","w+") as f1:
    f1.write("\nPlayer name:")
    f1.write(name)
    f1.write("\nPlayer age:")
    f1.write(age)
    f1.seek(0)
    print(f1.read())

x1=datetime.datetime.now()

i=random.randint(1,100)
print("Random number is",i)

print("Game completed  in:",end="")
print(x1.strftime("%c"))