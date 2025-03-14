from Window import *
from file_selecting import *
from directory_selecting import *
from CreateProjectWindow import *

class WelcomeWindow(Window):
    def __init__(self):
        super().__init__("Welcome to Chameleon!")
        x = self.winfo_screenwidth()
        y = self.winfo_screenheight()
        self.geometry('{}x{}+{}+{}'.format(int(x * 0.7), int(y * 0.7), 0, 0))
        create_project_btn = Button(text="Create empty project", command=self.create_chosen) # открытие нового окна
        open_project_btn = Button(text="Open existing project", command=self.open_chosen)
        upload_btn = Button(text="Upload an image", command=self.upload_chosen)
        create_project_btn.pack()
        open_project_btn.pack()
        upload_btn.pack()
        print(dt.now().time(), "Welcome window is opened")
    def create_chosen(self):
        print(dt.now().time(), "\"Create empty project\" option is chosen")
        create_project_win = CreateProjectWindow()
    def open_chosen(self):
        print(dt.now().time(), "\"Open existing project\" option is chosen")
        chosen_dir = select_directory()
        #продолжение в проекте уже
    def upload_chosen(self):
        print(dt.now().time(), "\"Upload an image\" option is chosen")
        chosen_image = select_file()
        #продолжение