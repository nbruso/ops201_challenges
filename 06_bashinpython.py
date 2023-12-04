# The Python module “os” must be utilized.
import os

# At least three variables must be declared and referenced in Python.
username = "JohnDoe"
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