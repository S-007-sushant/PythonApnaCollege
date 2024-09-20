# #Loops in Python | While and for loops
# # Loops are used to repeat instructions.
# """
# while Loops  

#     while condition :
#         #some work
# """
# # x = 10
# # while x<=20:
# #     print(x)
# #     x+=1
# # print(x)

# # i = 5
# # while i>=1:
# #     print(i)
# #     i-=1

# #1. Print numbers fromm 1 to 100
# """x = 1
# while x<=100:
#     print(x)
#     x+=1"""

# #2. Print numbers from 100 to 1
# """x = 100
# while x>=1:
#     print(x)
#     x-=1"""

# #3. Print the multiplication table of a number n.
# """x = 1
# while x<=10:
#     print("3 x",x," = ",3*x)
#     x+=1"""

# #4. print the elements of the following list using a loop
# # [1,4,9,16,25,36,49,64,81,100]
# x = 1
# sroots = []
# while x <=10:
#     sroots.append(x*x)
#     x+=1
# print(sroots)
# trootrs = (1,4,9,16,25,36,49,64,81,100)

# idx = 0
# findNumebr = int(input("Enter number to search"))
# while idx <len(trootrs):
#     if(findNumebr == trootrs[idx]):
#         print("at index",idx)
#     idx+=1


#Breaks and Continue

# Break : used to terminate theloop when encountered.
# Continue : terminates execution in the current iteration and continues execution of the loop
# i = 1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1

# i = 0
# while i<=10:
#     if(i%2 == 0):
#         i+=1
#         continue
#     print(i)
#     i+=1


# Loops in Python
# loops are used for sequential traversal. For traversing list, string tuples

# for Loops 

"""
for el in list:
    some task
"""
# list = [1,2,3]
# for el in list:
#     print(el)

# # for loops with else
# print("\nFor Loops with else\n")
# for el in list:
#     print(el)
# else: print("End")

# print the elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]
# list = [1,4,9,16,25,36,49,64,81,100]
# for i in list:
#     print(i)
# idx = 0
# num = 36
# for i in list:
#     if(num == i):
#         print("at index: ",idx)
#         break
#     idx+=1

# Range
# range() : Range functions return a sequence of numbers, starting from 0
# by default, and increments by 1 (by default), and stops before a specified number.
# range(start?,stop,step?)
# for el in range(5):
#   print(el)
# for el in range(1,5):
#   print(el)
# for el in range(1,5,2):
#   print(el) 

# print(range(5))
# seq = range(5)
# for i in seq:
#     print(i)

# for i in range(10): #range(stop)
#     print(i)

# for i in range(2,10): #range(start, stop)
#     print(i)

# for i in range(2,10,2): #range(start,stop,step)
#     print(i)

#print numbers from 1 to 100 
# for i in range(1,101):
#     print(i)

#print numbers from 100 to 1
# for i in range(100,0,-1):
#     print(i)

# print the multiplication table of a number n
# number = int(input("Enter a number for multiplication: "))
# for i in range(1,11):
#     print(number*i)

# Pass statement
# pass is a null statement that does nothing. It is used as a placeholder for futer code
# for el in range(10):
#     pass

# write a program to find the sum of first n numbers 
#BY USING FOR LOOP
# number = int(input("Enter the first n number: "))
# sum = 0
# for i in range(number+1):
#     sum = sum+i
# print("total sum : ",sum)
# BY USING WHILE LOOP
# number = int(input("Enter the first n number: "))
# sum = 0
# i = 0
# while(i<=number):
#     sum = sum+i
#     i+=1
# print("total sum",sum)

# write a program to find the factorial of first n numbers (using for)
# BY USING FOR LOOP
# number = int(input("Enter the first n number: "))
# fact = 1
# for i in range(1,number+1):
#     fact = fact * i
# print("Factorial of ",number," is : ",fact)
# BY USING WHILE LOOP
# number = 3
# fact = 1
# i = 1
# while i<=number:
#     fact*=i
#     i+=1
# print("factorial :",fact)