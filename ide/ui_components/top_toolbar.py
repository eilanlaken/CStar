from tkinter import *


def run():
    print('run clicked')


def terminate():
    print('terminate clicked')


def search():
    print('search clicked')


def debug_call(frame: Frame):
    print('hello ' + str(frame.config))


class TopToolBar(Frame):

    def __init__(self, application_context, root, path_labels):
        super().__init__(root, bg='red')
        self.application_context = application_context
        self.path_labels = path_labels
        self.labels = []

        # left hand side: context
        for label_str in self.path_labels:
            self.labels.append(Label(self, text=label_str).pack(side=LEFT, padx=5, pady=5))

        # right hand side: run, terminate, search
        self.run_btn = Button(self, text='Run', command=run)
        self.terminate_btn = Button(self, text='Kill', command=terminate)
        self.search_btn = Button(self, text='Search', command=search)
        self.debug_btn = Button(self, text='Debug', command=lambda: debug_call(self))

        self.debug_btn.pack(side=RIGHT, padx=5, pady=5)
        self.run_btn.pack(side=RIGHT, padx=5, pady=5)
        self.terminate_btn.pack(side=RIGHT, padx=5, pady=5)
        self.search_btn.pack(side=RIGHT, padx=5, pady=5)

    def reset_context_labels(self, path_labels):
        pass

