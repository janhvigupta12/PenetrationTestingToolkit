#!/usr/bin/env python3
"""
Penetration Testing Toolkit - Main Launcher

This is a modular penetration testing toolkit with multiple modules,
including a Port Scanner and Brute-Forcer.

Usage:
    Run this script, and select a tool from the menu.

Modules:
    1. Port Scanner: Scan target IP/hostname ports for open ports.
    2. Brute-Forcer: Brute force login credentials for SSH or HTTP Basic Auth.

Requirements:
    - Python 3.6+
    - For SSH Brute-forcing: 'paramiko' package (pip install paramiko)
    - For HTTP Brute-forcing: 'requests' package (pip install requests)

Author: BLACKBOXAI
"""

import sys
import time

from pen_toolkit.port_scanner import port_scanner
from pen_toolkit.brute_forcer import brute_forcer


def main_menu():
    print("""
Penetration Testing Toolkit
===========================

Select a tool to run:

1. Port Scanner
2. Brute-Forcer
3. Exit
""")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice (1-3): ").strip()
        if choice == '1':
            port_scanner()
        elif choice == '2':
            brute_forcer()
        elif choice == '3':
            print("Exiting toolkit. Stay ethical!")
            sys.exit(0)
        else:
            print("Invalid choice, please try again.")
        time.sleep(1)


if __name__ == "__main__":
    main()

