#!/usr/bin/env python3

import sys

# Initialize variables to accumulate follower counts for each user
#current_user = None
#total_followers = 0

# Read input from standard input
#for line in sys.stdin:
    # Split the input line into user_id and follower_count
#    user_id, follower_count = line.strip().split('\t')
#    follower_count = int(follower_count)

    # If the user_id changes, print the total followers for the current user
#    if user_id != current_user:
#        if current_user is not None:
#            print(f"{current_user}\t{total_followers}")
#        current_user = user_id
#        total_followers = 0

    # Accumulate the follower counts for the current user
#    total_followers += follower_count

# Print the total followers for the last user
#if current_user is not None:
#    print(f"{current_user}\t{total_followers}")




import happybase
import sys

# Connect to HBase
connection = happybase.Connection()
table = connection.table('users')

# Read from standard input and insert into HBase
for line in sys.stdin:
    try:
        user, follower_count = line.strip().split('\t')
        # Ensure that 'user' and 'follower_count' are correctly extracted from the line
        # and are in the expected format.
        table.put(user.encode('utf-8'), {'following:count': follower_count.encode('utf-8')})
    except Exception as e:
        print(f"Error inserting data: {str(e)}")

# Close the HBase connection
connection.close()

