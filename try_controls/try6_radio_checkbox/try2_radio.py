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
frame_root1 = tk.Frame(top_win, bg="grey", width=760, height=200)
# frame_root1.pack()
frame_root1.place(x=20, y=20)

# Step2: Appedn other controls
# 单选框
var_sel = tk.IntVar()
var_sel.set(0)  # default value
text_of_btn = ('北京', '上海', '广州', '深圳')
value_of_btn = (0, 1, 2, 3)

def show_selected():
    v = var_sel.get()
    print(text_of_btn[v])
    return

for idx in range(4):
    rad_btn = tk.Radiobutton(
        frame_root1,
        variable=var_sel,
        text=text_of_btn[idx],
        value=value_of_btn[idx],
        command=show_selected
        )
    rad_btn.place(x=20 + idx * 190, y=40)



#------------------------------


# show window and get into event loop
top_win.mainloop()
