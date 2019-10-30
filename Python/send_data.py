import serial
import struct
import time
ser = serial.Serial('COM3', 19200)
print(ser)
while True:

    print(ser.read_all())
