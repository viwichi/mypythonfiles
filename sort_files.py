# Make sure you have python3 or up installed 
# Check out https://www.python.org/downloads/ to download.
# And you are good to go :)
# This program does't require any other configuaratios.
#Make sure you give the right path in lin 12

import os
import shutil
   
# Give the name of the directory here,
# that needs to get sorted
path = '/path/to/your/directory'
  
  
# This will create a list with
# All the filename that directory

list_ = os.listdir(path)
   
# This will go through each file
for file_ in list_:
    name, ext = os.path.splitext(file_)
  
    # This is to store the extension type
    ext = ext[1:]
  
    # This forces the next iteration,
    # if it is the directory
    if ext == '':
        continue
  
    # This is to move the file to the directory
   
    if os.path.exists(path+'/'+ext):
       shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
  
    # This will create a new directory,
    # If the directory does not already exist
    # And files will be moved to the directory
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
