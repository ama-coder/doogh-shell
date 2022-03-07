#parch doogh shell
import subprocess
import platform
import os
import time
import sys
import socket
import random
print("Welcome to doogh shell version 0.11 made for parch GNU/Linux")
while True:
    code = input("User/doogh > ")
    if code == 'ver':
        print("doogh shell version 0.1")
    if code == 'neofetch':
        subprocess.call(['neofetch'])
    if code == 'help':
        print("the commands are ver, neofetch, help, sum ,random-number , whatos , restart , shutdown , ,exit")
    if code == 'sum':
        while True:
            print("enter the numbers to add")
            num1 = int(input("num1 > "))
            num2 = int(input("num2 > "))
            print(num1 + num2)
            break
    if code == 'random-number':
        print(random.randint(1, 100))
    if code == 'time':
        print(time.ctime())
    if code == 'whatos':
        print(platform.platform())
    if code == 'restart':
        if platform.system() == 'Linux':
            os.system('reboot')
        if platform.system() == 'Windows':
            os.system('shutdown -r -t 0')
    if code == 'shutdown':
        if platform.system() == 'Linux':
            os.system('shutdown -h now')
        if platform.system() == 'Windows':
            os.system('shutdown -s -t 0')
    if code == 'exit':
        print(
            "Thank you for using doogh shell, have a nice day!")
        sys.exit()
        )