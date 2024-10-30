#!/usr/bin/python3
import sys
import signal

def print_status_codes(status_code_count, total_size):
    """
    Prints the total file size and counts of each status code.

    Args:
        status_code_count: Dictionary of HTTP status codes and their counts.
        total_size: Total size of all files processed.
    """
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status_code_count.items()):
        if count != 0:
            print("{}: {}".format(status_code, count))

def signal_handler(sig, frame):
    """
    Handles the signal interruption to print the results.
    """
    print_status_codes(status_code_count, total_file_size)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

total_file_size = 0
line_count = 0
status_code_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue

        try:
            file_size = int(parts[-1])
            status_code = parts[-2]

            total_file_size += file_size
            if status_code in status_code_count:
                status_code_count[status_code] += 1

        except (ValueError, IndexError):
            continue

        line_count += 1
        if line_count == 10:
            print_status_codes(status_code_count, total_file_size)
            line_count = 0

finally:
    print_status_codes(status_code_count, total_file_size)
