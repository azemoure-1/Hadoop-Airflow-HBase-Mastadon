#!/usr/bin/env python3

import sys

#current_url = None
#url_count = 0

#for line in sys.stdin:
#    try:
#        url, count = line.strip().split('\t')

#        if current_url == url:
#            url_count += int(count)
#        else:
#            if current_url:
                # Output the URL and its count
#                print(f"{current_url}\t{url_count}")
#            current_url = url
#            url_count = int(count)

#    except ValueError:
        # Ignore lines that don't have the expected format
#        continue

# Output the most shared external URL and its count
#if current_url:
#    print(f"{current_url}\t{url_count}")

import happybase
import sys

# Connect to HBase
connection = happybase.Connection()
table = connection.table('toots')

# Read from standard input and insert into HBase
for line in sys.stdin:
    try:
        toot_id, content, created_at, user_id = line.strip().split('\t')
        # Define the HBase row key, which should be unique for each Toot
        row_key = toot_id.encode('utf-8')
        data = {
            'content:content': content.encode('utf-8'),
            'content:created_at': created_at.encode('utf-8'),
            'content:user_id': user_id.encode('utf-8')
        }
        table.put(row_key, data)
    except Exception as e:
        print(f"Error inserting data: {str(e)}")

# Close the HBase connection
connection.close()

