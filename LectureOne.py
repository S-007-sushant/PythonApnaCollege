"""
Apna Collage

machine <-- Translator <-- code 
       (compiler/Interpretor)
What is python?
1. Python is simple and easy
2. Free and open source
3. High Level Langauage
4. Developed by Guido van Rossum
5. Portable 
"""
print("Hello World") # output

"""Python character set

letters - A to Z, a to z
digit - 0 to 9
special symbols - + - * / etc
white spaces - Blank Space, tab, carriage return, new line, formfeed
"""
print("Sushant is my name.","My age is 23")
print(23)
print(23+58)

"""
Variable :
A variable is a name given to a memory location in a program

"""
name = "Sushant"
age = 23
price = 24.99
print(name,age,price)
first_name = "Sushant"
print("My name is :",name)

# = is assign operator
"""
uppercase, lowercase letter and underscore(_)
myVariable, variable_1, variable_for_print
1variable (not valid), variable1 (valid)

"""
print(type(name))
print(type(age))
print(type(price))

"""
Data Types
1. Integer : +ve, -ve 0

2. String - name, hello '' or "" also in """

name1 = 'sk'
name2 = "sk"
name3 = """sk"""

"""
3. Float 3.99, 2.5

4. Boolean : True and False
old = True

5. None 
"""


"""
Key words

and as assert break class continue def 
del elif else except finally False for 
from global if import in is lambda nonlocal 
None not or pass raise return True try with while yield

Python is a case sensitive

"""
# Print Sum
number_1 = 2000
number_2 = 50000
sum = number_1 + number_2
difference = number_1 - number_2
print(sum)

# single line Comments 
""" Multi Line Comments """

"""
Types of Operator : 
An operator is a symbol that performs a certain operation between operands.
"""
# 1. Airthmetic Operator (+ - * / % **exponential)
a = 4
b = 2
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplicaiton
print(a/b) #division with decimal
print(a//b) #division without decimal
print(a%b)  # to find reminders
print(a**b) # exponential

#2. Relational / Comparision Operator (==, !=, >, <, >=, <=)
print("Relational/ Comparision Operator : ")
c = 50
d = 20
print(c == d) #False
print(c !=d) #True
print(c>d) #True
print(c>=d) #true
print(c<d) # false
print(c<=d) #false


#3. Assignment Operators ( =, +=, -=, *=, /=, %=, **=)
num = 10
num+=10
print(num)


#. Logical Operators (not, and, or)
parent = True
print(parent)
print(not parent)

"""
Type conversion
Coverting one type to another

Type Conversion and Type Casting

Type conversion : 
interpertor do automatically

Type Casting: manually doing coversion

1.

"""
a = "2"
b = 4.25

sum = int(a)+b
print("Type coversion", sum)


"""
User input in Python
"""

# first_name = float(input("Enter your age : "))
# print("hello,",first_name, type(first_name))
# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# marks = float(input("Enter your marks"))
# print(name, age, marks)

"""# Write a program to input 2 numbers and print thier sum : 
number_1 = int(input("Enter first number:"))
number_2 = int(input("Enter second number:"))
# sum = number_1+number_2
print("sum =", number_1+number_2)"""

"""
write a program to input side of a square and print its area
"""
# side = float(input("enter the side of square:"))
# print("area of square:", side*side,"cm square")

"""
Write a program to input 2 floating point numbers and print thier average
"""
# number_1 = float(input("enter number 1:"))
# number_2 = float(input("enter number 2:"))
# print((number_1+number_2)/2)

"""
Write a program to input 2 int numbers a and b, print True if a is greater
than or equal to b. if not print False"""
a = int(input("first number: "))
b = int(input("second number: "))
print(a>=b)



