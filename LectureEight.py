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


"""
class Student:
    name="Sushant"
    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in Database...")

s1 = Student("Karan")
print(s1.name)