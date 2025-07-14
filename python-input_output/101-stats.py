#!/usr/bin/python3
"""
Reads stdin line by line, computes and prints metrics:
- Total file size
- Number of lines by status code
Prints stats every 10 lines and on keyboard interruption.
"""

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_counts = {code: 0 for code in status_codes}
total_size = 0
line_count = 0


def print_stats():
    """Print the accumulated statistics."""
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
        if len(parts) < 2:
            # Malformed line; skip
            continue
        # Try to parse file size first (last element)
        try:
            size = int(parts[-1])
            total_size += size
        except ValueError:
            # Can't parse file size; skip adding size
            continue

        # Try to parse status code (second last element)
        try:
            status = int(parts[-2])
            if status in status_counts:
                status_counts[status] += 1
        except ValueError:
            # Malformed status code; just skip counting status
            pass

        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    pass
finally:
    print_stats()
