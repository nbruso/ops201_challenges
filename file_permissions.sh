#!/bin/bash

# Script Name:                  Changing File Permissions           
# Author:                       Dominique Bruso
# Date of latest revision:      11/29/2023
# Purpose:                      To practice changing file permissions
# Execution:                    bash file_permissions.sh or ./file_permissions.sh



# Prompt the user for the directory path
read -p "Enter the directory path: " directory_path

# Display the entered directory path
echo "You entered directory path: $directory_path"

# Prompt the user for input permissions number
read -p "Enter the permissions number (e.g., 777): " permissions_number

# Display the entered permissions number
echo "You entered permissions number: $permissions_number"

# Navigate to the directory input by the user and change all files inside it to the input setting
echo "Changing permissions for all files in $directory_path to $permissions_number"
chmod -R "$permissions_number" "$directory_path"

# Prints to the screen the directory contents and the new permissions settings of everything in the directory.
echo "Here are the updated permissions"
ls -al "$directory_path"

# sources: https://chat.openai.com/share/c2232e16-a527-4be4-a4d8-5e96d2ee222b; https://github.com/codefellows/seattle-ops-301d14/blob/main/class-03/challenges/DEMO.md