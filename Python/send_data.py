import serial
import time
ser = serial.Serial()
ser.baudrate = 19200
ser.port = 'COM3'
ser.stopbits = 1
ser.parity = 'N'
ser.timeout = None
ser.bytesize = 8
ser.open()

time.sleep(3)

while 1==1:
    ina = input()
    print(ina.encode())
    ser.write(ina.encode())
