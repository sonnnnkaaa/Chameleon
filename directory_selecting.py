from tkinter.filedialog import *
from datetime import datetime as dt

dir_name = ""

def select_directory():
    print(dt.now().time(), "Directory selecting window is opened")
    global dir_name
    dir_name = askdirectory(title="Select a directory", initialdir="/", mustexist=False)
    if dir_name == () or dir_name == "":
        print(dt.now().time(), "Nothing is selected...")
    else:
        print(dt.now().time(), dir_name, "is selected")