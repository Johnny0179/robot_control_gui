import threading
import time
from tkinter import *

import modbus as mb
import table

'''global varaibles'''
# empty tuple
list_hold_reg = []
stop_flag = False

root = Tk()
root.title('Robot Control GUI')
# root.iconbitmap("/home/johnny/work/python/robot_control_gui/ico/icon.ico")
root.geometry("1200x600")

# dress label
# mbAddressLabel = Label(root, text="modbus slave address:", fg="black", bg="white").grid(row=1, column=0)
mbAddressLabel = Label(root, text="Modbus slave address").grid(
    row=1, column=0, sticky='nw')
mbAddressEntry = Entry(root, width=10, bg="white", fg="purple")
mbAddressEntry.insert(END,'10.60.2.100')
mbAddressEntry.grid(row=1, column=1)

# Port label
mbPortLabel = Label(root, text="Modbus slave port").grid(
    row=2, column=0, sticky='nw')
mbPortEntry = Entry(root, width=10, bg="white", fg="purple")
mbPortEntry.insert(END,'1502')
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

def ModbusConnect():
    # start button
    global mb_server
    print("connect")
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


mbConnectButton = Button(root, text="Connect", bg="gray",
                         command=ModbusConnect, padx=6, pady=6)
mbConnectButton.grid(row=1, column=2, sticky='nw')

mbStartButton = Button(root, text="Start Poll", bg="gray",
                       command=ModbusPoll, padx=6, pady=6)
mbStartButton.grid(row=1, column=3, sticky='nw')


def ModbusStopPoll():
    global stop_flag
    stop_flag = True


# Disconnect button
mbStopPollButton = Button(root, text="Stop Poll", bg="gray",command=ModbusStopPoll, padx=6, pady=6)
mbStopPollButton.grid(row=1, column=4, sticky='nw')

# ModbusSlaveAddressLabel.grid(row=0, column=0)

# draw table


# read holding registers button
mbShowButton = Button(root, text="Read Registers",
                      bg="gray", command=lambda: table.ShowTable(int(mbHoldRegisterStartAddressEntry.get()), int(
        mbHoldRegisterNumEntry.get()), list_hold_reg), padx=6, pady=6)
mbShowButton.grid(row=3, column=2, sticky='nw')

# plot figure function


# plot figure button
mbPlotButton = Button(root, text="Plot Figure",
                      bg="gray", command=table.ShowTable, padx=6, pady=6)
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
    root, text="Write Hold Register", bg="gray",
    command=lambda: WriteReg(int(mbHoldRegisterWriteAddressEntry.get()), int(
        mbHoldRegisterWriteValueEntry.get())), padx=6, pady=6)
mbWriteHoldButton.grid(row=5, column=2, sticky='nw')

root.mainloop()

# main function
# if __name__ == "__main__":
