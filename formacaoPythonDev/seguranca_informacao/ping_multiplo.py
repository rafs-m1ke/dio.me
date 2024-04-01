import os
import time


with open("hosts.txt", "r") as file:
    
    for ip in file:
        print("-" * 60)
        os.system(f"ping -c 2 {ip}")
        print("-" * 60)
        time.sleep(5)