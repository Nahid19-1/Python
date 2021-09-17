
file = open("test.txt","w")
file.write("my first file\n")
file.write("This file\n\n")
file.write("contains three lines\n")
file.close()
file = open("test.txt","r")
print(file.read())

file = open("test.txt","a")
file.write("a - Append - will append to the end of the file\n")
file = open("test.txt","r")
print(file.read())

#newfile = open("create.txt","x")

import os
#os.remove("create.txt")