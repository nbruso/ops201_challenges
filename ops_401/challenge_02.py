# OPS401D10  Ops Challenge 02
# 01/09/2024
# Dominique Bruso
# source: https://github.com/codefellows/seattle-cybersecurity-401d10/tree/main/class-02/challenges; https://chat.openai.com/share/1e59f557-425c-4ecb-8dd9-04610bff6295; https://github.com/codefellows/seattle-cybersecurity-401d10/tree/main/class-03/challenges; https://chat.openai.com/share/a6f03d94-ef92-4f20-89a2-e430556e0518


# Import necessary modules
import datetime  # Import the datetime module to work with timestamps
import os        # Import the os module for executing system commands
import time      # Import the time module for introducing pauses
import smtplib   # Import the smtplib module for sending emails
from email.mime.text import MIMEText  # Import MIMEText to create email messages
from getpass import getpass  # Import getpass for secure password input

# Email setup
# Prompt for the user's email address and password for sending notifications
email_address = input("Enter your email address: ")  # Get email address from user
email_password = getpass("Enter your email password: ")  # Securely get password from user
smtp_server = 'smtp.yourprovider.com'  # SMTP server address (replace with actual server)
smtp_port = your_smtp_port  # SMTP port number (replace with actual port)

# Function to send email
def send_email(subject, body):
    # Create a MIME text message
    msg = MIMEText(body)
    msg['Subject'] = subject  # Set email subject
    msg['From'] = email_address  # Set sender email address
    msg['To'] = email_address   # Set recipient email address

    # Send the email using SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Start TLS for security
        server.login(email_address, email_password)  # Login to the SMTP server
        server.send_message(msg)  # Send the email message

# Define the target IP address for monitoring
target_ip = "192.168.1.1"  # Target IP address (replace with actual IP)

# Variable to keep track of the previous status of the target
previous_status = None

# Main loop for continuous monitoring
while True:
    try:
        # Get the current timestamp
        timestamp = datetime.datetime.now()

        # Send ICMP packet to target IP using the ping command
        response = os.system("ping -c 1 " + target_ip)

        # Determine the current status of the target IP
        current_status = 'Active' if response == 0 else 'Inactive'

        # Check if there is a change in status compared to previous check
        if previous_status is not None and previous_status != current_status:
            # Compose and send an email notification about the status change
            subject = f"Host Status Change Detected"
            body = (f"Host {target_ip} status changed from {previous_status} to {current_status}"
                    f" at {timestamp}")
            send_email(subject, body)

        # Update the previous status for the next iteration
        previous_status = current_status

        # Print the current status, timestamp, and target IP
        print(f"{timestamp} Network {current_status} to {target_ip}")

    except Exception as e:
        # Catch and print any exceptions that occur
        print(f"Error: {e}")

    finally:
        # Finally block to ensure certain actions happen after each loop iteration
        # Print the start time of each loop iteration
        print("Start:", time.ctime())
        # Pause for two seconds before next iteration
        time.sleep(2)
