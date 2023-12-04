#!/bin/bash

# Script Name:                  Ops Challenge 05: Log Clearing           
# Author:                       Dominique Bruso
# Date of latest revision:      12/01/2023
# Purpose:                      To practice log clearing
# Execution:                    sudo bash 05_logclearing.sh or sudo ./05_logclearing.sh
# Sources:                      https://chat.openai.com/share/a4ee55d6-fd5a-4b28-b40d-3ae817bea40e; https://github.com/codefellows/seattle-ops-301d14/blob/main/class-05/challenges/DEMO.md

#!/bin/bash

# Declaration of variables
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
backup_directory="/var/log/backups"

# Create the backup directory if it doesn't exist
mkdir -p "$backup_directory"

# Clear the screen
clear

# Print to the screen the file size of the log files before compression
echo "This is the file size of my log files before compression"
syslog_file_size=$(stat -c %s /var/log/syslog)
wtmp_file_size=$(stat -c %s /var/log/wtmp)
echo "Syslog file size before compression: $syslog_file_size"
echo "Wtmp file size before compression: $wtmp_file_size"

# Pause for user to read information
read -n 1 -s -r -p "Press any key to continue..."

# Clear the screen
clear

# Compress the contents of the log files to a backup directory
echo "Compressing files"
gzip -c /var/log/syslog > "$backup_directory/syslog-$TIMESTAMP.gz"
gzip -c /var/log/wtmp > "$backup_directory/wtmp-$TIMESTAMP.gz"

# Clear the contents of the log files
echo -n > /var/log/syslog
echo -n > /var/log/wtmp

# Pause for user to read information
read -n 1 -s -r -p "Press any key to continue..."

# Clear the screen
clear

# Print to the screen the file size of the compressed files
syslog_compressed_size=$(stat -c %s "$backup_directory/syslog-$TIMESTAMP.gz")
wtmp_compressed_size=$(stat -c %s "$backup_directory/wtmp-$TIMESTAMP.gz")
echo "Syslog compressed file size: $syslog_compressed_size"
echo "Wtmp compressed file size: $wtmp_compressed_size"

# Pause for user to read information
read -n 1 -s -r -p "Press any key to continue..."

# Clear the screen
clear

# Compare the size of the compressed files to the size of the original log files
echo "File size before compression: Syslog=$syslog_file_size, Wtmp=$wtmp_file_size"
echo "File size after compression: Syslog=$syslog_compressed_size, Wtmp=$wtmp_compressed_size"

# Pause for user to read information
read -n 1 -s -r -p "Press any key to continue..."

# Clear the screen
clear

if [[ $syslog_file_size -gt $syslog_compressed_size || $wtmp_file_size -gt $wtmp_compressed_size ]]; then
    echo "Compression unsuccessful: compressed file size is larger than original file size"
else
    echo "Compression successful: compressed file size is smaller than or equal to original file size"
fi
