# Script Name:                  Ops Challenge 12     
# Author:                       Dominique Bruso
# Date of latest revision:      12/12/2023
# Purpose:                      To practice python
# Execution:                    python3 day12.py
# Source:                       https://chat.openai.com/share/45aa219e-77fc-4fd4-8f13-8c3b01bca5a5; https://github.com/codefellows/seattle-ops-301d14/blob/main/class-12/challenges/DEMO.md

#!/usr/bin/env python3

import requests

# Prompt the user to type a string input as the variable for your destination URL
url = input("Enter the destination URL: ")

# Check if the URL starts with 'http://' or 'https://', and add it if missing
if not url.startswith(('http://', 'https://')):
    url = 'http://' + url

# Prompt the user to select an HTTP Method
http_method = input("Select an HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

# Validate the user input for HTTP Method
allowed_methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
if http_method not in allowed_methods:
    print("Invalid HTTP Method. Please choose from:", ", ".join(allowed_methods))
    exit()

# Print the entire request about to be sent and ask for confirmation
print(f"\nRequest about to be sent:\nURL: {url}\nHTTP Method: {http_method}")
confirmation = input("Do you want to proceed? (yes/no): ").lower()

if confirmation != "yes":
    print("Request aborted.")
    exit()

# Perform the request using the requests library
response = requests.request(http_method, url)

# Print response header information
print("\nResponse Header Information:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

# Translate status code into plain terms
status_mapping = {
    200: "OK",
    201: "Created",
    204: "No Content",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error",
}

status_code = response.status_code
print(f"\nTranslated Status: {status_mapping.get(status_code, 'Unknown')}")
