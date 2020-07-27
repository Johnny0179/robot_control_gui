from tkinter import *
import tkinter.ttk as ttk
import threading


class Table:
    def __init__(self, start_address, reg_num, reg):
        self.table = Toplevel()
        self.table.title("Holding Registors")
        self.table.geometry("600x1400")
        self.tree = ttk.Treeview(self.table,height=50)  # #创建表格对象,fault 50 rows

        # style
        self.s = ttk.Style(self.table)
        self.s.configure('Treeview', rowheight=40)

        self.tree["columns"] = ('#1' ) # #定义列
        self.tree.column('#0', width=30, minwidth=150)
        self.tree.column('#1', width=30, minwidth=150)
        # self.tree.column("姓名", width=100)  # #设置列

        # Define Column Headings
        self.tree.heading('#0', text="Reg Address", anchor=W)
        self.tree.heading('#1', text="Reg Value", anchor=W)

        # insert rows
        for i in range(start_address, start_address + reg_num):
            self.tree.insert("", i, text=i, values=reg[i])

        self.tree.pack(side=TOP, fill=X)

    # def self.TablePoll():
