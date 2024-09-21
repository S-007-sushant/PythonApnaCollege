# Functions in Python
# Block of statement that perform a specific task
# Example: 
"""
def func_name(param1, param2,...) :
    some work
    return val

func_name(arg1,arg2,..) function call 
"""
# def calc_sum(a,b):
#     sum = a + b
#     print(sum)
#     return sum
# # print(calc_sum(5,6))
# calc_sum(10,20)

# print average of 3 number
# def average(a,b,c):
#     return round((a+b+c)/3,2)
# print(average(98,97,95))

#Functions :
"""
Built in Functions and User Define functions
print() : built in function
len() : built in function
type() : built in function
range() : buikt in function 
"""
# print("Sushant", end=" ") 
# print("raj")

# Defualt Parameter
# def cal_prod(a = 1,b = 1):
#     print(a*b)
#     return a * b
# cal_prod( )

# def cal_prod(a, b = 2):
#     print(a*b)
#     return a * b
# cal_prod(1)

# Let's Practise
#1. write a program to print the length of a list (list is the parameter)
# def lengthFinder(array):
#     len = 0
#     for i in array:
#         len+=1
#     print(len)
#     return len
# def findlength(array):
#     print(len(array))


# num = [1,8,5,6,9,0,9,75,10,12]
# lengthFinder(num)

#cities = ["ranchi","mumbai","delhi","kolkata", "Bangalore"]
# findlength(cities)

#2. Write a function to print the elements of a list in a single line.(list is the parameter)
# cities = ["ranchi","mumbai","delhi","kolkata", "Bangalore"]
# def printlinebyline(arrays):
#     for i in arrays:
#         print(i, end=", ")    
# printlinebyline(cities)

#3. Write a function to find the factorial of n (n is the parameter)
# by using for loop
# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
#     return fact
# factorial(4)

# # by using while loop
# def Wfactorial(n):
#     fact = 1
#     i = 1
#     while i<=n:
#         fact *=i
#         i+=1
#     print(fact)
# Wfactorial(4)

# write a function to convert USD to INR
# def usdtoinr(price):
#     inr = 83
#     print(price, "USD = ", price*inr,"INR")

# usdtoinr(73)
    
# write a function to check a numebr is odd then print odd and if even then print even
# def oddeven(num):
#     if(num%2 == 0):
#         print("Even")
#     else : print("Odd")
# oddeven(32)

# Recursion
# when a function calls itself repeatedly
"""
def show(n):
    if(n==0):
        return 
    print(n)
    show(n-1)
"""

"""
Recursion factorial

def fact(n):
    if(n == 0 or n == 1)
        return 1
    else : return n * fact(n-1) 
"""

#1. wrire a recursive function to calculate the sum of first n natural numebr:

# def sumofn(n):
#     if(n==0):
#         return 0
#     return sumofn(n-1) + n

# print(sumofn(3))

# write a recursive function to print all elements in a list
# def arrayPrint(array,idx):
#     if(idx == len(array)):
#         return 
#     print(array[idx])
#     arrayPrint(array,idx+1)
# list = ["mango", "grapes", "banana", "strawberies"]
# arrayPrint(list,idx = 0)
