from Window import *

class WelcomeWindow(Window):
    def __init__(self):
        super().__init__("Welcome to Chameleon")
        x = self.winfo_screenwidth()
        y = self.winfo_screenheight()
        self.geometry('{}x{}+{}+{}'.format(int(x * 0.7), int(y * 0.7), 0, 0)) # 0 0 поменять
        create_project_btn = Button(text="Create project")
        open_project_btn = Button(text="Open existing project")
        upload_btn = Button(text="Upload an image")
        create_project_btn.pack()
        open_project_btn.pack()
        upload_btn.pack()