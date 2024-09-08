"""
String: 
string is data type that stores a sequence of characters.
"hello"+"world"
"""
str1 = "this is a string"
str2 = 'ApnaCollege'
str3 = """This is also a string"""

"""
why three string, because some times we need to print the aposthropy
in our code or string
"""

str1 = "This is a string.\nwe are creating it in python"
print(str1)

#Concatenation
# "hello"+"world" = "helloworld"

str1 = "sushant"
str2 = "raj"
final_string = str1+str2
print(final_string)

#Length of str
print("length of the string :",len(str1))

#Indexing
#apna_College
#0123456789
name = "Sushant_Raj"
chh = name[1]
# name[7] = "t"
print(chh,name)

#Slicing
#accessing parts of a string
str = "ApnaCollege"
print("Sliced string:",str[1:4])
str4 = "Apple"
print(str4[-4:])

#String Function
str = "i am a coder and i am a super man"
print("string function")
print(str.endswith("er")) # returen true if string ends with substr
print(str.capitalize()) # capitalize 1st charecter
print(str.replace("am","was")) #str.replace(old,new) replaces all occurrence of old with new 
print(str.find("c")) # str.find(word) returns 1st index of 1st occurrence
print(str.count("am")) # counts the occurrence of substr in the string

"""Practice Time """
#1. write a program to input user's first name and print its length
# firstName = input("Enter first name :")
# print("Length of the String:",len(firstName))

#2. write a program to find the occurrence of '$' in a string
str = "This is the $ string which counts the $ in this statement $"
print("this is the count of $",str.count("$"))

#Conditional Statement at 
#1. if-elif-else (SYNTAX)

"""
if(condition):
    statement1
elif(condition):
    statement2
else:
    statement
"""
"""age = 17
if(age>=18):
    print("can vote")
else:
    print("can't vote")

light = "green"
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("lood")
else:print("go")
"""
# marks = int(input("Enter marks in math: "))13
# technique 1
# if(marks>=90):
#     grade = "A"
# elif(marks>=80 and marks<90):
#     grade = "B"
# elif(marks>=70 and marks<80):
#     grade = "C"
# else : grade = "F"

#technique 2
"""if(marks<70):
    grade = "F"
elif(marks<80):
    grade = "C"
elif(marks<90):
    grade = "B"
else : grade = "A"

print("Student marks is : ",grade)"""

#Nesting: if under if
age = 34
if(age>=18):
    if(age>=80):
        print("Can't drive")
    print("can drrive")
else:
    print("connot drive")


"""
practice time

"""
#1. write a program to check if a nunber entered by the user is odd or even
# number = int(input("Enter a number: "))
# if(number%2==0):
#     print("Even Number")
# else: print("Odd")

#2. write a program to find the greatest of 3 numbers entered by the users
# a = int(input("Enter first number : "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if(a>b and a>c):
#     print("a is greater number",a)
# elif(b>a and b>c):
#     print("b is greater number",b)
# else: print("c is greater number",c)

#3. write a program to checkk if a number is multiple of 7 or not
number = int(input("Enter a number : "))
if(number%7==0):
    print("The number is divisible by 7: ",number)
else: print("The number is not divisible by 7: ",number)
