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
from PIL import Image, ImageTk

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '800x600'
#win_size_pos = '360x60'
top_win.geometry(win_size_pos)

#------------------------------

# 对图片进行预处理，变成 bitmap
image = Image.open('2020-MeiTu.png')
bk_img = ImageTk.PhotoImage(image)
# 放置背景图片
# balablabla
lbl_background = tk.Label(
    top_win,
    text='Hello World!',
    bg='black',
    image=bk_img,
)
lbl_background.place(x=0, y=0, width=800, height=600)

ent_username = tk.Entry(top_win, width=10, bg='black', fg='white')
ent_username.place(x=600, y=450)

#------------------------------


# show window and get into event loop
top_win.mainloop()
