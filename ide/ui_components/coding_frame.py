from tkinter import *
from tkinter import ttk
from ide.ui_components.static_assets import *


def apply_style_code(text_region: Text):
    text = text_region.get("1.0", "end-1c")

    text_region.tag_configure("warning", background=text["bg"], foreground="white")


def init_tabbed_region(parent: Frame, project_state=None):
    tabbed_view = ttk.Notebook(parent)
    if project_state is not None:
        pass  # ignore for now.
    else:  # debug
        tab = ttk.Frame(tabbed_view)
        tabbed_view.add(tab, text='welcome')

        '''
        empty_label = Label(tab, text='Welcome to')
        empty_label.pack(expand=1, fill='both')
        '''
        text_region = Text(tab, bg='grey20')
        text_region.tag_configure("access_modifier", background=text_region['bg'], foreground="white")
        text_region.tag_raise("sel")

        text_region.insert("1.0", "public 898 9!")
        text_region.tag_add("access_modifier", "1.0", "1.21")
        text_region.insert(END, "Just a text Widget\nin two lines\n")
        text_region.pack(expand=1, fill='both')
    tabbed_view.pack(expand=1, fill='both')
    return tabbed_view


class AutoCompletePredictor:
    pass


class GCNotebook(ttk.Notebook):

    def __init__(self, parent: Frame, project_json):
        super().__init__(parent)
        self.image = get_icon_image('directory')
        self.init_for_debug()

    def init_from_json(self, project_json):
        pass

    def init_for_debug(self):
        tab = Frame(self)
        self.add(tab, text='okkok', image=self.image, compound=LEFT)
        text_region = Text(tab, bg='grey20')
        text_region.pack(expand=1, fill='both')


class CodeEditorFrame(Frame):

    def __init__(self, root, project_state=None):
        super().__init__(root, bg='brown')
        #self.tabbed_region = init_tabbed_region(self)
        self.notebook = GCNotebook(root, None)
        self.notebook.pack(expand=1, fill=BOTH)

    def open_file_in_tabbed_view(self):
        pass

    def close_file_in_tabbed_view(self):
        pass
