#!/usr/bin/python3

import sys

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

total_file_size = 0
status_code = 0
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
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            line_count += 1
            total_file_size += int(parsed_line[0])  # file size
            status_code = parsed_line[1]  # status code

            if status_code in status_code_count:
                status_code_count[status_code] += 1

            if line_count == 10:
                print_status_codes(status_code_count, total_file_size)
                line_count = 0

finally:
    print_status_codes(status_code_count, total_file_size)
