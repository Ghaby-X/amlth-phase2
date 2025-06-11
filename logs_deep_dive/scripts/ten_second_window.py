import ipaddress
from datetime import datetime, timedelta

# get sorted logs
def get_sorted_logs(logfile):
    with open(logfile) as f:
        lines = f.readlines()
        sorted_log = sorted(lines)

    return sorted_log

# extract date from ipaddress sample date 2025-06-03T10:09:04.088Z
def extract_date(line: list[str]):
    if len(line) < 1: return False
    current_date = line[0]
    try:
        dateobj = datetime.fromisoformat(current_date) # get current date
    except:
        return False
    return current_date

# function to get unique ips
def extract_ip(line: list[str]):
    if len(line) < 2: return False
    current_ip = line[1]
    try:
        ipaddress.ip_address(current_ip)
    except:
        return False
    
    return current_ip

# add ten seconds to date
def add_n_seconds(date: str, n:int) -> str:
    dateobj = datetime.fromisoformat(date)
    ten_seconds = timedelta(seconds=n)
    dateobj += ten_seconds
    return dateobj.isoformat()

# counts the number of ip within n window
def ip_count_n_window(logs: list[str], n: int = 10):
    ip_count = {}
    ip_timestamp ={}

    for log in logs:
        log_split = log.split()
        ip_address = extract_ip(log_split)
        timestamp = extract_date(log_split)

        if ip_address and timestamp:
            if ip_address not in ip_timestamp:
                ip_timestamp[ip_address] = timestamp
                ip_count[ip_address] = 1
            else:
                max_time_stamp = add_n_seconds(ip_timestamp[ip_address], n)
                if timestamp < max_time_stamp:
                    ip_count[ip_address] += 1
    
    return ip_count

if __name__ == "__main__":
    filename = "sample.log"
    ip_count_window_10 = {}
    
    sorted_log = get_sorted_logs(filename)
    count_dict = ip_count_n_window(sorted_log, 10) 

    # format and print count_dict
    print("======== IP addresses and their counts within 10 seconds =========")
    for ip, count in count_dict.items():
        print("IP address: ", ip)
        print("Count: ", count)
        print("\n")


    
