# OPS401D10  Ops Challenge 28
# 02/14/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source: https://dotnettutorials.net/lesson/logging-module-in-python/; https://docs.python.org/3/howto/logging.html#logging-basic-tutorial; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-26/challenges/DEMO.md;https://chat.openai.com/share/5183f95d-c44b-4361-b6ad-5f9f0a77e87b 

#!/usr/bin/env python3

import logging  # Importing the logging module for handling logs
import paramiko  # Importing the paramiko module for SSH functionality

# Configuring logging: setting up basic configuration for logging to a file ('ssh_attempts.log'),
# with logging level set to INFO, and defining log message format
logging.basicConfig(filename='ssh_attempts.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ssh_connect(host, username, password):
    # Creating an SSHClient instance
    ssh = paramiko.SSHClient()
    # Setting the missing host key policy
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Attempting SSH connection
        ssh.connect(host, port=22, username=username, password=password)
        # Closing the SSH connection
        ssh.close()
        # Returning True if connection is successful
        return True
    except paramiko.AuthenticationException:
        # Handling authentication failure, logging error, and returning False
        logging.error(f"Failed SSH attempt: Authentication failed for {username}@{host}")
        return False
    except paramiko.SSHException as e:
        # Handling other SSH exceptions, logging error, and returning False
        logging.error(f"SSH error occurred: {e}")
        return False

def main():
    # Prompting user for hostname
    host = input("Enter hostname: ")
    # Prompting user for username
    username = input("Enter username: ")
    # Prompting user for password
    password = input("Enter password: ")
    
    if ssh_connect(host, username, password):
        # Printing success message if connection is successful
        print("SSH connection successful")
    else:
        # Printing failure message if connection fails
        print("SSH connection failed. Check logs for details.")

if __name__ == "__main__":
    # Calling the main function directly at the end of the script
    main()
