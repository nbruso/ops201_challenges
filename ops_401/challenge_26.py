# OPS401D10  Ops Challenge 26
# 02/12/2024
# Dominique Bruso
# Purpose: practice python scripting 
# source: 

#!/usr/bin/env python3


# Import libraries
import logging
import os

# Create the log object
log = logging.getLogger("my_logger")

# Configure my logging object
logging.basicConfig()

log.info("Hello, World")
log.warning("THIS IS A WARNING")

#Define a function
def do_something():
log.debug("Doing something!")

#Call our function
do_something()
