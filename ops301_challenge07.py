# Script Name:                  Ops Challenge 07         
# Author:                       Dominique Bruso
# Date of latest revision:      12/05/2023
# Purpose:                      To practice python
# Execution:                    python lab08.py
# Source:                       https://chat.openai.com/share/1b46fadb-7c12-4194-aaf9-f79706a5becc

#!/usr/bin/env python3

# Import libraries
import os

# Declaration of variables
directory_path = None  # Initialize the variable

# Read user input here into a variable
directory_path = input("Enter the directory path: ")

# Declaration of functions
def generate_directory_structure(user_path):
    for (root, dirs, files) in os.walk(user_path):
        # Print the current root directory
        print("==root==")
        print(root)

        # Print the subdirectories in the current root
        print("==dirs==")
        print(dirs)

        # Print the files in the current root
        print("==files==")
        print(files)

# Main
# Pass the variable into the function here
generate_directory_structure(directory_path)
