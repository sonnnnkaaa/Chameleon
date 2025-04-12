from tkinter.filedialog import *
from tkinter import *
from tkinter.ttk import *
from datetime import datetime as dt
from directory_selecting import *
import os
from Message import *

def create_directory(new_dir_name):
    if new_dir_name == "":
        print(dt.now().time(), "Empty field is entered")
        open_warning("You have not entered the project name, please enter the name of your project")
        return
    print(dt.now().time(), "Directory creating window is opened")
    parent_dir = select_directory()
    if not parent_dir:
        return
    if not os.access(parent_dir, os.W_OK):
        print(dt.now().time(), f"No write permissions for", parent_dir)
    try:
        os.mkdir(parent_dir + "/" + new_dir_name)
    except OSError:
        print(dt.now().time(), "New directory was not created because it already exists")
        open_warning("A directory " + new_dir_name + " already exists")
        return
    # except TypeError:
    #     open_warning("Nothing is selected")
    #     return
    created_directory_path = parent_dir + "/" + new_dir_name
    print(dt.now().time(), created_directory_path, "is created")
    return created_directory_path

