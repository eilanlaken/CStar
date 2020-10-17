from tkinter import *
import os
from tkinter import ttk


def get_icon_image(icon='directory', size=4):
    if icon == 'directory':
        img = PhotoImage(file=r"C:\Users\User\PycharmProjects\CStar\ide\assets\folderIcon.gif")
        img = img.subsample(size, size)
        return img
    elif icon == 'csfile':
        img = PhotoImage(file=r"C:\Users\User\PycharmProjects\CStar\ide\assets\pageIcon.gif")
        img = img.subsample(size, size)
        return img
    elif icon == 'imagefile':
        img = PhotoImage(file=r"C:\Users\User\PycharmProjects\CStar\ide\assets\imageFormatIcon.gif")
        img = img.subsample(size, size)
        return img
    elif icon == 'jsonfile':
        img = PhotoImage(file=r"C:\Users\User\PycharmProjects\CStar\ide\assets\jsonIcon.gif")
        img = img.subsample(size, size)
        return img
    elif icon == '3dfile':
        img = PhotoImage(file=r"C:\Users\User\PycharmProjects\CStar\ide\assets\meshIcon.gif")
        img = img.subsample(size, size)
        return img
    elif icon == 'closetab':
        img = PhotoImage(file=r"C:\Users\User\PycharmProjects\CStar\ide\assets\closeTab.gif")
        img = img.subsample(size, size)
        return img
