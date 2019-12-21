# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   界面 class 练习 - Show
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox  # 这个是消息框，对话框的关键

class UC_Show:
    def __init__(self, pwin):
        print('UC_Show class created ! ')
        self.parent_win = pwin

        # create login window
        self.parent_win.title('Show - By Class')
        win_size_pos = '800x600'
        self.parent_win.geometry(win_size_pos)

        # 对本窗体进行自动布局
        self.__init_widgets()

        return

    def __init_widgets(self):
        '对本窗体进行布局'
        self.lbl_info = tk.Label(
            self.parent_win,
            text='Show form',
            anchor="w",
            justify="left",
            bg='blue',
            fg='white',
            height=1
        )
        self.lbl_info.place(x=20, y=20, width=200)
        return
