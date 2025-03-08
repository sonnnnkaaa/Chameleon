from Window import *
from directory_selecting import *

project_name = ""

class CreateProjectWindow(Window):
    def __init__(self):
        super().__init__("Create new project")
        x = self.winfo_screenwidth()
        y = self.winfo_screenheight()
        self.geometry('{}x{}+{}+{}'.format(int(x * 0.3), int(y * 0.5), 0, 0))
        choose_dir_btn = Button(text="Choose directory", command=select_directory, textvariable=dir_name)
        project_name_input = Entry()
        project_name_input.pack()
        choose_dir_btn.pack()
    def choosing_dir(self):
        
