from tkinter import *
from tkinter.ttk import *
class Window(Tk):
    """Class responsible for the application window"""
    def __init__(self, title):
        """Initialization"""
        super().__init__()
        self.title(title)
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
        print("Closing Chameleon...")