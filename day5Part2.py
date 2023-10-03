# moving a file
import os

source = "day4.txt"
destination= "C:\\Users\\USER\Desktop\\Hello.txt "

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+'was moved')

except FileNotFoundError:
    print(source+'was not found')

# .....................

source = "folder"
destination= "C:\\Users\\USER\Desktop\\folder "

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+'was moved')

except FileNotFoundError:
    print(source+'was not found')


