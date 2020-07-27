from tkinter import *
import modbus as mb
import threading
import table as tb
import time

root = Tk()
root.title('Robot Control GUI')
# root.iconbitmap("/home/johnny/work/python/robot_control_gui/ico/icon.ico")
root.geometry("1000x800")

# dress label
# mbAddressLabel = Label(root, text="modbus slave address:", fg="black", bg="white").grid(row=1, column=0)
mbAddressLabel = Label(root, text="Modbus slave address").grid(row=1, column=0)
mbAddressEntry = Entry(root, width=10, bg="white", fg="black")
mbAddressEntry.grid(row=1, column=1)

# Port label
mbPortLabel = Label(root, text="Modbus slave port").grid(row=2, column=0)
mbPortEntry = Entry(root, width=10, bg="white", fg="black")
mbPortEntry.grid(row=2, column=1)

# read holding register label
mbHoldRegistorStartAddressLabel = Label(root, text="Hold Registor Start Address")
mbHoldRegistorStartAddressLabel.grid(row=3, column=0)
# read holding register label
mbHoldRegistorStartAddressEntry = Entry(root, width=10)
mbHoldRegistorStartAddressEntry.grid(row=3, column=1)

# read holding register label
mbHoldRegistorNumLabel = Label(root, text="Hold Registor Number")
mbHoldRegistorNumLabel.grid(row=4, column=0)
# read holding register label
mbHoldRegistorNumEntry = Entry(root, width=10)
mbHoldRegistorNumEntry.grid(row=4, column=1)

# start button
# mbStartButton = Button(root, text="Modbus Start", bg="gray", padx=6, pady=6).grid(row=0, column=0)
mbStartButton = Button(root, text="Start", bg="gray", padx=6, pady=6)
mbStartButton.grid(row=1, column=2)
# pause button
mbPauseButton = Button(root, text="Pause", bg="gray", padx=6, pady=6)
mbPauseButton.grid(row=2, column=2)
# ModbusSlaveAddressLabel.grid(row=0, column=0)

import random

hold_reg = (1, 3, 4, 7, 2, 8, 3, 8, 0, 2, 56, 767, 235, 45, 67, 12, 1, 2, 3, 4,77, 5, 7, 1,12,34,56,6768,12324,55676,3435435,1244)


# create new thread
# while 1:
#     a = a + 1
#     b = b + 1
#     time.sleep(1)


def Show():
    print(mbAddressEntry.get())


def ShowTable():
    # create new window
    tb.Table(int(mbHoldRegistorStartAddressEntry.get()), int(mbHoldRegistorNumEntry.get()), hold_reg)


def ReadHoldRegistor():
    print(mbAddressEntry.get())


# show button
mbShowButton = Button(root, text="Show Registors", bg="gray", command=ShowTable, padx=6, pady=6)
mbShowButton.grid(row=3, column=2)
#
#
# myButton = Button(root, text="show the input", command=clickbutton, fg="black", bg="gray")
# myButton.pack()

root.mainloop()
