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


 