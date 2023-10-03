import shutil
# using shutil module for copy file

# copy file()=copies contents of a file
# copy()=copyfile()+permission mode+destination can be directory
# copy2()=copy()+copies metadata(file's creation and modification times)

# copy a file

shutil.copyfile('day4.txt','copy.txt') 
#(src,dst)

shutil.copyfile('day4.txt','C:\\Users\\USER\Desktop\\copy.txt') 

