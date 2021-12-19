#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tkinter as tk
from tkinter import ttk
from windowFun import AndroidTools

file_path = os.path.abspath(os.path.dirname(__file__))
dirpath = '/Data/'
if not os.path.exists(file_path + dirpath):
    os.mkdir(file_path + dirpath)
    os.mkdir(file_path + dirpath + "/screenshot")
    os.mkdir(file_path + dirpath + "/log")
    os.mkdir(file_path + dirpath + "/screenrecord")

def device_status():
    device_info.delete(1.0, tk.END)
    device_info.insert(1.0, AndroidTools().get_status())


window = tk.Tk()
window.geometry("1300x700+5+5")
window.title("Android Tools")

note_book = ttk.Notebook()  #导航栏
phone_tab = ttk.Frame(note_book)
note_book.add(phone_tab, text="手机")
note_book.pack(expand=1, fill='both')

'''手机连接状态'''
status_frame = ttk.LabelFrame(phone_tab, text="手  机")
status_frame.grid(column=0, row=0, sticky='NW', padx=8, pady=4)

label_status = ttk.Label(status_frame, text="设备名")
label_status.grid(column=0, row=0, sticky='W')

device_info = tk.Text(status_frame, width=50, height=1.4, bd=2, fg='blue', font='Helvetica -16')
device_info.grid(column=1, row=0, sticky='W')
device_status()

refresh_Btn = tk.Button(status_frame, text="刷新状态", command=device_status, bd=2, width=12, font='Helvetica -16')
refresh_Btn.grid(column=2, row=0, sticky='W')


'''截图'''
screenshot_frame = ttk.LabelFrame(phone_tab)
screenshot_frame.grid(column=0, row=1, sticky='NW', padx=8, pady=4)

# screenshot_lable = ttk.L


window.mainloop()