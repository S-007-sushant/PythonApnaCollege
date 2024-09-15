# Lecture Four : Dictionary and set in python
""""
Dictionnaries are used to store data value in key:value pairs
they are unordered, mutable (changeable) and don't allow duplicate keys
ex : 
dict = {
    "name": "Sushant"
    "cgpa": 9.6
    "marks" : [98,97,94],
}
"""
# info = {
#     "name":"sushant raj",
#     "subject": ["python","C","Java"],
#     "topics": ("Dict","set"),
#     "learning":"coding",
#     "age": 53,
#     "is_adult":True,
#     "marks":84
# }
# print(info["name"])
# info["name"] = "Sushant Raj"
# info["college"] = "BIT Mesra"
# print(info)

null_dict = {}
null_dict["name"] = "ApnaCollege"
print(null_dict)

#Nested Dictionaries
# we can create nested dictionaries also
student ={
    "name":"Sushant Raj",
    "subjects": {
        "phy":97,
        "chem":88,
        "math":90
    }
}
print(student["subjects"]["phy"])

#Dictionary Methods
# 1. myDict.keys() return all keys
# 2. myDict.values() return all values
# 3. myDict.items() returns all (key, value), pairs as tuples
# 4. myDict.get("key") return the key according to value
# 5. myDict.update(newDict) inserts the specified items to the dictionary.

print(list(student.values()))

# print(len(list(student.values())))
print(list(student.items()))
pairs = list(student.items())

print(student.get("name")) #will not give error if the key is wrong
print(student["name"]) # will give error when parameter not find

student.update({"city":"mumbai", "age":24})
print(student)
