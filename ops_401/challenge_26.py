# OPS401D10  Ops Challenge 26
# 02/12/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source: 

#!/usr/bin/env python3


# Import libraries
import logging
import os

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

# Create the log object
log = logging.getLogger("my_logger")

# Configure my logging object
logging.basicConfig(logging.basicConfig(filename='sssh_attempts.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'))

log.critical("CRITICAL ALERT")
log.warning("WARNING:SSH ATTEMPT")

#Define a function
def ssh_alerts():
log.critical("CRITICAL ALERT")
log.warning("WARNING:SSH ATTEMPT")

#Call our function
ssh_alerts()
