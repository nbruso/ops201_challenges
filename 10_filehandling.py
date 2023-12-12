# Script Name:                  Ops Challenge 10
# Author:                       Dominique Bruso
# Date of latest revision:      12/08/2023
# Purpose:                      To practice python
# Execution:                    python3 10_filehandling.py
# Source:                       https://github.com/codefellows/seattle-ops-301d14/tree/main/class-10/challenges; https://chat.openai.com/share/a00b4222-8df0-4730-9bb4-0614154836af



# create a new .txt file
file_path = "demofile.txt"

# open the file in write mode to create it
with open(file_path, "w") as file:
    # append three lines
    file.write("Hello, World!\n")
    file.write("How are you today?\n")
    file.write("Have a great day!\n")

# open the file in read mode
with open(file_path, "r") as file:
    # print to the screen the first line
    first_line = file.readline()
    print(first_line)

# delete the .txt file
import os
os.remove(file_path)
