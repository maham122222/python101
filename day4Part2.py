# File detection

import os
import shutil

path ="C:\\Users\\USER\\Desktop\\pushpa"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist!")


# read a file
try:
    with open('day4.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("that file was not found :")

# write a file
# The 2nd argument is by default r which means read
text="hello \n This is some text"
with open('day4.txt','w') as file:
    file.write(text)
# a to append text so it will not overwrite previous one
text="hello \n This is other some text"
with open('day4.txt','a') as file:
    file.write(text)


# copy a file
# use shutil module to copy file

