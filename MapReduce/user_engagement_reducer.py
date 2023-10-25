#!/usr/bin/env python3
import sys

# Process input from standard input
#for line in sys.stdin:
#    try:
#        user_id, engagement_rate = line.strip().split('\t')
#        engagement_rate = float(engagement_rate)

        # Emit the user_id and engagement_rate
#        print(f"{user_id}\t{engagement_rate}")

#    except ValueError:
        # Handle invalid input, if necessary
#        pass


import happybase
import sys

# Connect to HBase
connection = happybase.Connection()
table = connection.table('user_engagement')

# Read from standard input and insert into HBase
for line in sys.stdin:
    try:
        user_id, engagement = line.strip().split('\t')
        table.put(user_id.encode('utf-8'), {'engagement:score': engagement.encode('utf-8')})
    except Exception as e:
        print(f"Error inserting data: {str(e)}")

# Close the HBase connection
connection.close()

