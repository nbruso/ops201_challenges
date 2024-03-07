# OPS401D10  Ops Challenge 37
# 02/27/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source:# https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/class-44/challenges/DEMO.html; https://docs.python.org/3/library/socket.html
#!/usr/bin/python3

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 10 # TODO: Set a timeout value here.
sockmod.settimeout(timeout)

hostip = input("Enter the hostname: ") # TODO: Collect a host IP from the user.
portno = # input("Enter the port number: ") TODO: Collect a port number from the user, then convert it to an integer data type.
portno = int(portno_str)

def portScanner(portno):
    if sockmod.FUNCTION((hostip, portno)): # TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
        print("Port closed")
    else:
        print("Port open")

portScanner(port)