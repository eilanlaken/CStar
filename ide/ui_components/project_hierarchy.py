from tkinter import *


class ProjectHierarchyFrame(Frame):

    def __init__(self, root, application_context):
        super().__init__(root, bg='yellow')
        self.application_context = application_context
