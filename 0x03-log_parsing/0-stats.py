#!/usr/bin/python3
import sys
import re

if __name__ == "__main__":
    total_size = 0
    line_count = 0
    status_code_frequency = {}

    # Updated regular expression to account for microseconds in the timestamp
    log_pattern = re.compile(
        r'^(\d{1,3}\.){3}\d{1,3} - \[' +
        r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}' +  # Date and time part
        r'(\.\d{6})?\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'  # Optional microseconds, status code, file size
    )

    try:
        while True:
            line = sys.stdin.readline().strip()
            if not line:  # If no more input, break the loop
                if line_count > 0:  # If there were any lines processed before EOF, print the result
                    print(f"File size: {total_size}")
                    for code in sorted(status_code_frequency.keys()):
                        print(f"{code}: {status_code_frequency[code]}")
                break  # End of file reached

            match = log_pattern.match(line)
            if match:
                # Extract file size and status code
                try:
                    file_size = int(match.group(4))  # Fixed index to match group for file size
                    status_code = match.group(3)  # Fixed index to match group for status code
                except ValueError:
                    # Skip invalid lines if status code or file size is invalid
                    continue

                total_size += file_size
                line_count += 1

                # Update the status code frequency
                if status_code in status_code_frequency:
                    status_code_frequency[status_code] += 1
                else:
                    status_code_frequency[status_code] = 1

                # Print metrics after every 10 lines
                if line_count == 10:
                    print(f"File size: {total_size}")
                    for code in sorted(status_code_frequency.keys()):
                        print(f"{code}: {status_code_frequency[code]}")
                    line_count = 0  # Reset the line count
                    status_code_frequency.clear()  # Clear the status code count

    except KeyboardInterrupt:
        # Handle keyboard interruption (Ctrl + C)
        print(f"\nFile size: {total_size}")
        for code in sorted(status_code_frequency.keys()):
            print(f"{code}: {status_code_frequency[code]}")

