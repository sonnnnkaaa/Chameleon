from tkinter.filedialog import *
from tkinter import *
from tkinter.ttk import *
from datetime import datetime as dt
import os

new_dir_name = ""

def create_directory():
    print(dt.now().time(), "File selecting window is opened")
    global new_dir_name
    parent_dir = askdirectory(title="Select a directory in which to save the new project", initialdir="/", mustexist=False)

    while True:

        try:
