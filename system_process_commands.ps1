# Script Name:                  Ops Challenge 10- System Process Commands
# Author:                       Dominique Bruso
# Date of latest revision:      11/03/2023
# Purpose:                      To practice making powershell scripts


# Print Active Processes by CPU Time Consumption:
Get-Process | Sort-Object -Property CPU -Descending | Format-Table -AutoSize

# Get-Process: Retrieves a list of currently running processes.
# Sort-Object -Property CPU -Descending: Sorts the list of processes based on CPU usage in descending order (highest CPU usage at the top).
# Format-Table -AutoSize: Formats and displays the sorted list in a table format.
# Print Active Processes by Process Identification Number (PID):

Get-Process | Sort-Object -Property Id | Format-Table -AutoSize

# Get-Process: Retrieves a list of currently running processes.
# Sort-Object -Property Id: Sorts the list of processes based on their Process Identification Number (PID) in ascending order.
# Format-Table -AutoSize: Formats and displays the sorted list in a table format

# Print Top Five Processes by Working Set (WS(K)):
Get-Process | Sort-Object -Property WorkingSet -Descending | Select-Object -First 5 | Format-Table -AutoSize

# Get-Process: Retrieves a list of currently running processes.
# Sort-Object -Property WorkingSet -Descending: Sorts the list of processes based on their Working Set (memory usage) in descending order.
# Select-Object -First 5: Selects the first five processes from the sorted list.
# Format-Table -AutoSize: Formats and displays the selected list in a table format.

# Start a Browser Process and Open a Website (e.g., OWASP):
Start-Process -FilePath "chrome.exe" -ArgumentList "https://owasp.org/www-project-top-ten/"

# Start-Process: Initiates a new process (in this case, a web browser process).
# -FilePath "chrome.exe": Specifies the path to the browser executable (replace with your preferred browser's executable path).
# -ArgumentList "https://owasp.org/www-project-top-ten/": Passes the URL of the website (in this case, OWASP's Top Ten) as an argument to the browser process.
# Replace "chrome.exe" with the path to your preferred browser executable.

# Start Notepad Ten Times Using a For Loop:
1..10 | ForEach-Object { Start-Process -FilePath "notepad.exe" }

# 1..10: Creates a range of numbers from 1 to 10.
# ForEach-Object { Start-Process -FilePath "notepad.exe" }: For each number in the range, it starts the Notepad application. This effectively starts Notepad ten times.

# Close All Instances of Notepad:
Get-Process | Where-Object { $_.ProcessName -eq "notepad" } | ForEach-Object { Stop-Process -Id $_.Id }

# Get-Process: Retrieves a list of currently running processes.
# Where-Object { $_.ProcessName -eq "notepad" }: Filters the list to select only processes with the name "notepad."
# ForEach-Object { Stop-Process -Id $_.Id }: For each filtered Notepad process, it forcefully stops (closes) the process based on its Process Identification Number (PID).

# Kill a Process by PID (e.g., Google Chrome or MS Edge):
Stop-Process -Id (Get-Process -Name "chrome" -or "msedge").Id

# Stop-Process -Id (Get-Process -Name "chrome" -or "msedge").Id: Identifies and forcibly terminates (kills) a specified process (e.g., "chrome" or "msedge") by its name. Use with caution, especially for web browsers, as it will forcefully close all instances of the specified process.
