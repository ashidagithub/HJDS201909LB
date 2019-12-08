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

def cmd_print():
    print('Show in command window...')
    return

def cmd_pop():
    tk.messagebox.showinfo(title='Information',
                           message='Mouse clicked !')  # 提示信息对话窗
    '''
    tk.messagebox.showwarning(title='Warning', message='Warning Information')  # 提出警告对话窗
    tk.messagebox.showerror(title='Error', message='Error Information')  # 提出错误对话窗
    '''
    #print('Show in command window...')
    return

btn_help = tk.Button(top_win, text="Push me!", command=cmd_pop)
btn_help.pack()

entry_cleartext = tk.Entry(
    top_win,
    show='*',
    font=('Arial', 14)
)  # 显示成明文形式
# entry_cleartext.pack()
entry_cleartext.place(x=100, y=100, width=50)
# 按钮样式 与前景背景色
button_relieves = ('flat', 'groove', 'raised', 'ridge', 'solid', 'sunken')
for r in button_relieves:
    tk.Button(top_win, text=r, relief=r, width=10, height=2).pack()


btn_test = tk.Button(top_win, text='Log in ', relief='raised', width=10, height=2)
btn_test.pack()
# 图片按钮
image = Image.open('btn1_shutdown.jpg')
bk_img = ImageTk.PhotoImage(image)
btn_try_pic = tk.Button(top_win, text='try pic', compound='center', image=bk_img)
btn_try_pic.pack()

#------------------------------


# show window and get into event loop
top_win.mainloop()
