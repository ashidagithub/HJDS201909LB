# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Window )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '800x600'
#win_size_pos = '360x60'
top_win.geometry(win_size_pos)

#------------------------------
# balablabla

# create a top menu
top_menu = tk.Menu(top_win)
top_menu.add_command(label="Hello", command=None)
top_menu.add_command(label="Quit", command=top_win.quit)

top_menu2 = tk.Menu(top_win)
top_menu2.add_command(label="Byebye", command=None)
top_menu2.add_command(label="Quit", command=top_win.quit)

# show the menu
top_win.config(menu=top_menu2)


#------------------------------


# show window and get into event loop
top_win.mainloop()
