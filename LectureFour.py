# # Lecture Four : Dictionary and set in python
# """"
# Dictionnaries are used to store data value in key:value pairs
# they are unordered, mutable (changeable) and don't allow duplicate keys
# ex : 
# dict = {
#     "name": "Sushant"
#     "cgpa": 9.6
#     "marks" : [98,97,94],
# }
# """
# # info = {
# #     "name":"sushant raj",
# #     "subject": ["python","C","Java"],
# #     "topics": ("Dict","set"),
# #     "learning":"coding",
# #     "age": 53,
# #     "is_adult":True,
# #     "marks":84
# # }
# # print(info["name"])
# # info["name"] = "Sushant Raj"
# # info["college"] = "BIT Mesra"
# # print(info)

# null_dict = {}
# null_dict["name"] = "ApnaCollege"
# print(null_dict)

# #Nested Dictionaries
# # we can create nested dictionaries also
# student ={
#     "name":"Sushant Raj",
#     "subjects": {
#         "phy":97,
#         "chem":88,
#         "math":90
#     }
# }
# print(student["subjects"]["phy"])

# #Dictionary Methods
# # 1. myDict.keys() return all keys
# # 2. myDict.values() return all values
# # 3. myDict.items() returns all (key, value), pairs as tuples
# # 4. myDict.get("key") return the key according to value
# # 5. myDict.update(newDict) inserts the specified items to the dictionary.

# print(list(student.values()))

# # print(len(list(student.values())))
# print(list(student.items()))
# pairs = list(student.items())

# print(student.get("name")) #will not give error if the key is wrong
# print(student["name"]) # will give error when parameter not find

# student.update({"city":"mumbai", "age":24})
# print(student)

# #Set in pythons
# print("\nSets in Python\n")
# # set is the collection of the unordered items
# # Each element in the set mush be unique and immutable.

# # nums = {1,2,3,4}
# # set2 = {1,2,2,2}
# #repeated elements stored only once, soit resolved to {1,2}
# null_set = set()

# collection = {1,2,2,2,"hello", "world", "world","4"}
# print(len(collection))
# print(type(collection))
# print(null_set)

# #Set Methods 
# #1. set.add(el) adds an element
# #2. set.remove(el) removes the element 
# #3. set.clear() empties the set
# #4. set.pop() removes a random value
# #5. set.union(set2) combines both set values and return new
# #6. set.intersection(set2)

# null_set.add(1)
# null_set.add(2)
# null_set.add(2)
# null_set.add(3)
# null_set.add(4)
# null_set.remove(2)
# collection.clear()
# null_set.pop()
# print(null_set)
# print(collection)
# set = {1,2,3}
# set2 = {3,4,5}
# print(set.union(set2))
# print(set.intersectionw(set2))

# Practice Time
#1. store following word meaning in a python dictionary:
"""
table : "a piece of furniture", "list of facts & figures"
cat : "a small animal"
"""
# Uncomment for answer
# dictionary = {
#     "cat": "a small animal",
#     "table":["a piece of furniture", "list of facts & figures"]
# }
# print(dictionary)

#2. You are given a list of subject for students. Assume on classroom is 
#   required for 1 subject. How many classroom are needed by all students.

# Uncomment for answer
# classroom = {"python", "java", "C++", "python","javascript", "java","python", "java", "C++", "C"}
# print("number of classes required: ", len(classroom))

#3. Write a program to enter marks of 3 subjects from the user and store them in
#   dictionary. Start with an empty dictionary and add one by one. Use subject name as key and mars as value.

# marks = {}
# x = int(input("Enter marks in phy: "))
# marks.update({"phy":x})
# x = int(input("Enter marks in chem: "))
# marks.update({"chem":x})
# x = int(input("Enter marks in maths: "))
# marks.update({"maths":x})

# print(marks)

#4. Figure out a way to store 9 and 9.0 as separate values in the set
# (You cantake help of built in data type)

set = {("float",9.0), ("int",9)}
print(set)
