# OPS401D10  Ops Challenge 16
# 01/26/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source: https://chat.openai.com/share/21cc496d-08bc-416d-b2a3-c3c5c45ead39; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-16/challenges/DEMO.md

#!/usr/bin/env python3
# The above line is a shebang line which tells the system how to execute
# this script (using Python 3).

import os
from time import sleep  # Import the sleep function from the time module.

# Define a function named 'menu' which contains the main menu logic.
def menu():
    while True:  # Start an infinite loop to show the menu repeatedly.
        # Print menu options to the console.
        print("\nMenu:")
        print("1. Mode 1: Offensive; Dictionary Iterator")
        print("2. Mode 2: Defensive; Password Recognized")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")  # Get user input for the menu choice.

        if choice == '1':  # Check if the user chose option 1.
            file_path = input("Enter the word list file path: ")  # Prompt for file path.
            dictionary_iterator(file_path)  # Call the function to handle dictionary iterator.
        elif choice == '2':  # Check if the user chose option 2.
            password = input("Enter the password to search for: ")  # Prompt for the password to search.
            file_path = input("Enter the word list file path: ")  # Prompt for file path.
            password_recognized(password, file_path)  # Call the function to handle password recognition.
        elif choice == '3':  # Check if the user chose option 3.
            print("Exiting...")  # Print exiting message.
            break  # Break the loop to exit the program.
        else:  # If the user enters an invalid option.
            print("Invalid choice. Please enter a number between 1 and 3.")  # Show an error message.

# Define a function to handle dictionary iterator mode.
def dictionary_iterator(file_path):
    with open(file_path, 'r') as file:  # Open the file in read mode.
        for line in file:  # Iterate over each line in the file.
            word = line.strip()  # Remove any leading/trailing whitespace from the line.
            print(word)  # Print the word.
            sleep(0.5)  # Pause for 0.5 seconds.

# Define a function to handle password recognition mode.
def password_recognized(password, file_path):
    with open(file_path, 'r') as file:  # Open the file in read mode.
        words = file.read().splitlines()  # Read all lines and split them into a list.
    if password in words:  # Check if the entered password is in the list of words.
        print("The password is in the list.")  # Print confirmation message.
    else:  # If the password is not in the list.
        print("The password is not in the list.")  # Print a different message.

# Call the menu function to start the program.
menu()
