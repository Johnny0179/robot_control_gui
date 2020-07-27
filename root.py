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
mbHoldRegisterStartAddressLabel = Label(root, text="Hold Register Start Address")
mbHoldRegisterStartAddressLabel.grid(row=3, column=0)
# read holding register entry
mbHoldRegisterStartAddressEntry = Entry(root, width=10)
mbHoldRegisterStartAddressEntry.grid(row=3, column=1)

# read holding register number label
mbHoldRegisterNumLabel = Label(root, text="Hold Register Number")
mbHoldRegisterNumLabel.grid(row=4, column=0)
# read holding register number entry
mbHoldRegisterNumEntry = Entry(root, width=10)
mbHoldRegisterNumEntry.grid(row=4, column=1)

# write holding register address label
mbHoldRegisterWriteAddressLabel = Label(root, text="Write Hold Register Address")
mbHoldRegisterWriteAddressLabel.grid(row=5, column=0)
# write holding register address entry
mbHoldRegisterWriteAddressEntry = Entry(root, width=10)
mbHoldRegisterWriteAddressEntry.grid(row=5, column=1)

# write holding register data label
mbHoldRegisterWriteDataLabel = Label(root, text="Write Hold Register data")
mbHoldRegisterWriteDataLabel.grid(row=6, column=0)
# write holding register address entry
mbHoldRegisterWriteDataEntry = Entry(root, width=10)
mbHoldRegisterWriteDataEntry.grid(row=6, column=1)

# empty tuple
list_hold_reg = []

def ModbusStart():
    # start button
    # mbStartButton = Button(root, text="Modbus Start", bg="gray", padx=6, pady=6).grid(row=6, column=0)
    def ModbusFun():
        mb_server = mb.ModbusServer(mbAddressEntry.get(), int(mbPortEntry.get()), 100, 1)
        global list_hold_reg
        list_hold_reg = list(mb_server.poll())
        # while 1:
        #     # global list_hold_reg
        #     # list_hold_reg = list(mb_server.poll())
        #     time.sleep(1)

    mbStartButton = Button(root, text="Start", bg="gray", command=ModbusFun, padx=6, pady=6)
    mbStartButton.grid(row=1, column=2)


# create start button thread
mbStartThread = threading.Thread(target=ModbusStart, args=[])
mbStartThread.setDaemon(True)
mbStartThread.start()

# pause button
mbPauseButton = Button(root, text="Pause", bg="gray", padx=6, pady=6)
mbPauseButton.grid(row=2, column=2)
# ModbusSlaveAddressLabel.grid(row=0, column=0)




def ShowTable():
    # create new window
    tb.Table(int(mbHoldRegisterStartAddressEntry.get()), int(mbHoldRegisterNumEntry.get()), tuple(list_hold_reg))


# read holding registers button
mbShowButton = Button(root, text="Read Registers", bg="gray", command=ShowTable, padx=6, pady=6)
mbShowButton.grid(row=3, column=2)

# write hold register button
mbWriteHoldButton = Button(root, text="Write Hold Register", bg="gray", command=ShowTable, padx=6, pady=6)
mbWriteHoldButton.grid(row=5, column=2)

# main function
# if __name__ == "__main__":

root.mainloop()
