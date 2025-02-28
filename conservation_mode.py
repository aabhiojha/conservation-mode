import os
import sys
import subprocess

file_path = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
# file_path = "text"

if os.geteuid() != 0:
    print("This script requires sudo prelivages.")
    subprocess.call(['sudo', sys.executable] + sys.argv)
    sys.exit()

with open(file_path, "r+") as f:
    f_content = f.read().strip()

    if(f_content == "1"):
        f.seek(0)
        f.write("0")
        print("Conservation mode is disabled")
        f.truncate() 
    else:
        f.seek(0)
        f.write("1")
        print("Conservation mode is enabled")
        f.truncate() 
