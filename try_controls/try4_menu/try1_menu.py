# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Menu )
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
# create a top menu
top_menu = tk.Menu(top_win)
'''
top_menu.add_command(label="Hello", command=None)
top_menu.add_command(label="Quit", command=top_win.quit)
'''
def cmd_menu_item():
    tk.messagebox.showinfo(title='Information',
                           message='Menu item clicked !')  # 提示信息对话窗
    return
# Create first dropdown menu
file_menu = tk.Menu(top_menu, tearoff=False)
file_menu.add_command(label="Open", command=cmd_menu_item)
file_menu.add_command(label="Save", command=cmd_menu_item)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=top_win.quit)
# add dropdown menu1 to top menu
top_menu.add_cascade(label="File", menu=file_menu)

# Create second dropdown menu
edit_menu = tk.Menu(top_menu, tearoff=False)
edit_menu.add_command(label="Select All", command=cmd_menu_item)
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=cmd_menu_item)
edit_menu.add_command(label="Cut", command=cmd_menu_item)
edit_menu.add_command(label="Paste", command=cmd_menu_item)
# add dropdown menu1 to top menu
top_menu.add_cascade(label="Edit", menu=edit_menu)


# show the menu
top_win.config(menu=top_menu)
#------------------------------


# show window and get into event loop
top_win.mainloop()
