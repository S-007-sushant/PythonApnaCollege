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

#Conditional Statement at 30:38
