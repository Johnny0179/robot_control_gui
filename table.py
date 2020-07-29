from tkinter import *
import tkinter.ttk as ttk
import threading


def ShowTree(table, start_address, reg_num, reg):
    # global list_hold_reg
    # reg = list_hold_reg
    tree = ttk.Treeview(table, height=50)  # #创建表格对象,default 50 rows

    # style
    s = ttk.Style(table)
    s.configure('Treeview', rowheight=40)

    tree["columns"] = ('#1')  # #定义列
    tree.column('#0', width=30, minwidth=150)
    tree.column('#1', width=30, minwidth=150)

    # Define Column Headings
    tree.heading('#0', text="Reg Address",anchor=W)
    tree.heading('#1', text="Reg Value", anchor=W)

    # test
    # reg[0]=reg[0]+1

    # insert rows
    for i in range(start_address, start_address + reg_num):
        tree.insert("", i, text=i, values=hex(reg[i]))

    tree.pack(side=TOP, fill=X)
    # tree.after(1000, ShowTree(table, start_address, reg_num, reg))


def ShowTable(start_address, reg_num, reg):
    # global list_hold_reg
    # create new window
    table = Toplevel()
    table.title("Holding Registers")
    table.geometry("400x1400")

    ShowTree(table, start_address, reg_num, reg)