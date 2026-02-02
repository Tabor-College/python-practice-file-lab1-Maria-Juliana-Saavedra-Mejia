# Strings and text files
# Subscript operator 

name = "Alan"
name = "Alan"
print(name[0])        # A
print(len(name))     # 4
print(name[len(name)-1])  # n
print(name[-2])      # an

# Slicing 

name2 = "Maria Juliana Saavedra Mejia"

name2[0:] #-entire string
name2[0:1]
name2[-3:] # last 3 characters

# Substring with IN operator

files = ["file.txt, file.doc, file.exe"]

for fileName in files: 
    if fileName.endswith(".txt"):
        print(fileName)


# Data encription 

# ASCII is a character encoding standard 
# that maps characters to numbers. 

# two imputs plain text and distance
 
# A cipher is a method or technique used to encrypt 
# and decrypt information by transforming readable text (plain text)
# into an unreadable form (cipher text) using a rule and 
# usually a key or value.
# In simple words: a cipher hides information 
# so only someone who knows the rule can understand it.

plain_text = input("Enter plain text: ")
distance = int(input("Enter distance (cipher value): "))

encrypted = ""

for char in plain_text:
    encrypted += chr(ord(char) + distance)

print("Encrypted text:", encrypted)

# Number system
# 8 - octal
# 16 - hexadecimal
# 10 - decimal 
# 2 - Binary

number = 415
binary = ""

while number > 0:
    residuo = number % 2
    binary = str(residuo) + binary
    number = number // 2

print("Binary:", binary)

# Text Files
# 1. writing text to file 

f = open("file.py", "w") # open is the function that opemns other files and w used to edit the file you open
f.write("line 1 ")
f.close()

# Example
import random

f = open("file.py", "w")
for count in range(100):
    num = random.randint(1,100)
    f.write(str(num)+'\n')
f.close

# 2. Read mode

f = open("file.txt", "r") # r is used in order just to read the content of the file 
text = f.read() # takes the whole document an puts it like one string 
print(text)

# Example 

f = open("file.txt", "r")
while True: 
    line = f.readline() # goes line by line in the whole file 
    if line == "":
        break
    print(line)

# 3. Manipulating files & directories in disk

import os

current = os.getcwd()
listofFiles = os.listdir(current)

for name in listofFiles:
    if ".py" in name:
        print(name)

# Paths to work with python 
# chdir(path)
# mkdir(path)
# remove(path)
# rmdir(path)

