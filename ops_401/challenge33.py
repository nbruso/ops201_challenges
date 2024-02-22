# OPS401D10  Ops Challenge 33
# 02/21/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source: https://github.com/eduardxyz/virustotal-search/blob/master/virustotal-search.py; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-33/challenges/DEMO.md

#!/usr/bin/env python

# The below demo script works in tandem with virustotal-search.py from https://github.com/eduardxyz/virustotal-search, which must be in the same directory.
# Set your environment variable first to keep it out of your script here.

#!/usr/bin/env python
# The above line is called a "shebang" line. It tells the system what interpreter to use to execute the script. In this case, it's Python.

import os
import subprocess
# Importing the 'os' and 'subprocess' modules which are required for interacting with the operating system and executing external commands.

# Set your environment variable 'API_KEY_VIRUSTOTAL' to store your VirusTotal API key.
# You can hard-code your API key here temporarily for testing purposes.
API_key = '6d97e7c04f91f496835f801ec2a511c2d1fe0e3a5c0a8d990ef12932d0433191'

# Get the API key from the environment variable.
apikey = os.getenv('API_KEY_VIRUSTOTAL')
# Retrieve the API key from the environment variable 'API_KEY_VIRUSTOTAL'.

# Check if the API key is set. If not, print an error message and exit.
if not apikey:
    print("Error: API_KEY_VIRUSTOTAL environment variable is not set.")
    exit(1)
# Check if the API key is set. If it's not set, print an error message and exit the script with an exit code of 1.

# Set the MD5 hash of the target file you want to query.
hash_value = 'D41D8CD98F00B204E9800998ECF8427E'

# Concatenate the command to query VirusTotal using the provided script.
query_command = ['python3', 'virustotal-search.py', '-k', apikey, '-m', hash_value]
# Define the command to execute to query VirusTotal. It's constructed as a list of strings.

# Execute the command and capture the output.
output = subprocess.check_output(query_command, universal_newlines=True)
# Execute the command using the 'subprocess' module and capture the output as a string.

# Parse the output to extract the number of positives detected and the total files scanned.
# You need to customize this part based on the output format of the virustotal-search.py script.
# Here, we assume the output format is: "Positives: <number>, Total: <number>"
positives = 0
total_files = 0
for line in output.split('\n'):
    if line.startswith('Positives:'):
        positives = int(line.split(':')[1])
    elif line.startswith('Total:'):
        total_files = int(line.split(':')[1])
# Iterate through each line of the output and extract the number of positives detected and the total files scanned.

# Print the results to the screen.
print("Number of positives detected:", positives)
print("Total files scanned:", total_files)
# Print the number of positives detected and the total files scanned to the screen.

