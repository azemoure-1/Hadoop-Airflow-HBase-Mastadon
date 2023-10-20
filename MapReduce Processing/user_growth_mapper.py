#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    try:
        user_data = json.loads(line.strip())  # Parse JSON data

        # Extract the user creation date
        created_at = user_data.get('account', {}).get('created_at', 'N/A')

        # Extract the year-month-day part of the creation date
        creation_date = created_at.split('T')[0]

        # Emit the creation date as the key and count as 1
        print(f"{creation_date}\t1")
    except json.JSONDecodeError:
        # Handle invalid JSON data, if necessary
        pass