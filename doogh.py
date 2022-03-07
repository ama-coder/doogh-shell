#parch doogh shell
import subprocess
import time
import platform
import os
print("Welcome to doogh shell version 0.1 made for parch GNU/Linux")
while True:
    code = input("User/doogh > ")
    if code == 'ver':
        print("doogh shell version 0.1")
    if code == 'neofetch':
        subprocess.call(['neofetch'])
    if code == 'help':
        print("the commands are ver, neofetch, help, sum ,exit")
    if code == 'sum':
        while True:
            print("enter the numbers to add")
            num1 = int(input("num1 > "))
            num2 = int(input("num2 > "))
            print(num1 + num2)
            break
    if code == 'exit':
        exit()
