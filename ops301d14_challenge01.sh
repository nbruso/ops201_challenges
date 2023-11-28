#!/bin/bash

# Script Name:                  301 Challenge 01         
# Author:                       Dominique Bruso
# Date of latest revision:      11/28/2023
# Purpose:                      apply today's date to a log file
# Execution:                    ./ops201d14_challenge01.sh


#!/bin/bash

# Declaration of functions

# Timestamp function to generate current date and time
timestamp() {
  date +"%Y%m%d_%H%M%S"
}

# Echo a message with a timestamp
log() {
  echo "$(timestamp) - $1"
}

# Log the start of the script
log "Starting script"

# Copy /var/log/syslog to the current working directory
log "Copying /var/log/syslog to the current working directory"
cp /var/log/syslog ./syslog_copy.txt

# Append the current date and time to the filename using >>
log "Appending current date and time to the filename"
echo "$(timestamp)" >> syslog_copy.txt

# Log the end of the script
log "Script completed."




