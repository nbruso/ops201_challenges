#!/bin/bash

# Script Name:                  Conditional script
# Author:                       Dominique Bruso
# Date of latest revision:      10/30/2023
# Purpose:                      To practice a conditional script
# Execution:                    bash conditionals.sh or ./conditonals.sh

#source: (OpenAI. (2023). ChatGPT (September 25 Version)

# Declaration of variables

# Array of paths to be checked
paths_to_check=("directory_to_create" "file_to_create.txt")

for path in "${paths_to_check[@]}"; do
    if [ ! -e "$path" ]; then
        if [ -d "$path" ]; then
            # Check if it's a directory and create it if it doesn't exist
            mkdir -p "$path"
            echo "Directory '$path' created."
        else
            # Create a file if it doesn't exist
            touch "$path"
            echo "File '$path' created."
        fi
    else
        echo "'$path' already exists."
    fi
done
