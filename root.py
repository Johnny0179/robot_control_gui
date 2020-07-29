from tkinter import *
import tkinter.ttk as ttk
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
mbAddressLabel = Label(root, text="Modbus slave address").grid(
    row=1, column=0, sticky='nw')
mbAddressEntry = Entry(root, width=10, bg="white", fg="black")
mbAddressEntry.grid(row=1, column=1)

# Port label
mbPortLabel = Label(root, text="Modbus slave port").grid(
    row=2, column=0, sticky='nw')
mbPortEntry = Entry(root, width=10, bg="white", fg="black")
mbPortEntry.grid(row=2, column=1)

# read holding register label
mbHoldRegisterStartAddressLabel = Label(
    root, text="Hold Register Start Address")
mbHoldRegisterStartAddressLabel.grid(row=3, column=0, sticky='nw')
# read holding register entry
mbHoldRegisterStartAddressEntry = Entry(root, width=10)
mbHoldRegisterStartAddressEntry.grid(row=3, column=1)

# read holding register number label
mbHoldRegisterNumLabel = Label(root, text="Hold Register Number")
mbHoldRegisterNumLabel.grid(row=4, column=0, sticky='nw')
# read holding register number entry
mbHoldRegisterNumEntry = Entry(root, width=10)
mbHoldRegisterNumEntry.grid(row=4, column=1)


# empty tuple
list_hold_reg = []


def ModbusConnect():
    # start button
    global mb_server
    mb_server = mb.ModbusServer(
        mbAddressEntry.get(), int(mbPortEntry.get()), 100, 1)


def ModbusFun():
    global list_hold_reg
    while 1:
        list_hold_reg = list(mb_server.poll())
        time.sleep(0.01)


def ModbusPoll():
    mbPollThread = threading.Thread(target=ModbusFun)
    # mbPollThread.setDaemon(True)
    mbPollThread.start()


mbConnectButton = Button(root, text="Connect Slave", bg="gray",
                         command=ModbusConnect, padx=6, pady=6)
mbConnectButton.grid(row=1, column=2, sticky='nw')

mbStartButton = Button(root, text="Start Poll", bg="gray",
                       command=ModbusPoll, padx=6, pady=6)
mbStartButton.grid(row=1, column=3, sticky='nw')


# # create start button thread
# mbStartThread = threading.Thread(target=ModbusStart, args=[])
# mbStartThread.setDaemon(True)
# mbStartThread.start()

# pause button
mbPauseButton = Button(root, text="Pause", bg="gray", padx=6, pady=6)
mbPauseButton.grid(row=2, column=2, sticky='nw')
# ModbusSlaveAddressLabel.grid(row=0, column=0)

# draw table


def ShowTree(table, start_address, reg_num, reg):
    # global list_hold_reg
    # reg=list_hold_reg
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

    # test
    # reg[0]=reg[0]+1

    # insert rows
    for i in range(start_address, start_address + reg_num):
        tree.insert("", i, text=i, values=reg[i])

    tree.pack(side=TOP, fill=X)
    # tree.after(1000, ShowTree(table, int(mbHoldRegisterStartAddressEntry.get()), int(
    #     mbHoldRegisterNumEntry.get()), tuple(list_hold_reg)))


def ShowTable(start_address, reg_num, reg):
    # create new window
    table = Toplevel()
    table.title("Holding Registers")
    table.geometry("600x1400")

    ShowTree(table, start_address, reg_num, reg)

    table.after(1000, ShowTree(table, int(mbHoldRegisterStartAddressEntry.get()), int(
        mbHoldRegisterNumEntry.get()),  list_hold_reg))


# read holding registers button
mbShowButton = Button(root, text="Read Registers",
                      bg="gray", command=lambda: ShowTable(int(mbHoldRegisterStartAddressEntry.get()), int(
                          mbHoldRegisterNumEntry.get()), list_hold_reg), padx=6, pady=6)
mbShowButton.grid(row=3, column=2, sticky='nw')

# plot figure function


# plot figure button
mbPlotButton = Button(root, text="Plot Figure",
                      bg="gray", command=ShowTable, padx=6, pady=6)
mbPlotButton.grid(row=3, column=3, sticky='nw')

# write holding register address label
mbHoldRegisterWriteAddressLabel = Label(
    root, text="Write Hold Register Address")
mbHoldRegisterWriteAddressLabel.grid(row=5, column=0, sticky='nw')
# write holding register address entry
mbHoldRegisterWriteAddressEntry = Entry(root, width=10)
mbHoldRegisterWriteAddressEntry.grid(row=5, column=1)

# write holding register data label
mbHoldRegisterWriteValueLabel = Label(root, text="Write Hold Register value")
mbHoldRegisterWriteValueLabel.grid(row=6, column=0, sticky='nw')
# write holding register address entry
mbHoldRegisterWriteValueEntry = Entry(root, width=10)
mbHoldRegisterWriteValueEntry.grid(row=6, column=1)


def WriteReg(addr, value):
    mb_server.single_wirte(addr, value)


    # write hold register button
mbWriteHoldButton = Button(
    root, text="Write Hold Register", bg="gray", command=lambda: WriteReg(int(mbHoldRegisterWriteAddressEntry.get()), int(
        mbHoldRegisterWriteValueEntry.get())), padx=6, pady=6)
mbWriteHoldButton.grid(row=5, column=2, sticky='nw')

# main function
if __name__ == "__main__":

    root.mainloop()
