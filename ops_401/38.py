# OPS401D10  Ops Challenge 38
# 02/28/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source:https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-38/challenges/DEMO.md


#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Date:        02/28/2024
# Modified by: Dominique Bruso

# Import libraries
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### This function retrieves all HTML forms present on a given URL ###
### It is crucial for the script as it helps identify potential injection points ###
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")  # Parse the HTML content of the webpage using BeautifulSoup
    return soup.find_all("form")  # Find all form tags in the HTML content and return them

### This function extracts details about a form ###
### It helps in understanding the structure of the form and its fields ###
def get_form_details(form):
    details = {}  # Initialize an empty dictionary to store form details
    action = form.attrs.get("action").lower()  # Get the 'action' attribute of the form and convert it to lowercase
    method = form.attrs.get("method", "get").lower()  # Get the 'method' attribute of the form, default to 'get', and convert it to lowercase
    inputs = []  # Initialize an empty list to store input details
    for input_tag in form.find_all("input"):  # Iterate over all input tags within the form
        input_type = input_tag.attrs.get("type", "text")  # Get the 'type' attribute of the input tag, default to 'text'
        input_name = input_tag.attrs.get("name")  # Get the 'name' attribute of the input tag
        inputs.append({"type": input_type, "name": input_name})  # Append input details to the inputs list
    details["action"] = action  # Store the form action in the details dictionary
    details["method"] = method  # Store the form method in the details dictionary
    details["inputs"] = inputs  # Store the input details in the details dictionary
    return details  # Return the details dictionary

### This function submits a form with potential injection values ###
### It is essential for testing whether the forms are vulnerable to XSS ###
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])  # Construct the complete URL to submit the form
    inputs = form_details["inputs"]  # Retrieve input details from form details
    data = {}  # Initialize an empty dictionary to store form data
    for input in inputs:  # Iterate over all input details
        if input["type"] == "text" or input["type"] == "search":  # Check if input type is text or search
            input["value"] = value  # Assign the provided value to the input
        input_name = input.get("name")  # Get the input name
        input_value = input.get("value")  # Get the input value
        if input_name and input_value:  # Check if both input name and value exist
            data[input_name] = input_value  # Add input name and value to the data dictionary

    if form_details["method"] == "post":  # Check if the form method is POST
        return requests.post(target_url, data=data)  # Send a POST request with form data
    else:  # If the form method is not POST (i.e., it is GET)
        return requests.get(target_url, params=data)  # Send a GET request with form data as query parameters

### This function scans a given URL for XSS vulnerabilities ###
### It tests each form on the page with a payload that triggers an alert ###
def scan_xss(url):
    forms = get_all_forms(url)  # Get all forms present on the given URL
    print(f"[+] Detected {len(forms)} forms on {url}.")  # Print the number of forms detected on the URL
    # XSS payload triggering an alert
    js_script = "<script>alert('XSS Vulnerability Detected');</script>"  # Define a JavaScript payload to trigger an alert
    is_vulnerable = False  # Initialize a flag to track if XSS vulnerability is detected
    for form in forms:  # Iterate over each form
        form_details = get_form_details(form)  # Get details of the current form
        content = submit_form(form_details, url, js_script).content.decode()  # Submit the form with the XSS payload and get the response content
        if js_script in content:  # Check if the XSS payload is present in the response content
            print(f"[+] XSS Detected on {url}")  # Print a message indicating XSS vulnerability detection
            print(f"[*] Form details:")  # Print the details of the vulnerable form
            pprint(form_details)  # Pretty print the form details
            is_vulnerable = True  # Set the flag to indicate XSS vulnerability detection
    return is_vulnerable  # Return whether XSS vulnerability is detected

# Main

### The main function prompts the user for a URL and scans it for XSS vulnerabilities ###
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:")  # Prompt the user to enter a URL
    print(scan_xss(url))  # Call the scan_xss function and print the result

### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target and one XSS-negative target
### TODO: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection

# Positive Detection Output (XSS Vulnerability Detected):
"""
Enter a URL to test for XSS: https://xss-game.appspot.com/level1/frame
[+] Detected 1 forms on https://xss-game.appspot.com/level1/frame.
[+] XSS Detected on https://xss-game.appspot.com/level1/frame
[*] Form details:
{'action': '', 'inputs': [{'name': 'query', 'type': 'text'}], 'method': 'get'}
True
"""

# Negative Detection Output (No XSS Vulnerability Detected):
"""
Enter a URL to test for XSS: http://dvwa.local/login.php
[+] Detected 2 forms on http://dvwa.local/login.php.
False
"""
