<<<<<<< HEAD
from log_parser import LogEntry


loger = "auth.log"

objects = []

try:
    with open(loger, "r"):
        for line in loger:
            x = LogEntry(loger)
            objects.append(x)
except FileNotFoundError:
    print("[!] The file must be in the same folder")

for obj in objects:
    print(f"[+] Object: {obj.get_all_attributes()}")
=======
import re
from log_parser import LogEntry



>>>>>>> main
