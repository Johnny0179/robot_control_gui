from tkinter import *
import tkinter.ttk as ttk
import modbus as mb
import threading
import table
import time


class RootData:
    def __init__(self):
        self.list_hold_reg = []
        self.mb_server = None
        self.disconnect_flag = False
