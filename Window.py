from tkinter import *

class Window(Tk):
    """Class responsible for the application window"""
    def __init__(self, size="1920x1080"):
        """Initialization"""
        super().__init__()
        self.title("Chameleon")
        self.geometry(size)
        self.resizable(True, True)
        self.minsize(200, 150)
        self.maxsize(1920, 1080)
        self.protocol("WM_DELETE_WINDOW", self.finish)
    def finish(self):
        """Closing"""
        self.destroy()
        print("Closing Chameleon")