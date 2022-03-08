import os
import platform
import shutil
import subprocess
import time


class Commands:
    def __init__(self):
        pass

    def ver(self):
        print("doogh shell version 0.12")

    def help(self):
        print("""
        ver
        neofetch
        help
        sum
        random-number
        time
        whatos
        restart
        os-ver
        shutdown
        webbrowser
        pdm
        ls
        locate
        bash
        exit
        """)

    def sum(self):
        while True:
            print("enter the numbers to add")
            num1 = int(input("num1 > "))
            num2 = int(input("num2 > "))
            print(num1 + num2)
            break

    def time(self):
        print(time.ctime())

    def whatos(self):
        print(platform.platform())

    def restart(self):
        if platform.system() == "Linux":
            os.system("reboot")
        elif platform.system() == "nt":
            os.system("shutdown -r -t 0")

    def randint(self):
        print(random.randint(1, 100))

    def os_version(self):
        print(*platform.uname())

    def shutdown(self):
        if platform.system() == "Linux":
            os.system("shutdown -h now")
        elif platform.system() == "nt":
            os.system("shutdown -s -t 0")

    def webbrowser(self):
        print("enter the url")
        url = input("url > ")
        if platform.system() == "Linux":
            os.system("xdg-open " + url)
        elif platform.system() == "nt":
            os.system("start " + url)

    def ping(self):
        if platform.system() == "Linux":
            os.system("ping -c 4 google.com")
        elif platform.system() == "nt":
            subprocess.call(["ping", "-n", "4", "google.com"])

    def ls (self,argv):
        if platform.system() == "Linux":
            args = 'ls'
            os.system("xdg-open " + url)
        elif platform.system() == "nt":
            args = 'dir'
            os.system("start " + url)