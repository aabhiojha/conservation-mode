#!/usr/bin/python3

import os
import sys
import subprocess
import argparse

file_path = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
# file_path = "text"

if os.geteuid() != 0:
    print("This script requires sudo prelivages.")
    subprocess.call(['sudo', sys.executable] + sys.argv)
    sys.exit()

parser = argparse.ArgumentParser(
    description="This tool toggles conservation mode in lenovo laptop"
)

# conservation get
# conservation -m enable
# conservation -m disable

parser.add_argument(
    "command",
    choices=["get"],
    help="Use 'get to chekc current status",
    nargs="?",
)

parser.add_argument(
    "-m", "--mode",
    choices=["enable", "disable"],
    help="Set enable or disable conservation mode"
)

args = parser.parse_args()

def get_status():
    try:
        with open(file_path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ("Error: Conservation mode file was not found")
        sys.exit(1)

def set_status(value):
    try:
        mode = '1' if value == 'enable' else '0'
        with open(file_path, "w") as f:
            f.write(mode)
        print(f"Conservation mode {'enabled' if value == 'enable' else 'disabled'}.")
    except PermissionError:
        print("Error: Insufficient permissions. Please run with sudo.")
        sys.exit(1)

if args.command == "get":
    status = get_status()
    print(f"Conservation mode is {'enabled' if status == '1' else 'disabled'}.")
elif args.mode:
    set_status(args.mode)