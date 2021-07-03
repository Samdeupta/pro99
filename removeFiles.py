import shutil
import time
import os

path=input("Enter file path")

if(os.path.exists(path)):
    os.walk(path)

    timeindays=os.stat(path).st_ctime
    timeinsec=timeindays*24*60*60

    if(timeinsec > (30*24*60*60)):
        os.remove(path)
        print("Files deleted")
    else:
        shutil.rmtree() 
    
else:
    print("File path incorrect")