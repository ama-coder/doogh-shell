#parch doogh shell
import subprocess
import platform
import os
import time
import sys
import random
print("Welcome to doogh shell version 0.12 made for parch GNU/Linux")
while True:
    code = input("doogh@parch:~$ ")
    if code == 'ver':
        print("doogh shell version 0.12")
    if code == 'neofetch':
        subprocess.call(['neofetch'])
    if code == 'help':
        print("the commands are ver, neofetch, help, sum ,random-number , whatos , restart , shutdown,os-ver ,pdm ,ls ,ping , webbrowser ,bash ,exit")
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
    if code == 'os-ver':
        print(platform.platform() +' '+platform.release()+' '+platform.version()+' '+platform.machine()+' '+platform.processor() )
    if code == 'shutdown':
        if platform.system() == 'Linux':
            os.system('shutdown -h now')
        if platform.system() == 'Windows':
            os.system('shutdown -s -t 0')
    if code == 'webbrowser':
        while True:
            if platform.system() == 'Linux':
                print("enter the url")
                url = input("url > ")
                os.system('xdg-open '+url)
                break
            if platform.system() == 'Windows':
                print("enter the url")
                url = input("url > ")
                os.system('start '+url)
                break
    if code == 'pdm':
        while True:
            if os.system() == 'Linux':
                print("enter the url")
                url = input("url > ")
                os.system('xdg-open '+url)
                break
            if os.system() == 'Windows':
                print("enter the url")
                url = input("url > ")
                os.system('start '+url)
                break
    if code == 'ls':
        if platform.system() == 'Linux':
            os.system('ls')
        if platform.system() == 'Windows':
            os.system('dir')
    if code == 'locate':
        if platform.system() == 'Linux':
            os.system('locate')
        if platform.system() == 'Windows':
            print("not supported on windows :)")
    if code == 'ping':
        if platform.system() == 'Linux':
            os.system('ping -c 4 google.com')
        if platform.system() == 'Windows':
            subprocess.call(['ping', '-n', '4', 'google.com'])
    if code == 'bash':
        while True:
            if platform.system() == 'Linux':
                os.system('bash')
                break
            if platform.system() == 'Windows':
                os.system('powershell')
                break
    if code == 'exit':
        print(
            "Thank you for using doogh shell, have a nice day!")
        sys.exit()
