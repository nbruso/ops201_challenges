# OPS401D10  Ops Challenge 12
# 01/23/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source: https://web.archive.org/web/20180826164313/https://infinityquest.com/python-tutorials/generating-a-range-of-ip-addresses-from-a-cidr-address-in-python/; https://chat.openai.com/share/48471212-55c9-46af-a98c-26d5cd1f7239; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-12/challenges/DEMO.md

#!/usr/bin/env python3

# Importing required libraries
from scapy.all import *  # Scapy for network operations
import ipaddress  # Used for handling IP addresses

# Function to get a list of IP addresses in a network
def list_all_addresses(network):
    try:
        # Create a network object from the given network string
        net = ipaddress.ip_network(network)
        # Return a list of all IP addresses in this network
        return list(net.hosts())
    except ValueError as e:
        # If there is an error (like a wrong network format), print the error
        print(f"Error: {e}")
        return []

# Function to scan a range of ports on a specific IP
def scan_ports(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        # Creating a TCP packet with a SYN flag
        packet = IP(dst=ip)/TCP(dport=port, flags='S')
        # Sending the packet and waiting for a response
        response = sr1(packet, timeout=1, verbose=0)
        # Checking if the response contains a TCP layer and SYN-ACK flags
        if response and response.haslayer(TCP) and response.getlayer(TCP).flags & 0x12:
            print(f"Port {port} is open on {ip}")
        else:
            print(f"Port {port} is closed or filtered on {ip}")

# Main function of the script
def main():
    # Ask the user to choose between two modes
    choice = input("Choose mode:\n1. TCP Port Range Scanner\n2. ICMP Ping Sweep\n3. Exit\nEnter choice (1, 2, or 3): ")
    
    if choice == '1':
        # TCP Port Range Scanner functionality
        target_ip = input("Enter the target IP address: ")
        start_port = int(input("Enter the start port number: "))
        end_port = int(input("Enter the end port number: "))
        scan_ports(target_ip, start_port, end_port)

    elif choice == '2':
        # ICMP Ping Sweep
        network = input("Enter the network in CIDR format (e.g., 192.168.1.0/24): ")
        addresses = list_all_addresses(network)
        if addresses:
            print("Performing ICMP Ping Sweep...")
            online_hosts = 0
            for address in addresses:
                packet = IP(dst=str(address))/ICMP()
                response = sr1(packet, timeout=1, verbose=0)
                if response:
                    if response.getlayer(ICMP).type == 3:
                        code = response.getlayer(ICMP).code
                        if code in [1, 2, 3, 9, 10, 13]:
                            print(f"{address} is actively blocking ICMP traffic.")
                        else:
                            print(f"{address} is responding.")
                    else:
                        print(f"{address} is up.")
                        online_hosts += 1
                else:
                    print(f"{address} is down or unresponsive.")
            print(f"Total number of online hosts: {online_hosts}")
        else:
            print("No addresses found or invalid network.")

    elif choice == '3':
        # Exit the program
        print("Exiting the program.")
    
    else:
        # Invalid choice entered
        print("Invalid choice.")

# This makes sure the script runs the main function when you run the script
if __name__ == "__main__":
    main()
