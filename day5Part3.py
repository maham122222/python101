import os
import shutil
# os.remove(path)=to delete file
# os.rmdir(path)=to delete an empty directory
# shutil.rmtree(path)=to delete directory containing files

# used shutil module here to delete a folder and also files in it

# Deleting a file
path = 'text.txt'
# os.remove(path)

try:
    os.remove(path)
    print('file is deleted')
except FileNotFoundError:
    print("That file was not found")

# deleting a folder

path = 'emptyfolder'

try:
    os.rmdir(path)
    print('file is deleted')
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
else:
    print(path+' was deleted')



# to delete folder and a file inside a folder

path = 'folder'

try:
    shutil.rmtree(path)
    print('file is deleted')
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("you cannot delete that using that function")
else:
    print(path+' was deleted')
























