#!/usr/bin/env python3

import sys

# Initialize variables to store the top users
top_users = []
max_users = 10  # Number of users with the most followers to keep track of

# Read input from standard input
for line in sys.stdin:
    user_id, follower_count = line.strip().split('\t')
    follower_count = int(follower_count)

    # Maintain a list of the top users with the most followers
    if len(top_users) < max_users:
        top_users.append((user_id, follower_count))
        top_users.sort(key=lambda x: x[1], reverse=True)
    else:
        # If the list is full, replace the user with the lowest follower count
        if follower_count > top_users[-1][1]:
            top_users.pop()
            top_users.append((user_id, follower_count))
            top_users.sort(key=lambda x: x[1], reverse=True)

# Print the top users
for user_id, follower_count in top_users:
    print(f"{user_id}\t{follower_count}")