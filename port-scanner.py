#!/bin/python3

import sys  # системные функции и параметры
from datetime import datetime as dt  # присвоить псевданим
import socket

# Define a target
if len(sys.argv) == 3 or 4:  # проверка на то, что в консоли комманда 'python3' сопровождается 3(4) аргументами: название_файла и айпи и порт (и порт)
    target = socket.gethostbyname(sys.argv[1])  # превратить второй аргумент состоящий из текстовой строки в IPv4
else: 
    print("Команда должна состоять из Трех(четырех) аргументов! \n Синтаксис: python3 port-scanner.py <ip> port (port)")
    sys.exit()
    
if len(sys.argv) == 3:
    port2 = int(sys.argv[2]) + 1
else:
    port2 = int(sys.argv[3]) + 1

# Add a banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(dt.now()))
print("-" * 50)

try:
    for port in range(int(sys.argv[2]), port2): # проверить порты в диапозоне [port-port2]
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # определяем, что у некоторой 's' будет айпи и порт
        socket.setdefaulttimeout(1)  # значение типа float
        result = s.connect_ex((target, port))  # установить соединение. Если это произойдет, то вернется "0"
        print("Checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:  # нажатие кнопки прерывания (Ctrl+C or Del)
    print("Прекращена работа проги пользователем")
    sys.exit()

except socket.gaierror:
    print("Hostname couldn't be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
