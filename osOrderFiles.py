from distutils import extension
import os
import shutil

dirName = input('enter folder name: ')
li = os.listdir(dirName)

for i in li:
    filename,extension = os.path.splitext(i)
    extension = extension[1:]

    if extension == "":
        continue

    if os.path.exists(dirName +'/'+extension):
        shutil.move(dirName+'/'+i,dirName+'/'+extension +'/'+i)
    else:
        os.makedirs(dirName+'/'+ extension)
        shutil.move(dirName+'/'+i,dirName+'/'+extension+'/'+i)