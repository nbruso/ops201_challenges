# Script Name:                  Ops Challenge 13  
# Author:                       Dominique Bruso
# Date of latest revision:      12/13/2023
# Purpose:                      To practice powershell
# Execution:                    paste into powershell
# Source:                       https://github.com/codefellows/seattle-ops-301d14/tree/main/class-13/challenges; https://chat.openai.com/share/cd1519ee-8411-4354-a902-3cc1726f5090


Import-Module ActiveDirectory

# Create the user in the specified OU
New-ADUser -Name "Franz Ferdinand" `
    -SamAccountName "f.ferdinand" `
    -UserPrincipalName "ferdi@GlobeXpower.com" `
    -GivenName "Franz" `
    -Surname "Ferdinand" `
    -DisplayName "Franz Ferdinand" `
    -Department "TPS Department" `
    -Path "OU=Domain Controllers,DC=corp,DC=globexpower,DC=com" `
    -AccountPassword (ConvertTo-SecureString -AsPlainText "P@ssw0rd" -Force) `
    -Enabled $true



