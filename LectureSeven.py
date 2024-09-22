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

f = open("demo.txt","w")
f.write("I wnat to learn Javascript")