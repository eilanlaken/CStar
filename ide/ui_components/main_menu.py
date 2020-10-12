from tkinter import *


# File menu actions
def file_command_new_project():
    print('New Project Clicked')


def file_command_new():
    print('New Clicked')


def file_command_open():
    print('Open Clicked')


# Edit menu actions

# Help menu actions
def help_command_cstar_tutorials():
    print('C* Tutorials Clicked')


def help_command_how_to():
    print('How to Clicked')


def help_command_find():
    print('Fined clicked')


def set_menu_bar(root):
    menu_bar = Menu(root)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='New Project', command=file_command_new_project)
    file_menu.add_command(label='New ...', command=file_command_new)
    file_menu.add_separator()
    file_menu.add_command(label='Open', command=file_command_open)
    menu_bar.add_cascade(label='File', menu=file_menu)

    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="C* Tutorials", command=help_command_cstar_tutorials)
    help_menu.add_command(label="How to...", command=help_command_how_to)
    help_menu.add_command(label="Find...", command=help_command_find)
    menu_bar.add_cascade(label='Help', menu=help_menu)
    root.config(menu=menu_bar)

