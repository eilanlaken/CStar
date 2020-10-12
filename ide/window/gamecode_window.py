import tkinter as tk
import ctypes
from ide.ui_components.main_menu import *

user32 = ctypes.windll.user32


class GameCodeWindow:

    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    def __init__(self, current_project=None, project_preferences=None):
        self.current_project = current_project
        self.project_preferences = project_preferences
        self.root = tk.Tk()
        self.root.title('[project name place holder].....  - GameCode')
        set_menu_bar(self.root)

    def launch(self):
        self.root.mainloop()


