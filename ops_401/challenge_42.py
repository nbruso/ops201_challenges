# OPS401D10  Ops Challenge 42
# 03/05/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source:https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-42/challenges/DEMO.md; https://chat.openai.com/share/b3155b6b-02cd-4c94-ad02-d2c3e3709845

#!/usr/bin/python3

# Import the nmap module
import nmap

# Create a nmap scanner object
scanner = nmap.PortScanner()

# Print header
print("Nmap Automation Tool")
print("--------------------")

# Prompt user for IP address to scan
ip_addr = input("IP address to scan: ")  # Asking the user to input the IP address to be scanned
print("The IP you entered is: ", ip_addr)  # Printing the entered IP address

# TODO: Determine why this line is here.
type(ip_addr)  # This line doesn't have any apparent purpose.

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3)              \n""")  # Providing options for the user to select a scan type
print("You have selected option: ", resp)  # Printing the selected option

range = '1-50'

# TODO: Prompt the user to type in a port range for this tool to scan
# This is necessary to allow the user to specify which ports should be scanned.
port_range = input("Enter port range (e.g., 1-100): ")

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())  # Printing the Nmap version
    scanner.scan(ip_addr, port_range, '-v -sS')  # Initiating SYN ACK scan on the provided IP address and port range
    print(scanner.scaninfo())  # Printing scan information
    print("Ip Status: ", scanner[ip_addr].state())  # Printing IP address status
    print(scanner[ip_addr].all_protocols())  # Printing protocols detected
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())  # Printing open TCP ports
elif resp == '2':
    # UDP Scan
    print("Nmap Version: ", scanner.nmap_version())  # Printing the Nmap version
    scanner.scan(ip_addr, port_range, '-v -sU')  # Initiating UDP scan on the provided IP address and port range
    print(scanner.scaninfo())  # Printing scan information
    print("Ip Status: ", scanner[ip_addr].state())  # Printing IP address status
    print(scanner[ip_addr].all_protocols())  # Printing protocols detected
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())  # Printing open UDP ports
elif resp == '3':
    # Custom Scan
    custom_command = input("Enter custom Nmap command: ")  # Prompting the user to enter a custom Nmap command
    print("Nmap Version: ", scanner.nmap_version())  # Printing the Nmap version
    scanner.scan(ip_addr, port_range, custom_command)  # Initiating custom scan on the provided IP address and port range
    print(scanner.scaninfo())  # Printing scan information
    print("Ip Status: ", scanner[ip_addr].state())  # Printing IP address status
    print(scanner[ip_addr].all_protocols())  # Printing protocols detected
    # Note: The keys might vary depending on the output of the custom command
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())  # Printing open ports based on the custom scan
else:
    # Handle invalid input
    print("Please enter a valid option")  # Notifying the user to enter a valid option if the input is not recognized
