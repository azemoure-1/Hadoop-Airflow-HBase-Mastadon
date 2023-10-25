#!/usr/bin/env python3

import sys

#media_counts = {"Media": 0, "No Media": 0}

#for line in sys.stdin:
#    key, count = line.strip().split('\t')
#    media_counts[key] += int(count)

#for key, count in media_counts.items():
#    print(f"{key}\t{count}")


import happybase
import sys

# Connect to HBase
connection = happybase.Connection()
table = connection.table('user_media')

# Read from standard input and insert into HBase
for line in sys.stdin:
    try:
        user_id, media_count = line.strip().split('\t')
        table.put(user_id.encode('utf-8'), {'media:count': media_count.encode('utf-8')})
    except Exception as e:
        print(f"Error inserting data: {str(e)}")

# Close the HBase connection
connection.close()

