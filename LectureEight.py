# Lecture Eight : OOP's

"""
To map with real world scenarios, we started suing objects in code.
This is called Object Oriendted programming

procedural -> functional -> oops

Class - Class is a blueprint for creating objects
Objects - The objects is an entity that has a state and behavior associated with it
    
"""
# ["sushant", 98,]  
# class Student:
#     name="Sushant"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s1.name)

# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand )

"""
__int__ function 
Constructor : All classes have a function called __init__(), which is always executed
when the class is being initiated.

default constructors
def __init__(self):
    pass



"""
# class Student:
#     # name="Sushant"

#     # default constructors
#     def __init__(self):
#         pass

#     # parameterized constructors
#     # def __init__(self, fullname):
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in Database...")

# s1 = Student("Karan",90)
# print(s1.name, s1.marks)
# s2 = Student("Arjun", 89)
# print(s2.name, s2.marks)

"""
The self parameter is a referrence to the current instance of the class, and is used to
accuess variables that belong to the class.
 
"""

"""
Class and Instance Attributes

class attributes - common for all objects

precedance :

obj attr > class attr

"""

class Student:
    college_name = "BIT Mesra"
    name = "anonymous" #class attribute

    def __init__(self, name, marks):
        self.name = name #obj attr > class attr
        self.marks = marks
        print("adding new student in database...")

s1 = Student("Sushant", 98)
