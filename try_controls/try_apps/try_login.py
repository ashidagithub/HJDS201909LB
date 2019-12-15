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
top_win.title('Login')

# resize root window
win_size_pos = '240x200'
#win_size_pos = '360x60'
top_win.geometry(win_size_pos)

# ------------------------------
# Step1:
lbl_info = tk.Label(
    top_win,
    text='Login form',
    anchor="w",
    justify="left",
    bg='#ceceff',
    fg='white',
    height=1
)
lbl_info.place(x=20, y=20, width=200)

# Step2:
default_var = tk.StringVar(value='username')
ent_username = tk.Entry(
    top_win,
    show=None,
    textvariable=default_var,
)
ent_username.place(x=20, y=60, width=200)

default_var = tk.StringVar(value='password')
ent_password = tk.Entry(
    top_win,
    show='*',
    textvariable=default_var,
)
ent_password.place(x=20, y=100, width=200)


def cmd_login():
    print(ent_username.get())
    print(ent_password.get())
    u = ent_username.get()
    p = ent_password.get()

    '''
    if u == 'admin':
        if p == '666':
            tk.messagebox.showinfo(title='Information', message='Successed!')
        else:
            tk.messagebox.showerror(
                title='Information', message='Wrong password!')
    else:
        tk.messagebox.showerror(title='Information', message='Wrong username!')
    '''

    if u == 'admin' and p == '666':
        tk.messagebox.showinfo(title='Information', message='Successed!')
    else:
        tk.messagebox.showerror(title='Information',
                                message='Wrong username or password')

    return


btn_login = tk.Button(
    top_win,
    text='Sign in ',
    relief='raised',
    width=10, height=2,
    bg='#ceceff',  fg='white',
    command=cmd_login,
)
btn_login.place(x=20, y=140, width=50)


# ------------------------------


# show window and get into event loop
top_win.mainloop()
