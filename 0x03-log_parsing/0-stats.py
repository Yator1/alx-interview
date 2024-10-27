#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regular expression to match the specific format
log_pattern = re.compile(
    r'(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
)

def print_statistics():
    """Print the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def process_line(line):
    """Process a single log line if it matches the expected format."""
    global total_file_size, line_count
    
    match = log_pattern.match(line)
    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))

        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_statistics()

def signal_handler(sig, frame):
    """Handle keyboard interruption (Ctrl + C) to print statistics."""
    print_statistics()
    sys.exit(0)

# Attach the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read lines from stdin
for line in sys.stdin:
    process_line(line)

# Print statistics at the end if any lines were processed
if line_count % 10 != 0:
    print_statistics()
