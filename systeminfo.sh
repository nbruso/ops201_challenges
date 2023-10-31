#!/bin/bash

# Script Name:                  Loop test
# Author:                       Dominique Bruso
# Date of latest revision:      10/31/2023
# Purpose:                      To practice displaying system ingo
# Execution:                    sudo ./systeminfo.sh
# Declaration of variables

#source: (OpenAI. (2023). ChatGPT (September 25 Version)

# Check if the script is run as root
if [ "$(id -u)" -ne 0 ]; then
  echo "This script must be run as root (use sudo)."
  exit 1
fi

# Function to display component information
display_component_info() {
  echo "==== $1 ===="
  lshw -c $2 | grep -E 'description|product|vendor|physical id|bus info|width|clock|capabilities|configuration|resources' | sed 's/^[[:space:]]*//'
  echo
}

# Display information for each component
display_component_info "Computer Name" system
display_component_info "CPU" cpu
display_component_info "RAM" memory
display_component_info "Display Adapter" display
display_component_info "Network Adapter" network