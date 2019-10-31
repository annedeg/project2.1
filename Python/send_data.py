import serial
import serial.tools.list_ports
import struct
import time
comPorts = list(serial.tools.list_ports.comports())
comPort = ''

for i in comPorts:
    l = str(i).split()
    if l[2] == 'Arduino':
        comPort = l[0]

ser = serial.Serial(comPort, 19200)
print(ser)
while True:
    print(ser.read_all())
