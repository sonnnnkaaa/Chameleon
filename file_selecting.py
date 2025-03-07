from tkinter.filedialog import *
from datetime import datetime as dt

filename = ""

def select_file():
    _filetypes = [('JPEG pictures', '*.jpg'),
                  ('PNG pictures', '*.png'),
                  ('All files', '*.*')]
    print(dt.now().time(), "File selecting window is opened")
    global filename
    filename = askopenfilename(title="Select a file", initialdir="/", filetypes=_filetypes)
    if filename == () or filename == "":
        print(dt.now().time(), "Nothing is selected...")
    else:
        # with open(filename, "rb") as selected_file: #rb - двоичный режим (без него не работает)
        #     content = selected_file.read()
        print(dt.now().time(), filename, "is selected")