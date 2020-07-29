from tkinter import *
import tkinter.ttk as ttk
import threading


def DrawTable(start_address, reg_num, reg):
    table = Toplevel()
    table.title("Holding Registers")
    table.geometry("600x1400")

    tree = ttk.Treeview(table, height=50)  # #创建表格对象,default 50 rows

    # style
    s = ttk.Style(table)
    s.configure('Treeview', rowheight=40)

    tree["columns"] = ('#1')  # #定义列
    tree.column('#0', width=30, minwidth=150)
    tree.column('#1', width=30, minwidth=150)
     # tree.column("姓名", width=100)  # #设置列

     # Define Column Headings
    tree.heading('#0', text="Reg Address", anchor=W)
    tree.heading('#1', text="Reg Value", anchor=W)

    # insert rows
    for i in range(start_address, start_address + reg_num):
        tree.insert("", i, text=i, values=reg[i])

    tree.pack(side=TOP, fill=X)
    table.after(1000, DrawTable)

    # def self.TablePoll():
