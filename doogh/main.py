""" Parch Doogh Shell

What is Doogh?
---
Doogh is a shell for parch GNU/Linux

Doogh features
---
Written in Python
Compatible with Mac OS , nt and Linux
Easy to use for users
Fast, secure, easy

License: GPL-3.0
"""

import os
import platform
import random
import subprocess
import sys
import time

import termcolor as tc
from commands import Commands
from user import host_name, user_home, user_name

while True:
    try:
        code = input(tc.colored(f"{user_name}@{host_name}:~$ ", "green"))
    except EOFError:
        sys.exit(0)
    except KeyboardInterrupt:
        print("")
        continue

    codeln = code.split(" ")

    cmds = Commands()

    if code == "version":
        cmds.version()
    elif code == "help":
        cmds.help()

    elif code == "sum":
        cmds.sum()

    elif code == "random-number":
        cmds.randint()

    elif code == "time":
        cmds.time()

    elif code == "whatos":
        cmds.whatos()

    elif code == "restart":
        cmds.restart()

    elif code == "os_version":
        cmds.os_version()

    elif code == "webbrowser":
        cmds.webbrowser()

    elif code == "ping":
        cmds.ping()

    elif code == "exit":
        print("Thank you for using doogh shell, have a nice day!")
        sys.exit()

    else:
        print(code)
        try:
            os.system(code)
        except:
            print(tc.colored("Command not found.", "red"))
