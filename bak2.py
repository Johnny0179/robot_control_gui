from tkinter import *
import tkinter.ttk as ttk
import modbus as mb
import threading
import table
import time


class Root:
    """empty variables"""

    list_hold_reg = []
    mb_server = None
    # disconnect_flag
    disconnect_flag = False

    def __init__(self):
        self.root = Tk()
        self.root.title('Robot Control GUI')
        self.root.geometry("1000x800")
        self.mb_server = None

        # icon
        # self.root.iconbitmap("/home/johnny/work/python/robot_control_gui/ico/icon.ico")

        # label and entry
        # dress label
        self.mbAddressLabel = Label(self.root, text="Modbus slave address").grid(
            row=1, column=0, sticky='nw')
        self.mbAddressEntry = Entry(
            self.root, width=10, bg="white", fg="purple")
        # self.mbAddressEntry.insert(self,'10.60.2.100')
        self.mbAddressEntry.grid(row=1, column=1)

        # Port label
        self.mbPortLabel = Label(self.root, text="Modbus slave port").grid(
            row=2, column=0, sticky='nw')
        self.mbPortEntry = Entry(self.root, width=10, bg="white", fg="purple")
        # self.mbAddressEntry.insert(0, '1502')
        self.mbPortEntry.grid(row=2, column=1)

        # read holding register label
        self.mbHoldRegisterStartAddressLabel = Label(
            self.root, text="Hold Register Start Address")
        self.mbHoldRegisterStartAddressLabel.grid(row=3, column=0, sticky='nw')
        # read holding register entry
        self.mbHoldRegisterStartAddressEntry = Entry(self.root, width=10)
        self.mbHoldRegisterStartAddressEntry.grid(row=3, column=1)

        # read holding register number label
        self.mbHoldRegisterNumLabel = Label(
            self.root, text="Hold Register Number")
        self.mbHoldRegisterNumLabel.grid(row=4, column=0, sticky='nw')
        # read holding register number entry
        self.mbHoldRegisterNumEntry = Entry(self.root, width=10)
        self.mbHoldRegisterNumEntry.grid(row=4, column=1)

        # write holding register address label
        self.mbHoldRegisterWriteAddressLabel = Label(
            self.root, text="Write Hold Register Address")
        self.mbHoldRegisterWriteAddressLabel.grid(row=5, column=0, sticky='nw')
        # write holding register address entry
        self.mbHoldRegisterWriteAddressEntry = Entry(self.root, width=10)
        self.mbHoldRegisterWriteAddressEntry.grid(row=5, column=1)

        # write holding register data label
        self.mbHoldRegisterWriteValueLabel = Label(
            self.root, text="Write Hold Register Value")
        self.mbHoldRegisterWriteValueLabel.grid(row=6, column=0, sticky='nw')
        # write holding register address entry
        self.mbHoldRegisterWriteValueEntry = Entry(self.root, width=10)
        self.mbHoldRegisterWriteValueEntry.grid(row=6, column=1)

        # buttons

        self.mbConnectButton = Button(self.root, text="Connect", bg="gray",
                                      command=self.modbus_connect(), padx=6, pady=6)
        self.mbConnectButton.grid(row=1, column=2, sticky='nw')

        self.mbStartButton = Button(self.root, text="Start Poll", bg="gray",
                                    command=self.modbus_poll(), padx=6, pady=6)
        self.mbStartButton.grid(row=1, column=3, sticky='nw')
        #
        # # DisConnect button
        # self.mbDisConnectButton = Button(self.root, text="Disconnect",
        #                                  bg="gray", command=self.modbus_disconnect(), padx=6, pady=6)
        # self.mbDisConnectButton.grid(row=2, column=2, sticky='nw')
        #
        # # read holding registers button
        # self.mbShowButton = Button(self.root, text="Read Registers",
        #                            bg="gray",
        #                            command=lambda: table.ShowTable(int(self.mbHoldRegisterStartAddressEntry.get()), int(
        #                                self.mbHoldRegisterNumEntry.get()), self.list_hold_reg), padx=6, pady=6)
        # self.mbShowButton.grid(row=3, column=2, sticky='nw')
        #
        # # plot figure button
        # self.mbPlotButton = Button(self.root, text="Plot Figure",
        #                            bg="gray", command=table.ShowTable, padx=6, pady=6)
        # self.mbPlotButton.grid(row=3, column=3, sticky='nw')
        #
        # # write hold register button
        # self.mbWriteHoldButton = Button(
        #     self.root, text="Write Register", bg="gray",
        #     command=lambda: self.WriteReg(int(self.mbHoldRegisterWriteAddressEntry.get()), int(
        #         self.mbHoldRegisterWriteValueEntry.get())), padx=6, pady=6)
        # self.mbWriteHoldButton.grid(row=5, column=2, sticky='nw')

    def modbus_connect(self):
        # defualt address and port
        print("connect")

        # self.mbAddressEntry.insert(END,'10.60.2.100')
        # self.mbPortEntry.insert(END,'1502')
        # self.mb_server = mb.ModbusServer(self.mbAddressEntry.get(), int(self.mbPortEntry.get()), 100, 1)

    def modbus_disconnect(self):
        self.disconnect_flag = True

    def modbus_fun(self):
        # empty
        if self.mb_server is None:
            pass
        else:
            while not self.disconnect_flag:
                self.list_hold_reg = list(self.mb_server.poll())
                time.sleep(0.01)

    def modbus_poll(self):
        modbus_poll_thread = threading.Thread(target=self.modbus_fun())
        # mbPollThread.setDaemon(True)
        modbus_poll_thread.start()
        modbus_poll_thread.join
    #
    # def WriteReg(self, address, value):
    #     self.mb_server.single_wirte(address, value)
