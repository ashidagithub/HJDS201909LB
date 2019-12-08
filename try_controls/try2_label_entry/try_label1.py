# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Label )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '800x600'
#win_size_pos = '360x60'
top_win.geometry(win_size_pos)

# ------------------------------
lbl_hello = tk.Label(
    top_win,
    text='Hello World!',
    bg='blue',
    fg='white',
    font=('Arial', 12),
    width=30,
    height=2
)
lbl_hello.pack()

lbl_programmer = tk.Label(
    top_win, text='I am a programmer!')
lbl_programmer.pack()

# 对图片进行预处理，变成 bitmap
image = Image.open('mybk.jpg')
bk_img = ImageTk.PhotoImage(image)
# 放置背景图片
lbl_bk = tk.Label(top_win, image=bk_img, text='MMP')
lbl_bk.place(x=100, y=300, width=600, height=300)

# ------------------------------


# show window and get into event loop
top_win.mainloop()
