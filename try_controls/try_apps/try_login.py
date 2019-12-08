# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Window )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
from tkinter import ttk

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '240x200'
#win_size_pos = '360x60'
top_win.geometry(win_size_pos)

#------------------------------
# Step1:
lbl_info = tk.Label(
    top_win,
    text='Login form',
    anchor="w",
    justify="left",
    bg='#ceceff',
    fg='white',
    width=27,
    height=1
)
lbl_info.place(x=20, y=20)

#------------------------------


# show window and get into event loop
top_win.mainloop()
