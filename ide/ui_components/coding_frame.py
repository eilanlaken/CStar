from tkinter import *
from tkinter import ttk


def init_tabbed_region(parent: Frame, project_state=None):
    tabbed_view = ttk.Notebook(parent)
    if project_state is not None:
        for tab_descriptor in project_state.open_tabs_descriptors:
            tab = ttk.Frame(tabbed_view)
            tabbed_view.add(tab, text=tab_descriptor.name)
            text_region = Text(tab)
            text_region.insert(END, "Just a text Widget\nin two lines\n")
    else:  # debug
        tab = ttk.Frame(tabbed_view)
        tabbed_view.add(tab, text='welcome')

        '''
        empty_label = Label(tab, text='Welcome to')
        empty_label.pack(expand=1, fill='both')
        '''
        text_region = Text(tab)
        text_region.insert(END, "Just a text Widget\nin two lines\n")
        text_region.pack(expand=1, fill='both')
    tabbed_view.pack(expand=1, fill='both')
    return tabbed_view


class CodeEditorFrame(Frame):

    def __init__(self, root, project_state=None):
        super().__init__(root, bg='brown')
        self.tabbed_region = init_tabbed_region(self)

    def open_file_in_tabbed_view(self):
        pass

    def close_file_in_tabbed_view(self):
        pass
