# Script Name:                  Ops Challenge 09          
# Author:                       Dominique Bruso
# Date of latest revision:      12/07/2023
# Purpose:                      To practice python
# Execution:                    python3 09lab
# Source:                       https://github.com/codefellows/seattle-ops-301d14/tree/main/class-09/challenges; https://chat.openai.com/share/65571ec8-0f3a-46f8-afcf-ecb39b4de3db

# define variables

# get user input for temperature and time of day
temperature_str = input("Enter the temperature: ")
time_of_day = input("Enter the time of day (morning/afternoon/evening): ")

# convert the input to an integer
temperature = int(temperature_str)

# if statement with 'and' between conditions
if temperature > 80 and time_of_day == "afternoon":
    print("It's hot in the afternoon!")
elif temperature < 50 and time_of_day == "morning":
    print("It's cold in the morning!")
else:
    print("Moderate temperature")

# get user input for temperature
temperature_str = input("Enter the temperature: ")

# convert the input to an integer
temperature = int(temperature_str)

# if statement with 'or' between conditions
if temperature < 50 or temperature > 80:
    print("Extreme temperature!")
else:
    print("Moderate temperature")

# get user input for temperature
temperature_str = input("Enter the temperature: ")

# convert the input to an integer
temperature = int(temperature_str)

# nested if statement
if temperature < 50:
    print("Cold")
    if temperature < 30:
        print("Very cold!")
elif temperature > 80:
    print("Hot")
    if temperature > 90:
        print("Very hot!")
else:
    print("Moderate temperature")

# get user input for temperature
temperature_str = input("Enter the temperature: ")

# convert the input to an integer
temperature = int(temperature_str)

# if statement with 'pass' to avoid errors
if temperature > 80:
    print("Hot")
elif temperature < 50:
    pass  # do nothing if it's too cold
else:
    print("What's the weather like today?")







