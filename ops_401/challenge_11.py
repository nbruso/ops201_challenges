# OPS401D10  Ops Challenge 11
# 01/22/2024
# Dominique Bruso
# source: https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-11/challenges/DEMO.md; https://scapy.readthedocs.io/en/latest/introduction.html#; https://chat.openai.com/share/caf39800-6d69-4e3d-ba7d-f4b3b6908996

#!/usr/bin/env python3
# Shebang line for Unix-based systems to execute the script with Python 3

# Run this with sudo
# Comment indicating the script should be run with superuser permissions

import sys
# Importing the sys module for system-specific parameters and functions

from scapy.all import sr1, IP, TCP
# Importing necessary functions and classes from Scapy for packet crafting and sending

host = "192.168.0.161"
# Setting the target host IP address

port_range = [20, 21, 22, 23, 80, 443]
# Defining a range or specific set of ports to scan

# Loop over each port in the port_range
for dst_port in port_range:

    # Sending a TCP SYN packet to each port and waiting for a response
    response = sr1(IP(dst=host)/TCP(dport=dst_port,flags="S"), timeout=1, verbose=0)

    if response:
        # If there is a response

        if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            # If the response has a TCP layer and flags are 0x12 (SYN-ACK), the port is open

            # Sending a TCP RST packet to close the connection gracefully
            sr1(IP(dst=host)/TCP(dport=dst_port,flags="R"), timeout=1, verbose=0)

            # Notifying the user that the port is open
            print(f"Port {dst_port} is open.")
        
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
            # If the response has a TCP layer and flags are 0x14 (RST), the port is closed

            # Notifying the user that the port is closed
            print(f"Port {dst_port} is closed.")

    else:
        # If there is no response, it is assumed the port is filtered and silently dropped

        # Notifying the user that the port is filtered
        print(f"Port {dst_port} is filtered and silently dropped.")

# End of script
# Indicates the end of the script
