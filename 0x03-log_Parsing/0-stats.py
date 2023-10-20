#!/usr/bin/python3
"""log parsing task
"""
import sys
from collections import defaultdict


total_file_size = 0
status_code_count = defaultdict(int)
line_count = 0


try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) == 7:
            ip_address, _, _, _, status_code,
            file_size = parts[0], parts[5], parts[6]

            if status_code.isdigit():
                status_code = int(status_code)
                file_size = int(file_size)
                total_file_size += file_size
                status_code_count[status_code] += 1
                line_count += 1

            if line_count % 10 == 0:
                print(f"Total file size: {total_file_size}")
                for code in sorted(status_code_count.keys()):
                    print(f"{code}: {status_code_count[code]}")

except KeyboardInterrupt:
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        print(f"{code}: {status_code_count[code]}")
