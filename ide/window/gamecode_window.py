import tkinter as tk
from tkinter import ttk
import ctypes
from ide.ui_components.main_menu import *
from ide.ui_components.top_toolbar import *
from ide.ui_components.coding_frame import CodeEditorFrame
from ide.ui_components.project_hierarchy import ProjectHierarchyFrame

user32 = ctypes.windll.user32


class GameCodeWindow:

    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    def __init__(self, application_context, current_project=None, project_preferences=None):
        self.application_context = application_context
        self.current_project = current_project
        self.project_preferences = project_preferences
        self.root = tk.Tk()
        style = ttk.Style()
        style.theme_create("MyStyle", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [2, 0, 2, 0]}},
            "TNotebook.Tab": {"configure": {"padding": [12, 4]}, }})
        style.theme_use("MyStyle")
        self.root.iconbitmap(r'C:\Users\User\PycharmProjects\CStar\ide\assets\gameCodeIcon.ico')
        self.root.title('[project name place holder].....  - GameCode')
        self.root.geometry('{}x{}'.format(int(GameCodeWindow.screensize[0]*0.8), int(GameCodeWindow.screensize[1]*0.8)))
        self.root['bg'] = 'gray5'
        init_menu_bar(self.root)
        # layout all of the main containers
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        create_top_frame(self.root, application_context)
        create_center_region(self.root, application_context)
        create_bottom_frame(self.root)

    def launch(self):
        self.root.mainloop()


def create_top_frame(root, application_context):
    top_frame = TopToolBar(application_context, root, ['proj 1 > ', 'hisfgs'])
    top_frame.pack(anchor=W, fill=X, expand=FALSE)


def create_center_region(root, application_context):
    center_frame = Frame(root)
    center = PanedWindow(center_frame, bg='grey10', orient=VERTICAL, sashwidth=8, showhandle=True)
    development_view = PanedWindow(center, bg='white', orient=HORIZONTAL, sashwidth=8, showhandle=True)
    project_hierarchy = ProjectHierarchyFrame(development_view, application_context)
    code_editor = CodeEditorFrame(development_view)
    development_view.add(project_hierarchy)
    development_view.add(code_editor)
    console_view = Frame(center, bg='yellow')
    center.add(development_view)
    center.add(console_view)
    center.pack(fill=BOTH, expand=True)
    center_frame.pack(fill=BOTH, expand=True)


def create_bottom_frame(root):
    bottom = Frame(root, bg='blue', width=int(GameCodeWindow.screensize[0] * 0.8), height=20, padx=3, pady=3)
    bottom.pack(side=BOTTOM, fill=BOTH, expand=False)
    bottom.lift()
