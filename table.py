import tkinter.ttk as ttk
from tkinter import *


def RefereshTree(tree, start_address, reg_num, reg):
    # mn.list_hold_reg
    # insert rows
    for i in range(start_address, start_address + reg_num):
        if reg[i]< 0x8000:
            tree.insert("", i, text=i, values=int(reg[i]))
        else:
            tree.insert("", i, text=i, values=int(reg[i]-0x10000))



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
    tree.heading('#0', text="Reg Address", anchor=W)
    tree.heading('#1', text="Reg Value", anchor=W)

    RefereshTree(tree, start_address, reg_num, reg)

    tree.pack(side=TOP, fill=X)
    # tree.after(1000, RefereshTree(tree, start_address, reg_num, reg))


def ShowTable(start_address, reg_num, reg):
    # global list_hold_reg
    # create new window
    table = Toplevel()
    table.title("Holding Registers")
    table.geometry("400x1400")
    ShowTree(table, start_address, reg_num, reg)


def ShowSingleTable(start_address, reg):
    # create new window
    table = Toplevel()
    table.title("Read 4 Bytes")
    table.geometry("400x200")

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
    tree.heading('#0', text="Reg Address", anchor=W)
    tree.heading('#1', text="Reg Value", anchor=W)

    tree.insert("", 0, text=start_address, values=int((reg[start_address] << 16) + reg[start_address + 1]))

    tree.pack(side=TOP, fill=X)
    # tree.after(1000, RefereshTree(tree, start_address, reg_num, reg))
