from tkinter import *


# File menu actions
def file_command_new_project():
    print('New Project Clicked')


def file_command_new():
    print('New Clicked')


def file_command_open():
    print('Open Clicked')


# Edit menu actions

def edit_command_():
    pass


# Navigation
def nav_command_():
    pass


# Help menu actions
def help_command_cstar_tutorials():
    print('C* Tutorials Clicked')


def help_command_how_to():
    print('How to Clicked')


def help_command_find():
    print('Fined clicked')


def init_menu_bar(root):
    menu_bar = Menu(root)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='New Project', command=file_command_new_project)
    file_menu.add_separator()
    file_menu.add_command(label='Open', command=file_command_open)
    file_menu.add_command(label='Open Recent', command=file_command_open)
    file_menu.add_command(label='Open From Link', command=file_command_open)
    file_menu.add_separator()
    file_menu.add_command(label='Save', command=file_command_open)
    menu_bar.add_cascade(label='File', menu=file_menu)

    edit_menu = Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label=r'Undo                  Ctrl + Z', command=edit_command_)
    edit_menu.add_command(label=r'Redo          Ctrl + Shift + Z', command=edit_command_)
    edit_menu.add_separator()
    edit_menu.add_command(label='Cut                    Ctrl + X', command=edit_command_)
    edit_menu.add_command(label='Copy                   Ctrl + C', command=edit_command_)
    edit_menu.add_command(label='Paste                  Ctrl + V', command=edit_command_)
    edit_menu.add_command(label='Delete                   Delete', command=edit_command_)
    edit_menu.add_separator()
    edit_menu.add_command(label='Indent Selection            Tab', command=edit_command_)
    edit_menu.add_command(label='Unindent Selection  Shift + Tab', command=edit_command_)
    edit_menu.add_separator()
    edit_menu.add_command(label=r'Select All            Ctrl + A', command=edit_command_)
    menu_bar.add_cascade(label='Edit', menu=edit_menu)

    nav_menu = Menu(menu_bar, tearoff=0)
    nav_menu.add_command(label=r'Search...               Shift x 2', command=nav_command_)
    nav_menu.add_separator()
    nav_menu.add_command(label=r'Prev File             Ctrl + Left', command=nav_command_)
    nav_menu.add_command(label=r'Next File            Ctrl + Right', command=nav_command_)
    nav_menu.add_separator()
    nav_menu.add_command(label=r'Find In File...          Ctrl + F', command=nav_command_)
    nav_menu.add_separator()
    nav_menu.add_command(label=r'Prev Function              Shift + Scroll Up', command=nav_command_)
    nav_menu.add_command(label=r'Next Function            Shift + Scroll Down', command=nav_command_)
    nav_menu.add_command(label=r'Prev Issue                  Ctrl + Scroll Up', command=nav_command_)
    nav_menu.add_command(label=r'Next Issue                Ctrl + Scroll Down', command=nav_command_)
    menu_bar.add_cascade(label='Navigate', menu=nav_menu)

    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="C* Docs", command=help_command_cstar_tutorials)
    help_menu.add_command(label="How to...", command=help_command_how_to)
    help_menu.add_command(label="Contribute", command=help_command_how_to)
    menu_bar.add_cascade(label='Help', menu=help_menu)

    root.config(menu=menu_bar)

