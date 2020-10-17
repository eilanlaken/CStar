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
        text_region = TextEditorFrame(tab, bg='grey20')
        text_region.pack(expand=1, fill='both')


class TextEditorFrame(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        self.vsb = Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.line_numbers = TextLineNumbers(self, width=30)
        self.line_numbers.attach(self.text)

        self.vsb.pack(side="right", fill="y")
        self.line_numbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

    def _on_change(self, event):
        self.line_numbers.redraw()


class TextLineNumbers(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        self.text_widget = None

    def attach(self, text_widget):
        self.text_widget = text_widget

    def redraw(self, *args):
        self.delete("all")

        i = self.text_widget.index("@0,0")
        while True:
            d_line = self.text_widget.dlineinfo(i)
            if d_line is None:
                break
            y = d_line[1]
            line_num = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=line_num)
            i = self.text_widget.index("%s+1line" % i)


class CustomText(Text):
    def __init__(self, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result


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
