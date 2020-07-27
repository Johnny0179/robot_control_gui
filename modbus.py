# modbus_tk github address
# https://github.com/ljean/modbus-tk

import time
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import threading


# modbus class
class ModbusServer:
    def __init__(self, slave_address, slave_port, length, time_out):
        self.master = modbus_tcp.TcpMaster(host=slave_address, port=slave_port)
        self.master.set_timeout(time_out)
        self.length = length

    def poll(self):
        while 1:
            # read hold registers 0-(length-1)
            return self.master.execute(1, cst.READ_HOLDING_REGISTERS, 0, self.length)
            # return ? where to store the data
