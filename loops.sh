#!/bin/bash

# Script Name:                  Loop test
# Author:                       Dominique Bruso
# Date of latest revision:      10/25/2023
# Purpose:                      To practice making lopps
# Execution:                    bash loops.sh or ./loops.sh
# Declaration of variables

#source: (OpenAI. (2023). ChatGPT (September 25 Version) [Large language model]. https://chat.openai.com


#Declaration of Functions:
while true; do
    # Display running processes
    echo "Running Processes:"
    ps aux

    # Ask the user for a PID to kill
    read -p "Enter the PID of the process you want to terminate (Ctrl + C to exit): " pid

    # Check if the input is a valid number
    if [[ "$pid" =~ ^[0-9]+$ ]]; then
        # Attempt to terminate the process
        kill -15 "$pid"
        if [ $? -eq 0 ]; then
            echo "Process with PID $pid terminated."
        else
            echo "Failed to terminate process with PID $pid."
        fi
    else
        echo "Invalid input. Please enter a valid PID."
    fi

    # Clear the screen for the next iteration (works on Unix-based systems)
    clear
done
#End