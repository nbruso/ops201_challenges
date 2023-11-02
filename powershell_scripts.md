# Ops Challenge 09
# Purpose: to practice scripting in powershell

# Output all events from the System event log that occurred in the last 24 hours to a file on your desktop named last_24.txt.

``Get-WinEvent -FilterHashtable @{LogName = "System"; StartTime = (Get-Date).AddHours(-24)} | Tee-Object -FilePath "$env:USERPROFILE\Desktop\last_24.txt" | Write-Host``

## This will display the events on the screen and also save them to the "last_24.txt" file on your desktop
###  Get-WinEvent retrieves the desired events from the System event log for the last 24 hours.
### Tee-Object is used to send the output to both the console (via Write-Host) and a file specified by the -FilePath parameter.
### -FilePath "$env:USERPROFILE\Desktop\last_24.txt" specifies the file path where the output will be saved.

# Output all “error” type events from the System event log to a file on your desktop named errors.txt.

``Get-WinEvent -LogName System -MaxEvents 0 | Where-Object { $_.LevelDisplayName -eq "Error" } | Format-List | Out-File -FilePath "$env:USERPROFILE\Desktop\errors.txt"``

## This command retrieves all error-type events from the "System" event log, formats them as a list, and saves the output to a file named "errors.txt" on the desktop.

### Get-WinEvent: This cmdlet retrieves events from the specified event log.

### LogName System: This parameter specifies the event log you want to query, in this case, the "System" event log, which contains system-related events.

### MaxEvents 0: This parameter sets the maximum number of events to retrieve. Setting it to 0 means you want to retrieve all events without a limit.

### |: This pipe symbol is used to pass the output of the previous cmdlet (Get-WinEvent) to the next cmdlet.

### Where-Object { $_.LevelDisplayName -eq "Error" }: This cmdlet filters the events received from Get-WinEvent. It selects only the events where the LevelDisplayName property is equal to "Error."

### Format-List: This cmdlet is used to format the filtered events as a list. It displays event information in a list format.

### Out-File -FilePath "$env:USERPROFILE\Desktop\errors.txt": This part of the command saves the output to a text file named "errors.txt" on the user's desktop.

### Out-File is used to write the output to a file.

### -FilePath "$env:USERPROFILE\Desktop\errors.txt" specifies the file path for the output file, which is located on the user's desktop.

# Print to the screen all events with ID of 16 from the System event log.

``Get-WinEvent -LogName System -MaxEvents 0 | Where-Object { $_.Id -eq 16 } | Format-Table -AutoSize``

## This command retrieves and displays events from the "System" event log that have an ID of 16, formatting them in a table with auto-sized columns for better readability on the screen.

### Get-WinEvent: This cmdlet retrieves events from the specified event log.

### -LogName System: This parameter specifies the event log you want to query, in this case, the "System" event log, which contains system-related events.

### -MaxEvents 0: This parameter sets the maximum number of events to retrieve. Setting it to 0 means you want to retrieve all events without a limit.

### |: This pipe symbol is used to pass the output of the previous cmdlet (Get-WinEvent) to the next cmdlet.

### Where-Object { $_.Id -eq 16 }: This cmdlet filters the events received from Get-WinEvent. It selects only the events where the Id property is equal to 16. This filters the events by their event ID, so it will only include events with an ID of 16.

### Format-Table -AutoSize: This cmdlet is used to format the filtered events as a table for display in the console. The -AutoSize parameter adjusts the column widths to fit the data, making it easier to read.

# Print to the screen the most recent 20 entries from the System event log.

``Get-WinEvent -LogName System -MaxEvents 20 | Format-Table -AutoSize``

## This command retrieves and displays the most recent 20 events from the "System" event log, formatting them in a table with auto-sized columns for better readability on the screen.

### Get-WinEvent: This cmdlet retrieves events from the specified event log.

### -LogName System: This parameter specifies the event log you want to query, in this case, the "System" event log, which contains system-related events.

### -MaxEvents 20: This parameter sets the maximum number of events to retrieve. It limits the query to the most recent 20 events in the "System" event log.

### |: This pipe symbol is used to pass the output of the previous cmdlet (Get-WinEvent) to the next cmdlet.

### Format-Table -AutoSize: This cmdlet is used to format the retrieved events as a table for display in the console. The -AutoSize parameter adjusts the column widths to fit the data, making it easier to read.


# Print to the screen all sources of the 500 most recent entries in the System event log.

``GGet-WinEvent -LogName System -MaxEvents 500 | Format-Table -Property TimeCreated, Id, ProviderName, Message -AutoSize``

## This command retrieves and displays the most recent 500 events from the "System" event log, formatting them in a table with auto-sized columns for better readability on the screen.

### Get-WinEvent: This cmdlet retrieves events from the specified event log.

### -LogName System: This parameter specifies the event log you want to query, in this case, the "System" event log, which contains system-related events.

### -MaxEvents 500: This parameter sets the maximum number of events to retrieve. It limits the query to the most recent 500 events in the "System" event log.

### |: This pipe symbol is used to pass the output of the previous cmdlet (Get-WinEvent) to the next cmdlet.

### Format-Table -AutoSize: This cmdlet is used to format the retrieved events as a table for display in the console. The -AutoSize parameter adjusts the column widths to fit the data, making it easier to read.

### source: 
