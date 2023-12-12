# Script Name:                  Ops Challenge 11         
# Author:                       Dominique Bruso
# Date of latest revision:      12/11/2023
# Purpose:                      To practice python
# Execution:                    python3 day11.py
# Source:                       https://chat.openai.com/share/b60a1db7-e16a-4090-9d7f-d93ec0bb74c2

import psutil

def get_cpu_times():
    print("Fetching CPU times...")
    return psutil.cpu_times()

def print_cpu_info(cpu_times):
    print("Printing CPU info...")
    print(f"Time spent by normal processes executing in user mode: {cpu_times.user}")
    print(f"Time spent by processes executing in kernel mode: {cpu_times.system}")
    print(f"Time when the system was idle: {cpu_times.idle}")
    print(f"Time spent by priority processes executing in user mode: {cpu_times.nice}")
    print(f"Time spent waiting for I/O to complete: {cpu_times.iowait}")
    print(f"Time spent for servicing hardware interrupts: {cpu_times.irq}")
    print(f"Time spent for servicing software interrupts: {cpu_times.softirq}")
    print(f"Time spent by other operating systems running in a virtualized environment: {cpu_times.guest}")
    print(f"Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel: {cpu_times.guest_nice}")

def main():
    cpu_times = get_cpu_times()
    print_cpu_info(cpu_times)

if __name__ == "__main__":
    main()
