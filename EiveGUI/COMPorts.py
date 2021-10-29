# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
try:
    import tkinter as tk
    import time
    import serial
    import serial.tools.list_ports
    import sys
    import os
    from datetime import datetime

except Exception as e:
    print("The library {}".format(e))

#List of ports Function

def listOfPorts():
    list_of_ports = (serial.tools.list_ports.comports())
    initial_list = []
    for port in list_of_ports:
        initial_list.extend(port)
        # print(port)
    # print(initial_list)

    sub = "COM"
    com_ports = []
    for text in initial_list:
        if sub in text:
            com_ports.append(text)
            # print(text)
    # print(com_ports)

    port_list = com_ports[0::2]
    port_list.sort()
    return port_list

def initialConnection(comports):
    return 0


def ATCommands(port_number, command):
    return 0