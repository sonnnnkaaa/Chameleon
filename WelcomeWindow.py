from file_selecting import *
from CreateProjectWindow import *
from WorkAreaWindow import *

class WelcomeWindow(Window):
    def __init__(self):
        super().__init__("Welcome to Chameleon!")
        x = self.winfo_screenwidth()
        y = self.winfo_screenheight()
        self.geometry('{}x{}+{}+{}'.format(int(x * 0.7), int(y * 0.7), 0, 0))
        self.create_project_btn = Button(text="Create empty project", command=self.create_chosen) # открытие нового окна
        self.open_project_btn = Button(text="Open existing project", command=self.open_chosen)
        self.upload_btn = Button(text="Upload an image", command=self.upload_chosen)
        self.exit_btn = Button(text="Exit", command=self.finish)
        self.create_project_btn.pack()
        self.open_project_btn.pack()
        self.upload_btn.pack()
        self.exit_btn.pack()
        print(dt.now().time(), "Welcome window is opened")
    def create_chosen(self):
        print(dt.now().time(), "\"Create empty project\" option is chosen")
        CreateProjectWindow()
        """здесь обязательно добавить закрытие welc win если перешли в рабочую область"""
    def open_chosen(self):
        print(dt.now().time(), "\"Open existing project\" option is chosen")
        chosen_dir = select_directory()
        self.open_project_btn["state"] = "disabled"
        if chosen_dir:
            self.finish()
            WorkAreaWindow(chosen_dir)
        else:
            self.open_project_btn["state"] = "normal"
    def upload_chosen(self):
        print(dt.now().time(), "\"Upload an image\" option is chosen")
        chosen_image = select_file()
        self.upload_btn["state"] = "disabled"
        if chosen_image:
            self.finish()
            """продолжение"""
        else:
            self.upload_btn["state"] = "normal"
