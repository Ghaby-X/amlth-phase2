# Logs Deep Dive

A collection of Python scripts for analyzing web server logs and extracting useful information.

## Overview

This project provides tools to analyze web server logs for various metrics including:
- IP address activity tracking
- Time-based analysis
- Endpoint access counting
- User agent identification

### Requirements

- python3.12


## Scripts

Sample results can be viewed in the results directory

### ten_second_window.py

Analyzes logs to identify IP addresses that make multiple requests within a 10-second window. This can be useful for detecting potential DoS attacks or aggressive crawlers.

```bash
python3.12 scripts/ten_second_window.py
```

Key features:
- Sorts logs chronologically
- Extracts timestamps and IP addresses
- Counts requests from each IP within configurable time windows
- Outputs IP addresses with their request counts

### log_parser.py

Parses log files to count unique IP addresses and their request frequencies.

```bash
python3.12 scripts/log_parser.py
```

Key features:
- Extracts and validates IP addresses
- Counts total requests per IP address

### endpoint_access_count.py

Analyzes which endpoints are being accessed and how frequently.

```bash
python3.12 scripts/endpoint_access_count.py
```

Key features:
- Extracts HTTP endpoints from logs
- Counts access frequency per endpoint

### request_from_agent_type.py

Identifies and counts requests by user agent type.

```bash
python3.12 scripts/request_from_agent_type.py
```

Key features:
- Extracts user agent strings
- Groups and counts requests by browser/agent type

## Log Format

The scripts are designed to work with logs in the following format:
```
TIMESTAMP IP - - [DATE:TIME +TIMEZONE] "METHOD ENDPOINT HTTP/VERSION" STATUS - "REFERRER" "USER_AGENT"
```

Example:
```
2025-06-03T10:09:02.588Z 197.159.135.110 - - [03/Jun/2025:10:09:02 +0000] "GET /favicon.ico HTTP/1.1" 200 - "http://108.129.212.117:8080/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
```

## Usage

1. Clone the repository

```
git clone https://github.com/Ghaby-X/amlth-phase2.git
```

2. Place your log file in the project root directory as `sample.log`
3. Run the scripts from the project root directory:

```bash
# Navigate to the project root directory first
cd /amlth-phase2/logs_deep_dive

# Then run the scripts
python3.12 scripts/ten_second_window.py
python3.12 scripts/log_parser.py
python3.12 scripts/endpoint_access_count.py
python3.12 scripts/request_from_agent_type.py
```

Note: The scripts expect the log file to be in the same directory from which you run the script. If you run the scripts from another directory, you'll need to provide the full path to the log file or modify the scripts to use the correct path.
