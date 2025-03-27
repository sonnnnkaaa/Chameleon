from tkinter.filedialog import *
from datetime import datetime as dt

def select_directory():
    print(dt.now().time(), "Directory selecting window is opened")
    dir_name = askdirectory(title="Select a directory", initialdir="/", mustexist=False)
    if dir_name == () or dir_name == "":
        print(dt.now().time(), "Nothing is selected...")
        return
    else:
        print(dt.now().time(), dir_name, "is selected")
        return dir_name

