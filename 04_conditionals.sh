#!/bin/bash

# Script Name:                  Ops Challenge 04: Conditionals           
# Author:                       Dominique Bruso
# Date of latest revision:      11/29/2023
# Purpose:                      To practice conditionals
# Execution:                    bash 04_conditionals.sh or ./04_conditionals.sh
# Sources                       https://chat.openai.com/share/0f6fc8b6-0734-4fc5-82cc-821a2c26ed57; https://linuxhint.com/bash_conditional_statement/

# Declaration of variables
ip_addresses=$(ip addr show | grep 'inet' | awk '{print $2}')

# Create a bash script that launches a menu system with the following options:
while true; do
    clear   

    # Hello world (prints “Hello world!” to the screen)
    echo "Hello world! Welcome to the menu"
    clear

    # Ping self (pings this computer’s loopback address)
    echo "Checking connectivity"
    ping -c 4 127.0.0.1
    if [ $? -eq 0 ]; then
        echo "Ping successful."
    else
        echo "Ping failed."
    fi
    read -p "Press Enter to continue"

    # IP info (print the network adapter information for this computer)
    clear
    echo "Verifying IP address"
    echo "IP addresses: $ip_addresses"
    read -p "Press Enter to continue"

    # Menu options
    while true; do
        clear
        echo "What is your favorite season? Please enter only the numerical value"
        echo "1. Summer"
        echo "2. Spring"
        echo "3. Fall"
        echo "4. Winter"
        echo "5. Exit"
        read choice

        if [[ $choice == 1 ]]; then
            echo "Summer - because sunburns are a small price to pay for fun in the sun."
            read -p "Press Enter to continue"
        elif [[ $choice == 2 ]]; then
            echo "The best season for spring cleaning, obviously!"
            read -p "Press Enter to continue"
        elif [[ $choice == 3 ]]; then
            echo "Fall - because it's the only season where 'falling' is encouraged!"
            read -p "Press Enter to continue"
        elif [[ $choice == 4 ]]; then
            echo "Winter - when your coffee gets cold almost as fast as your nose."
            read -p "Press Enter to continue"
        elif [[ $choice == 5 ]]; then
            echo "Goodbye!"
            exit 0
        else
            echo "Invalid choice"
            read -p "Press Enter to continue"
        fi
    done  # End of inner while loop
done  # End of outer while loop
