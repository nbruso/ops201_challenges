# OPS401D10  Ops Challenge 36
# 02/25/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source:https://www.hackingarticles.in/multiple-ways-to-banner-grabbing/; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-36/challenges/DEMO.md;https://chat.openai.com/share/469da274-a644-432a-b9cf-f8ab3e207708 

import subprocess  # Importing the subprocess module to run shell commands

def prompt_user(message):
    return input(message)  # Function to prompt the user for input and return the entered value

def banner_grabbing_with_netcat(target_address, port):
    command = f"nc {target_address} {port}"  # Constructing the Netcat command
    try:
        result = subprocess.run(command.split(), capture_output=True, text=True)  # Running the Netcat command and capturing the output
        print(result.stdout)  # Printing the output of the Netcat command
    except Exception as e:
        print(f"Error: {e}")  # Handling any errors that occur during execution

def banner_grabbing_with_telnet(target_address, port):
    command = f"telnet {target_address} {port}"  # Constructing the Telnet command
    try:
        result = subprocess.run(command.split(), capture_output=True, text=True)  # Running the Telnet command and capturing the output
        print(result.stdout)  # Printing the output of the Telnet command
    except Exception as e:
        print(f"Error: {e}")  # Handling any errors that occur during execution

def main():
    target_address = prompt_user("Enter the target URL or IP address: ")  # Prompting the user to enter the target address
    port = prompt_user("Enter the port number: ")  # Prompting the user to enter the port number

    print("Performing banner grabbing with Netcat:")  # Informing the user about the action being performed
    banner_grabbing_with_netcat(target_address, port)  # Calling the function to perform banner grabbing with Netcat

    print("\nPerforming banner grabbing with Telnet:")  # Informing the user about the action being performed
    banner_grabbing_with_telnet(target_address, port)  # Calling the function to perform banner grabbing with Telnet

if __name__ == "__main__":
    main()  # Calling the main function when the script is executed
