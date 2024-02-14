# OPS401D10  Ops Challenge 27
# 02/13/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source: https://dotnettutorials.net/lesson/logging-module-in-python/; https://docs.python.org/3/howto/logging.html#logging-basic-tutorial; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-26/challenges/DEMO.md;https://chat.openai.com/share/5183f95d-c44b-4361-b6ad-5f9f0a77e87b 
#!/usr/bin/env python3
# ^ Shebang line specifying the interpreter to use

import logging
import paramiko
import sys
# ^ Importing necessary modules: logging, paramiko, sys

logging.basicConfig(filename='ssh_attempts.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# ^ Configuring logging: setting up basic configuration for logging to a file ('ssh_attempts.log'),
#   with logging level set to INFO, and defining log message format

logger = logging.getLogger("ssh_attempts")
# ^ Creating a logger object named "ssh_attempts"

def ssh_connect(host, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ^ Creating an SSHClient instance and setting the missing host key policy
    
    try:
        ssh.connect(host, port=22, username=username, password=password)
        ssh.close()
        return True
        # ^ Attempting SSH connection and returning True if successful
    except paramiko.AuthenticationException:
        logger.error(f"Failed SSH attempt: Authentication failed for {username}@{host}")
        return False
        # ^ Handling authentication failure, logging error, and returning False
    except paramiko.SSHException as e:
        logger.error(f"SSH error occurred: {e}")
        return False
        # ^ Handling other SSH exceptions, logging error, and returning False

def main():
    host = input("Enter hostname: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    # ^ Prompting user for hostname, username, and password
    
    if ssh_connect(host, username, password):
        print("SSH connection successful")
    else:
        print("SSH connection failed. Check logs for details.")
    # ^ Calling ssh_connect function with user-provided credentials and printing success or failure message

main()  # Calling the main function directly at the end of the script

# 