import serial
import serial.tools.list_ports
import struct
import time

for i in comPorts:
    l = str(i).split()
    activeComPorts.append(l[0])

for comPort in activeComPorts:
    ser = serial.Serial(comPort, 19200)
    time.sleep(3)
    test = bytearray(b'\xf3')
    ser.write(test)
    if ser.read() == bytearray(b'\xf3'):
        arduinos.append(ser)
