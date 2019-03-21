import os
import shutil

cwd=os.getcwd()

for(path,dirs,files) in os.walk(cwd):
    for f in files:
        fullpath = os.path.join(path,f)
        print(fullpath)
        if f=="move_file.py":
          continue
        print(cwd)
        shutil.move(fullpath,cwd)
