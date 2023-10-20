#!/usr/bin/env python3
import sys

current_date = None
user_count = 0

for line in sys.stdin:
    try:
        date, count = line.strip().split('\t')

        if current_date == date:
            user_count += int(count)
        else:
            if current_date:
                # Output the date and user count
                print(f"{current_date}\t{user_count}")
            current_date = date
            user_count = int(count)

    except ValueError:
        # Ignore lines that don't have the expected format
        continue

Output the last date and user count
if current_date:
    print(f"{current_date}\t{user_count}")