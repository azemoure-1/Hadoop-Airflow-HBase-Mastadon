#!/usr/bin/env python3

import sys
import json

# Read input from standard input
#for line in sys.stdin:
#    try:
#        user_data = json.loads(line.strip())  # Parse JSON data
#        user_id = user_data.get('account', {}).get('username', 'N/A')
#        follower_count = user_data.get('account', {}).get('followers_count', 0)
#        print(f"{user_id}\t{follower_count}")
#    except json.JSONDecodeError:
        # Handle invalid JSON data, if necessary
#        pass



import sys
import json

for line in sys.stdin:
    try:
        data = json.loads(line.strip())
        user_id = data["account"]["id"]
        following_count = data["account"]["following_count"]
        print(f"{user_id}\t{following_count}")
    except Exception as e:
        print(f"Error processing data: {str(e)}")

