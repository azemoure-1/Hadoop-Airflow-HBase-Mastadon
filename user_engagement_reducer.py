#!/usr/bin/env python3
import sys

# Process input from standard input
for line in sys.stdin:
    try:
        user_id, engagement_rate = line.strip().split('\t')
        engagement_rate = float(engagement_rate)

        # Emit the user_id and engagement_rate
        print(f"{user_id}\t{engagement_rate}")

    except ValueError:
        # Handle invalid input, if necessary
        pass