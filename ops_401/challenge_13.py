# OPS401D10  Ops Challenge 13
# 01/24/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source: https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-13/challenges/DEMO.md

#!/usr/bin/env python3

from scapy.all import *
import ipaddress

# Function to get a list of IP addresses in a network
def list_all_addresses(network):
    try:
        net = ipaddress.ip_network(network)  # Create a network object
        return list(net.hosts())  # Return a list of all hosts in the network
    except ValueError as e:
        print(f"Error: {e}")  # Print error if invalid network format
        return []

# Function to check if a host is up using ICMP echo request
def is_host_up(ip_address):
    icmp_packet = IP(dst=ip_address)/ICMP()  # Create an ICMP packet with destination IP
    response = sr1(icmp_packet, timeout=1, verbose=False)  # Send the packet and wait for response
    return response is not None  # Return True if response is received

# Function to perform TCP port scan
def tcp_port_scan(ip_address, start_port, end_port):
    for port in range(start_port, end_port+1):
        # Create a TCP packet with a random source port and specific destination port
        tcp_packet = IP(dst=ip_address)/TCP(sport=RandShort(), dport=port, flags="S")
        response = sr1(tcp_packet, timeout=1, verbose=False)  # Send the packet and wait for response
        
        if response is not None and response.haslayer(TCP):
            # Check if the response has a TCP layer
            tcp_layer = response.getlayer(TCP)
            if tcp_layer.flags == 0x12:  # Check if the flags are SYN-ACK (0x12)
                print(f"Port {port} is open on {ip_address}")
            # Send a TCP RST packet to politely close the connection
            sr(IP(dst=ip_address)/TCP(sport=RandShort(), dport=port, flags="R"), timeout=1, verbose=False)

def main():
    network = input("Enter the network in CIDR format (e.g., 192.168.1.0/24): ")
    addresses = list_all_addresses(network)  # Get list of IP addresses in the network
    if addresses:
        for address in addresses:
            print(f"Scanning {address}...")
            if is_host_up(str(address)):
                # If host is up, perform TCP port scan on ports 1-1024
                tcp_port_scan(str(address), 1, 1024)
            else:
                print(f"{address} is not responsive.")
    else:
        print("No addresses found or invalid network.")

if __name__ == "__main__":
    main()
