from tkinter import *
import os
from tkinter import ttk
from ide.ui_components.static_assets import *


class ProjectHierarchyFrame(Frame):

    def __init__(self, root, application_context, project_directory=None):
        super().__init__(root, bg='yellow')
        self.application_context = application_context
        self.project_tree = ProjectTree(self)


class ProjectTree(ttk.Treeview):

    def __init__(self, parent: Frame, project_directory=None):
        super().__init__(parent, show='tree')
        self.y_bar = Scrollbar(parent, orient=VERTICAL, command=self.yview)
        super().configure(yscroll=self.y_bar.set)
        project_directory = r'C:\Users\User\PycharmProjects\CStar\ide\ui_components'
        super().heading('#0', text='Dir：'+project_directory, anchor='w')
        path = os.path.abspath(project_directory)
        self.img = get_icon_image('3dfile')
        node = super().insert('', 'end', image=self.img, text=path, open=True)
        self.traverse_dir(node, path)
        self.y_bar.pack(fill=Y, side=RIGHT)
        super().pack(fill=BOTH)

    def populate_tree(self, node):
        pass

    def traverse_dir(self, parent, path):
        for d in os.listdir(path):
            full_path = os.path.join(path, d)
            isdir = os.path.isdir(full_path)
            id = self.insert(parent, 'end', image=self.img, text=d, open=False)
            if isdir:
                self.traverse_dir(id, full_path)


class ImagedLabel(Label):

    def __init__(self, root, text, icon='directory'):
        self.img = get_icon_image(icon)
        super().__init__(root, text=text, image=self.img, bg='yellow', compound=LEFT)
