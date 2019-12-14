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
# Step1: Create frame
frame_root1 = tk.Frame(top_win, bg="#BF3EFF", width=760, height=200)
# frame_root1.pack()
frame_root1.place(x=20, y=20)

# Step2: Appedn other controls
lbl_test = tk.Label(frame_root1, text='text in frame')
lbl_test.place(x=20, y=20)
#------------------------------


# show window and get into event loop
top_win.mainloop()
