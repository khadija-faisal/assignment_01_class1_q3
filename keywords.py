#  ASSIGNMENT_NO_01 

# -python data types and keywords;

# -python keywords:

# what is python keywords?
#Python keywords are reserved words in Python that have special meanings and are part of the language’s syntax. You cannot use these words as variable names or identifiers.

# below down 10 most commonly used keywords.

# 1 - and
#A logical operator that returns True if both operands are true.
# understand with Example:
if (5 > 3) and (2 < 4):
    print("both operators are true.")

# 2 - as
# used to create an alias white importing a module or use to import module as a different name.
# understand with Example:
import math as m 
print("square roots of 12 is", m.sqrt(16))

# 3 - break 
# used to exit a loop or a statement block.
# understand with Example:
for i in range(15):
    if i == 5:
        break
    print(i)

# 4- class
# used to define a class.
# understand with Example:
class Mobile:
    def __init__(self, name,):
        self.name = name

ans= Mobile("Samsung")
print("my fav phone brand is",ans.name)

# 5 - continue
# used to skip the current iteration of a loop and continue with the next iteration.
# understand with Example:
for i in range(10):
    if i == 5:
        continue  # Skip printing when i equals 5.
    print(i)

# 6 - def
# used to define a function.
# understand with Example:
def name():
    print("my name is khadija")
name()

# 7 - del
# used to delete objects.
# understand with Example:
num = 10
print("print before its deletion",num)
del num
# print("print after its deletion",num) #throw error

# 8 - elif
# stand for "else if" in conditional statements.
# understand with Example:
num = 15
if num > 5:
    print(f"{num} is greater then 5")
elif num < 20:
    print(f"{num} is less then 20")
else:
    print("nothing")

# 9 - lambda
# used to create small anonymous functions.
# understand with Example:
addition = lambda a, b: a + b
print("Sum is",addition(4, 7))

# 10 - return
# used to exit function  and optionally passes back a value
# understand with Example:
def greeting(name):
    return "assalam o alaikum " + name
print(greeting("Sir Asharib"))

# i just share ten most commonly used keywords in python. although i'm also learning and understand new advanced keyword async match and case and many more.




       