# LIBS USED:    matplotlib
#               numpy
#               pyserial

import time
import serial.tools.list_ports

arduinos = []
activeComPorts = []
distance_gemiddelde = [0, 0, 0, 0, 0]
light_gemiddelde = [0, 0, 0, 0, 0]
temp_gemiddelde = [0, 0, 0, 0, 0]
total_data = [[], [], [], [], []]
zonnescherm_status = [-1,-1,-1,-1,-1]
zonnescherm_doel = 0
aantal_rondes = 0
aantal_loop = 0
open_of_dicht = 0
current_graph = -1
current_config_setting = -1
min_length = 20
max_length = 100

#setup the arduino's and connects to them
def setup_arduinos():
    com_ports = list(serial.tools.list_ports.comports())
    for i in com_ports:
        l = str(i).split()
        if l[0] not in activeComPorts:
            activeComPorts.append(l[0])
            ser = serial.Serial(l[0], 19200)
            time.sleep(1)
            arduinos.append(ser)

#calculates the mean in python with all the things in a list
def bereken_gemiddelde(lijst, ding, hoeveelste, aantal_voor_gemiddelde):
    aantal_voor_gemiddelde = -aantal_voor_gemiddelde
    lijst = lijst[ding][aantal_voor_gemiddelde:]
    aantal = len(lijst)
    gemiddelde = 0
    if aantal == 0:
        aantal = 1
    for i in lijst:
        gemiddelde += i[hoeveelste]
    gemiddelde = gemiddelde / aantal
    return gemiddelde


def binary_to_data(binary_value):
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
    data = [light, distance, temp, light2, bit_controle]
    return data


def loop_data():
    global arduinos, aantal_rondes, binary_value, light_gemiddelde, temp_gemiddelde, distance_gemiddelde, total_data
    ding = 0
    if len(arduinos) > 0:
        for arduino in arduinos:
            print(arduino.in_waiting)
            waarde = arduino.read().hex()
            if waarde == 'ff':
                scale = 16
                num_of_bits = 8
                binary_value = ""
                for i in range(5):
                    binary_value = str(binary_value) + str(
                        bin(int(arduino.read().hex(), scale))[2:].zfill(num_of_bits))
                if str(binary_value[:8]) == "11111111":
                    binary_value = str(binary_value[8:])
                    binary_value = str(binary_value) + str(
                        bin(int(arduinos[ding].read().hex(), scale))[2:].zfill(num_of_bits))

                data = binary_to_data(binary_value)
                total_data[ding].append(data)

                distance_gemiddelde[ding] = bereken_gemiddelde(total_data, ding, 1, 5)
                light_gemiddelde[ding] = bereken_gemiddelde(total_data, ding, 3, 5)
                temp_gemiddelde[ding] = bereken_gemiddelde(total_data, ding, 2, 5)
                total_data[ding].append(data)
                ding += 1
                aantal_rondes += 1
                if aantal_rondes > 3:
                    setup_arduinos()
                    aantal_rondes = 0
            # except serial.serialutil.SerialException:
            #     aantal = 0
            #     activeComPorts.remove(arduino.name)
            #     for i in arduinos:
            #         if i.name == arduino.name:
            #             arduinos.pop(aantal)
            #         aantal += 1
            #
            #     arduino.close()
            # except ValueError:
            #     aantal = 0
            #     activeComPorts.remove(arduino.name)
            #     for i in arduinos:
            #         if i.name == arduino.name:
            #             arduinos.pop(aantal)
            #         aantal += 1
            #     arduino.close()
    else:
        setup_arduinos()


def loop_loop():
    setup_arduinos()
    aantal_loop = 0
    global zonnescherm_status
    while 1:
        loop_data()
        check_zonnescherm()

def open_zonnescherm(aantal = None):
    if aantal == None and current_config_setting == 0:
        aantal = current_graph
        print("Je zet nu arduino " + str(aantal+1) + " aan")
    elif(aantal == None):
        print(current_config_setting)
    else:
        open_of_dicht = 1
        global zonnescherm_status
        zonnescherm_status[aantal] = 1
        i = arduinos[aantal]
        i.write(bytearray(b'\x02'))


def close_zonnescherm(aantal = None):
    if aantal == None and current_config_setting == 0:
        aantal = current_graph
        print("Je zet nu arduino " + str(aantal+1) + " uit")
    elif(aantal == None):
        print("")
    else:
        open_of_dicht = 2
        global zonnescherm_status
        zonnescherm_status[aantal] = 2
        i = arduinos[aantal]
        i.write(bytearray(b'\x01'))

def set_current_graph(ding, ding2):
    global current_graph, current_config_setting
    current_graph = ding
    current_config_setting = ding2

def knipper(aantal):
    global zonnescherm_status
    zonnescherm_status[aantal] = 3
    i = arduinos[aantal]
    i.write(bytearray(b'\x03'))

def check_zonnescherm():
    aantal = 0
    for i in arduinos:
        distance = distance_gemiddelde[aantal]
        if distance > max_length: # ik heb geen idee welke waarde je wilt
            open_zonnescherm(aantal)
        elif distance < min_length:
            close_zonnescherm(aantal)
        else:
            knipper(aantal)
        aantal+=1

# def check_zonnescherm():
#     global zonnescherm_status, zonnescherm_doel
#     if zonnescherm_status == 0:
#         for i in arduinos:
#             i.write(bytearray(b'\x01'))
#     elif zonnescherm_status == 1:
#         for i in arduinos:
#             i.write(bytearray(b'\x02'))
#     elif zonnescherm_status == 2:
#         print(zonnescherm_status, zonnescherm_doel)
#         if zonnescherm_doel == 1 and gemiddelde_gemiddelde_afstand() > 100:
#             zonnescherm_doel = 0
#             zonnescherm_status = 0
#             for i in arduinos:
#                 i.write(bytearray(b'\x01'))
#
#         if zonnescherm_doel == 2 and gemiddelde_gemiddelde_afstand() < 40:
#             zonnescherm_doel = 0
#             zonnescherm_status = 1
#             for i in arduinos:
#                 i.write(bytearray(b'\x02'))


def set_min_max_length(min = None, max = None):
    global min_length, max_length
    min_length = min
    max_length = max

def gemiddelde_gemiddelde_afstand():
    aantal = 0
    totaal = 0
    for i in range(0, len(arduinos)):
        aantal+=1
        totaal+=distance_gemiddelde[i]

    if aantal == 0:
        aantal = 1
    return totaal/aantal

def get_zonnescherm():
    global zonnescherm_status
    return zonnescherm_status

