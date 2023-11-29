#!/bin/bash

# Script Name:                  301 Challenge 01         
# Author:                       Dominique Bruso
# Date of latest revision:      11/28/2023
# Purpose:                      apply today's date to a log file
# Execution:                    ./ops301d14_challenge01.sh


# Get the current date and time
timestamp=$(date +"%Y%m%d_%H%M%S")

# Log message with timestamp
echo "$timestamp - Starting script..."

# Copy /var/log/syslog to the current working directory
echo "$timestamp - Copying /var/log/syslog to the current working directory..."
cp /var/log/syslog "./syslog_copy_$timestamp.txt"

# Log the end of the script
echo "$timestamp - Script completed."



# sources: https://google.github.io/styleguide/shellguide.html; https://github.com/codefellows/seattle-ops-301d14/tree/main/class-02/challenges; https://chat.openai.com/share/b9b81750-1303-46c2-8755-1c7a4d761d35


