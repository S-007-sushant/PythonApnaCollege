#List and Tuple in Python
"""
A built in data type that stores set of values
It can store elements of different types (integer, floaat, string,etc)
example : 
marks = [87, 64, 33, 95, 76]

Student = ["Karan", 85, "Delhi"]

Student[0] = "Arjun"

len(student) #return length

"""
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))

#string are immutable in python 
#list are mutable in python.

student = ["karan", 85, 17, "Delhi"]
#List Slicing
# list_name[starting_index:ending_index]

marks = [94, 95, 66, 45]
print(marks[:-3])
"""
#List methods
list = [2,1,3]
print("acctual list",list)
list.append(4) # adds one element at the end
print("append :",list)
list.sort() # sort in ascending order
print("sort ascending :",list)
list.sort(reverse=True) #sorts in descending order
print("sort descending :",list)
list.reverse() #reverse list
print("list reverse :",list)
list.insert(2,5) #list.insert(index, element) insert element at index
print("list insert at index 2 ",list)
list.remove(1) # removes first occurrence of element
print(list)
list.pop() #list.pop(idc)removes element at idx
print(list)
list.pop(1)
print(list)
"""
#Tuples in Python
# a built in data type that lets us create immutable sequence of value
"""tup = (87,64,33,44,55)
print(tup,type(tup), tup[2])
tupp = (1)
tupp = (1,2,3,3,2)
print(tup[1:3])
print(tupp.index(1)) #return index of the first occurrence
print(tupp.count(2))"""

#practice
#1. write a program to ask the user to enter name of their 3 favorite
# movies and store them in a list

"""movieList = []
movieName1 = input("Enter a first Movie")
movieList.append(movieName1)
movieName2 = input("Enter second movie")
movieList.append(movieName2)
movieName3 = input("Enter third movie")
movieList.append(movieName3)
movies = []
movies.append(input("Enter 1st movie"))
movies.append(input("Enter 2st movie"))
movies.append(input("Enter 3st movie"))

print(movieList)"""

# 2. write a program to check if a list contains a palindrome of elements 

"""listName = [1,2,1]
copyListName = listName.copy()
copyListName.reverse()
if(listName == copyListName):
    print("Its a Parlinderom")
else: print("Not Palindrome")"""

#3. write a program to count the number of student with the "A" 
#  grade in the following tuple
gradTuple = ["C","D","A","A","B","B","A"]
print(gradTuple.count("A"))

#4. Store the above values in a list and sort them from "A to D"
gradList = []
for i in gradTuple:
    gradList.append(i)
print(gradList)
gradList.sort(reverse=True)
print("sorted :", gradList)

 






 