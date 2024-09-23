# File I/O
 # Python can be used to perform operations on a file (read and write data)
"""
Types of all files
1. Text Files : .txt, .docx, .log etc
2. Binary Files : .mp4, .mov, .png, .jpge etc.
 
Open, read & close Files 
we have to open a file before reading or writing.
f = open("file_name","mode")
sample.txt  - r : read mode
demo.docx   - w : write mode

Modes 

Character 
'r': open for reading (default)
'w': open for writing, truncating the file first
'x': create a new file and open it for writing
'a': open for writing, appending to the end of the file if tit exists
'b': binary mode 
't': text mode (default)
'+': open a disk file for updating (reading and writing)

Reading a file
data = f.read() : reads entire file
data = f.readline() reads one line at a time
data = f.read(5) reads first 5 character of a file
"""
# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close() 

"""
Writing to a file
f = open("demo.txt", "w")
f.write("This is a new line") overwrites the entire file

f = open("demo.txt","a")
f.write("this is a new line") adds to the file 
"""

# f = open("demo.txt","w")
# f.write("I wnat to learn Javascript")
# f = open("demo.txt","r")
# data = f.read()
# print(data)
# f.close

"""appending the data"""

# with syntax
"""
with open("demo.txt", "a") as f:
    data = f.read()
"""

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt", "w") as f:
#     f.write("Iron Man is Toney Stark")
#     print(data)

# deleting a file
"""
using the os module 
Module (like a code library) is a file written by another programmer that
generally has a functions we can use.
"""
# import os 

# with open("sample.txt", "w") as f:
#     f.write("Iron Man is Toney Stark")
# os.remove("sample.txt") 

# Practice time
#1. Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java
# I like programming in Java

# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java\nI like programming in Java")

# with open("practice.txt","r") as f:
#     print(f.read())

#2. Write a function that replace all occurrence of "java" with "python" in above file
# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("Java","Python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)

#3. Search if the word "learning" exists in the file or not

# def checkWord(word):
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if(data.find(word)!= -1):
#             print("found")
#         else : print("not found")

# checkWord("sushant")

#4. write a function in whihc line of the file does the word "learning"
# occur first. Print -1 if word not found
# def checkWordline(word):
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no +=1
#     return -1

# result = checkWordline("pyq")
# print(result)

#4. From a file containg number separated by comma, print the count of even numbers
# 1, 2, 76, 84, 90, 101
count = 0
with open("practice.txt","r") as f:
    data = f.read()
    print(data)
    
    num = data.split(",")
    print(num)
    for i in num:
        if(int(i) % 2 == 0):
            count+=1
        
print(count)