from tkinter import *


class CodeEditorFrame(Frame):

    def __init__(self, root):
        super().__init__(root, bg='brown')
        self.open_tabs = []

