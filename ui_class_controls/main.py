# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   界面 class 练习 - Main
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox  # 这个是消息框，对话框的关键

from gui_class_login import UC_Login
from gui_class_show import UC_Show

# 显示登陆界面
'''
root = tk.Tk()
form_login = UC_Login(root)
root.mainloop()
root.destroy()

root = tk.Tk()
form_show = UC_Show(root)
root.mainloop()
'''

root = tk.Tk()
form_login = UC_Login(root)
root.mainloop()
root.destroy()

root = tk.Tk()
form_show = UC_Show(root)
root.mainloop()
