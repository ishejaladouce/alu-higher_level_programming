#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
- Total file size
- Number of lines per HTTP status code

Prints stats every 10 lines and on keyboard interrupt.
"""

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_counts = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

def print_stats():
    """Print the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        count = status_counts[code]
        if count > 0:
            print(f"{code}: {count}")

try:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        # Expecting format:
        # <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status> <size>
        # So status is second last, size is last element
        try:
            status = int(parts[-2])
            size = int(parts[-1])
        except (IndexError, ValueError):
            # Malformed line, ignore
            continue

        if status in status_counts:
            status_counts[status] += 1
        total_size += size

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
