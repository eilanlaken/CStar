from tkinter import *

CURRENT_CONTEXT_PROGRAM_OUTPUT = 0
CURRENT_CONTEXT_COMPILE_LOG = 1


class ConsoleLogFrame(Frame):

    def __init__(self, root):
        self.parent = root
        self.current_context = CURRENT_CONTEXT_PROGRAM_OUTPUT
        self.program_output = ProgramOutputFrame(self)
        self.compiler_output = CompileLogFrame(self)


class ProgramOutputFrame(Frame):

    def __init__(self, parent: ConsoleLogFrame):
        self.parent = parent
        self.program_output_text = ''


class CompileLogFrame(Frame):

    def __init__(self, parent: ConsoleLogFrame):
        self.parent = parent
        self.compile_log_text = ''


class ConsoleContextBar(Frame):

    def __init__(self, parent: ConsoleLogFrame):
        self.parent = parent
        self.btn_program_output = Button(parent, text='Program Output', command=self.switch_context)
        self.btn_program_output.pack()
        self.btn_compile_log = Button(parent, text='Compile Log', command=self.switch_context)
        self.btn_compile_log.pack()

    def switch_context(self):
        print('current context: ' + str(self.parent.current_context))
