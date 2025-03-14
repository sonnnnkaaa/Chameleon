from tkinter.messagebox import *

def open_info(info_message):
    showinfo(title="Information", message=info_message)

def open_warning(warning_message):
    showwarning(title="Warning", message=warning_message)

def open_error(error_message):
    showerror(title="Error", message=error_message)
