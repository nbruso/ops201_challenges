# OPS401D10  Ops Challenge 32
# 02/20/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source: https://docs.python.org/3/library/hashlib.html; https://www.programiz.com/python-programming/examples/hash-file; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-32/challenges/DEMO.md; https://chat.openai.com/share/8f829f60-4e35-4dca-b668-c112785d1a29

#!/usr/bin/env python3

import os  # Import the os module for interacting with the operating system
import hashlib  # Import the hashlib module for generating cryptographic hashes
import datetime  # Import the datetime module for working with dates and times

def search_files():  # Define a function named search_files
    file_name = input("Enter the file name to search for: ")  # Prompt the user to enter the file name to search for
    directory = input("Enter the directory to search in: ")  # Prompt the user to enter the directory to search in

    files_searched = 0  # Initialize a counter for the number of files searched
    hits_found = 0  # Initialize a counter for the number of hits found

    for root, dirs, files in os.walk(directory):  # Recursively walk through the directory tree
        for file in files:  # Iterate over the files in the current directory
            files_searched += 1  # Increment the counter for files searched
            if file == file_name:  # Check if the current file matches the searched file name
                hits_found += 1  # Increment the counter for hits found
                print("Found:", file_name)  # Print a message indicating the file was found
                print("Location:", os.path.join(root, file))  # Print the full path of the found file

                # Open the current file in binary read mode
                with open(os.path.join(root, file), "rb") as f:
                    md5_hash = hashlib.md5()  # Initialize an MD5 hash object
                    # Read the file in chunks and update the MD5 hash
                    while chunk := f.read(4096):
                        md5_hash.update(chunk)
                    
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current timestamp
                    file_size = os.path.getsize(os.path.join(root, file))  # Get the size of the current file
                    # Print metadata about the file
                    print("Timestamp:", timestamp)
                    print("File Name:", file)
                    print("File Size (bytes):", file_size)
                    print("Complete File Path:", os.path.join(root, file))
                    print("MD5 Hash:", md5_hash.hexdigest())  # Print the MD5 hash of the file

    # Print search summary
    print("\nSearch Summary:")
    print("Files searched:", files_searched)  # Print the total number of files searched
    print("Hits found:", hits_found)  # Print the total number of hits found

if __name__ == "__main__":  # Check if the script is being run directly
    search_files()  # Call the search_files function to start the file search process
