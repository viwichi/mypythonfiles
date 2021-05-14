# Python program to rename all file
# names in your directory 
# Make sure you have python installed
# This program doesn't require any other configurations.
# Just give the path to the directory  in line 10
# And you'll be good to go

import os
  
os.chdir('give/path/to/your/directory/here')
print(os.getcwd())
INC = 1

def increment():
    global INC
    INC = INC + 1
  
  
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_name = "file" + str(INC)
    increment()
  
    new_name = '{} {}'.format(f_name, f_ext)
    os.rename(f, new_name)
