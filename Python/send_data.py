import serial
import struct
import time
ser = serial.Serial('COM3', 19200)
print(ser)
while True:
    if ser.read().hex() == 'ff':
        byte = []
        scale = 16
        num_of_bits = 8
        light = 0
        temp = 0
        distance = 0
        light2 = 0
        bit_controle = 0
        binary_value = ""
        for i in range(4):
            binary_value = binary_value + str(bin(int(ser.read().hex(), scale))[2:].zfill(num_of_bits))
        binary_value = str(binary_value)
        light = binary_value[0:2]
        light = light[::-1]
        temp = binary_value[10:20]
        temp = temp[::-1]
        distance = binary_value[2:10]
        distance = distance[::-1]
        light2 = binary_value[20:27]
        light2 = light2[::-1]
        bit_controle = binary_value[27:]
        bit_controle = bit_controle[::-1]
        temp = int(temp, 2)
        light2 = int(light2, 2)
        distance = int(distance, 2)
        light = int(light, 2)
        bit_controle = int(bit_controle, 2)
        print("Temperatuur: "+str(temp), "Lichtsensor: "+str(light2), "Distance: "+str(distance), "What light: "+str(light), "Controle: "+str(bit_controle))
