import serial
import serial.tools.list_ports
import struct
import time
comPorts = list(serial.tools.list_ports.comports())
activeComPorts = []

for i in comPorts:
    l = str(i).split()
    if l[2] == 'Arduino':
        activeComPorts.append(l[0])

for comPort in activeComPorts:
    ser = serial.Serial(comPort, 19200)
    print(ser)
while True:
    print(ser.read_all())
