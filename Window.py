from tkinter import *
from datetime import datetime as dt

class Window(Tk):
    name = ""
    """Class responsible for the application window"""
    def __init__(self, title):
        """Initialization"""
        super().__init__()
        self.title(title)
        self.name = title
        x = self.winfo_screenwidth()
        y = self.winfo_screenheight()
        self.geometry('{}x{}'.format(x, y))
        self.resizable(True, True)
        self.minsize(200, 150)
        self.maxsize(1920, 1080)
        self.protocol("WM_DELETE_WINDOW", self.finish)
    def finish(self):
        """Closing"""
        self.destroy()
        print(str(dt.now().time()) + " Closing window " + self.name + "...")