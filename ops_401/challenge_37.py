# OPS401D10  Ops Challenge 37
# 02/27/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source:https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-37/challenges/DEMO.md; https://www.dev2qa.com/how-to-get-set-http-headers-cookies-and-manage-sessions-use-python-requests-module/; https://www.asciiart.eu/television/sesame-street; https://chat.openai.com/share/32d15d5a-b4d2-4c2c-8a71-7c11e7bff7de

#!/usr/bin/env python3

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

import requests
import webbrowser

# Define target site
targetsite = "http://www.whatarecookies.com/cookietest.asp"

# Send the cookie back to the site and receive HTTP response
response = requests.get(targetsite)
cookie = response.cookies

# Generate a .html file to capture the contents of the HTTP response
html_content = response.content
with open("response.html", "wb") as file:
    file.write(html_content)

# Open the HTML file with Firefox
webbrowser.open("response.html")

# Stretch Goal: Give Cookie Monster hands
def give_cookie_monster_hands():
    print('''
               .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
      .'`-._'    " .     " _.-'`. :       o  :
  .'    "     '         "     "   ; `.;";";";'
 ;         '       "       '     . ; .' ; ; ;
;     '         '       '   "    .'      .-'
'  "     "   '      "           "    _.-'  
''')

give_cookie_monster_hands()
