 # OPS401D10  Ops Challenge 01
# 01/09/2024
# Dominique Bruso
# source: https://github.com/codefellows/seattle-cybersecurity-401d10/tree/main/class-02/challenges



# Import necessary modules
import datetime  # Import the datetime module to work with timestamps
import os        # Import the os module for executing system commands
import time      # Import the time module for introducing pauses
# These lines import the necessary modules for the script. datetime is used for working with timestamps, os for executing system commands, and time for introducing pauses.

# Define the target IP address
target_ip = "192.168.1.1"  # Replace with the actual IP address you want to monitor
# This line defines a variable target_ip and assigns the IP address "192.168.1.1" to it. You should replace this with the actual IP address you want to monitor.

# Main loop for continuous monitoring
while True:  # Infinite loop for continuous monitoring
    try:  # Try block to catch exceptions during execution

        # Get the current timestamp
        timestamp = datetime.datetime.now()
        # This line uses the datetime module to get the current date and time, storing it in the variable timestamp.

        # Send ICMP packet using subprocess module
        response = os.system("ping -c 1 " + target_ip)
        # This line uses the os module to execute the ping command (os.system("ping -c 1 " + target_ip)) and captures the response in the variable response. The -c 1 flag ensures only one ping is sent.

        # Evaluate the response and update the status variable
        success = response == 0
        # This line checks if the response is 0, which indicates a successful ping. The result is stored in the success variable.

        # Print the status, timestamp, and destination IP
        print(f"{timestamp} Network {'Active' if success else 'Inactive'} to {target_ip}")
        # This line prints the status, timestamp, and destination IP to the console. The 'Active' or 'Inactive' is determined based on the success of the ping.

    except Exception as e:
        # Handle exceptions (e.g., if ping command fails)
        print(f"Error: {e}")
        # If an exception occurs in the try block, this except block catches the exception and prints an error message.

    finally:
        # Pause for two seconds before the next iteration
        print("Start:", time.ctime())
        time.sleep(2)
        # The finally block ensures that this part of the code runs regardless of whether an exception occurred or not. It prints the start time and introduces a 2-second pause before the next iteration.
