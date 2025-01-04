#!/usr/bin/python3
"""states file"""


import sys
import re

if __name__ == "__main__":
    total_size = 0
    line_count = 0
    status_code_count = {}

    # Updated regular expression to match the generator's output
    log_pattern = re.compile(
        r'^(\d{1,3}\.){3}\d{1,3} - \[' +
        r'.*?\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
    )

    try:
        while True:
            line = sys.stdin.readline().strip()
            if not line:
                break

            match = log_pattern.match(line)
            if match:
                file_size = int(match.group(3))
                status_code = match.group(2)
                total_size += file_size
                line_count += 1


                if status_code in status_code_count:
                    status_code_count[status_code] += 1
                else:
                    status_code_count[status_code] = 1


                if line_count == 10:
                    print(f"File size: {total_size}")
                    for code, count in sorted(status_code_count.items()):
                        print(f"{code}: {count}")
                    line_count = 0
                    status_code_count.clear()

    except KeyboardInterrupt:
        # Print final results on CTRL+C
        print(f"\nFile size: {total_size}")
        for code, count in sorted(status_code_count.items()):
            print(f"{code}: {count}")
