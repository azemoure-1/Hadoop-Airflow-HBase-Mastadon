#!/usr/bin/env python3
import sys
import json

# Initialize variables to store user engagement counts
#user_engagement = {}

# Process input from standard input
#for line in sys.stdin:
#    try:
#        user_data = json.loads(line.strip())  # Parse JSON data
#        user_id = user_data.get('account', {}).get('username', 'N/A')

        # Extract engagement metrics
#        reblogs_count = user_data.get('reblogs_count', 0)
#        replies_count = user_data.get('replies_count', 0)
#        favourites_count = user_data.get('favourites_count', 0)

        # Calculate engagement rate
#        total_engagement = reblogs_count + replies_count + favourites_count
#        engagement_rate = total_engagement / max(1, user_data.get('account', {}).get('statuses_count', 1))

        # Update user engagement in the dictionary
#        user_engagement[user_id] = engagement_rate

#    except json.JSONDecodeError:
        # Handle invalid JSON data, if necessary
#        pass

# Emit user_id and engagement rate as key-value pair
#for user_id, engagement_rate in user_engagement.items():
#    print(f"{user_id}\t{engagement_rate}")



import sys
import json

for line in sys.stdin:
    try:
        data = json.loads(line.strip())
        user_id = data["account"]["id"]
        reblogs_count = data["reblogs_count"]
        favorites_count = data["favourites_count"]
        engagement = (reblogs_count + favorites_count) / 2.0
        print(f"{user_id}\t{engagement:.4f}")
    except Exception as e:
        print(f"Error processing data: {str(e)}")

