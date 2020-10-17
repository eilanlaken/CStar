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
    edit_menu.add_command(label=r'Undo', command=edit_command_, accelerator="Ctrl + Z")
    edit_menu.add_command(label=r'Redo', command=edit_command_, accelerator='Ctrl + Shift + Z')
    edit_menu.add_separator()
    edit_menu.add_command(label='Cut', command=edit_command_, accelerator='Ctrl + X')
    edit_menu.add_command(label='Copy', command=edit_command_, accelerator='Ctrl + C')
    edit_menu.add_command(label='Paste', command=edit_command_, accelerator='Ctrl + V')
    edit_menu.add_command(label='Delete', command=edit_command_, accelerator='Delete')
    edit_menu.add_separator()
    edit_menu.add_command(label='Indent Selection', command=edit_command_, accelerator='Tab')
    edit_menu.add_command(label='Unindent Selection', command=edit_command_, accelerator='Shift + Tab')
    edit_menu.add_separator()
    edit_menu.add_command(label=r'Select All', command=edit_command_, accelerator='Ctrl + A')
    menu_bar.add_cascade(label='Edit', menu=edit_menu)

    nav_menu = Menu(menu_bar, tearoff=0)
    nav_menu.add_command(label=r'Search...', command=nav_command_, accelerator='Shift x 2')
    nav_menu.add_separator()
    nav_menu.add_command(label=r'Prev File', command=nav_command_, accelerator='Ctrl + Left')
    nav_menu.add_command(label=r'Next File', command=nav_command_, accelerator='Ctrl + Right')
    nav_menu.add_separator()
    nav_menu.add_command(label=r'Find In File...', command=nav_command_, accelerator='Ctrl + F')
    nav_menu.add_separator()
    nav_menu.add_command(label=r'Prev Function', command=nav_command_, accelerator='Shift + Scroll Up')
    nav_menu.add_command(label=r'Next Function', command=nav_command_, accelerator='Shift + Scroll Down')
    nav_menu.add_command(label=r'Prev Issue', command=nav_command_, accelerator='Ctrl + Scroll Up')
    nav_menu.add_command(label=r'Next Issue', command=nav_command_, accelerator='Ctrl + Scroll Down')
    menu_bar.add_cascade(label='Navigate', menu=nav_menu)

    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="C* Docs", command=help_command_cstar_tutorials)
    help_menu.add_command(label="How to...", command=help_command_how_to)
    help_menu.add_command(label="Contribute", command=help_command_how_to)
    menu_bar.add_cascade(label='Help', menu=help_menu)

    root.config(menu=menu_bar)

