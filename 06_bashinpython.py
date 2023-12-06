# Script Name:                  Ops Challenge 06: Bash in Python          
# Author:                       Dominique Bruso
# Date of latest revision:      12/04/2023
# Purpose:                      To practice python
# Execution:                    python2 06_bashinpython.py
# Source: https://chat.openai.com/share/f8ad1684-8cb1-434d-8efe-e1cbf022df51


# The Python module “os” must be utilized.
import os

# At least three variables must be declared and referenced in Python.
username = "dominiquebruso"
network_interface = "eth0"
hardware_type = "disk"

# The Python function print() must be used at least three times.
# Print the variables using the print() function
print("Username:", username)
print("Network Interface:", network_interface)
print("Hardware Type:", hardware_type)

# Execute bash commands using os.system with variables
print("\nExecuting Bash Commands:")
os.system("whoami")
os.system("sudo ip a")
os.system("sudo lshw -short")