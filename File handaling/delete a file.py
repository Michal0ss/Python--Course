import os
import shutil

path = "asd.txt"

try:
    os.remove(path)       #delete a file
    # os.rmdir(path)        #delete an empty folder
    #shutil.rmtree(path)     #delete a folder containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You dont have permission to delete that")
except OSError:
    print("You cannot delete that using that function")  #
else:
    print(path + " was deleted")
