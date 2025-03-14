from Window import *
from directory_selecting import *
from directory_creating import *
import os

class CreateProjectWindow(Window):
    def __init__(self):
        super().__init__("Create new project")
        self.project_name = None
        x = self.winfo_screenwidth()
        y = self.winfo_screenheight()
        self.geometry('{}x{}+{}+{}'.format(int(x * 0.3), int(y * 0.5), 0, 0))
        self.project_name_input = Entry(master=self)
        self.project_name_input.pack()
        self.create_proj_btn = Button(master=self,
                                      text="Create",
                                      command=self.click_create_btn)
        self.create_proj_btn.pack()
    def click_create_btn(self):
        self.create_proj_btn["state"] = "disabled"
        self.project_name = self.project_name_input.get()
        if create_directory(self.project_name):

        else:
            self.create_proj_btn["state"] = "normal"


