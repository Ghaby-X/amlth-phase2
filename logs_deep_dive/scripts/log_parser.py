import re
import ipaddress
from datetime import datetime, timedelta

# function to get unique ips
def extract_ip(line: list[str]):
    if len(line) < 2: return False
    current_ip = line[1]
    try:
        ipaddress.ip_address(current_ip)
    except:
        return False
    
    return current_ip


if __name__ == "__main__":
    unique_ip_count = {}
    filename = "sample.log"

    with open(filename) as f:
        for line in f:
            cur_log = line.strip()
            line_array = line.split()

            cur_ip = extract_ip(line_array)

            if cur_ip:
                if cur_ip in unique_ip_count:
                    unique_ip_count[cur_ip] += 1
                else:
                    unique_ip_count[cur_ip] = 1
    
    print("======== Unique IP addresses and their counts =========")
    for k, v in unique_ip_count.items():
        print("IP address: ", k)
        print("Count: ", v)
        print("\n")
