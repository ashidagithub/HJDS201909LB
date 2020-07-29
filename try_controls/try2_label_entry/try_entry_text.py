# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Entry, Text )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
from tkinter import ttk

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '800x600'
#win_size_pos = '360x60'
top_win.geometry(win_size_pos)

# ------------------------------
default_var = tk.StringVar(value='2019/12/8')
ent_row = tk.Entry(
    top_win,
    show=None,
    textvariable=default_var,
)
#ent_row.pack()
ent_row.place(x=100, y=100, width=150)

txt_desc = tk.Text(top_win, height=6, width=50)
txt_desc.pack()

# ------------------------------

# show window and get into event loop
top_win.mainloop()
