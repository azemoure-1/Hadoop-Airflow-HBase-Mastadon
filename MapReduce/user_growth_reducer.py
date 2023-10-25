#!/usr/bin/env python3
import sys

#current_date = None
#user_count = 0

#for line in sys.stdin:
#    try:
#        date, count = line.strip().split('\t')

#        if current_date == date:
#            user_count += int(count)
#        else:
#            if current_date:
                # Output the date and user count
#                print(f"{current_date}\t{user_count}")
#            current_date = date
#            user_count = int(count)

#    except ValueError:
        # Ignore lines that don't have the expected format
#        continue

# Output the last date and user count
#if current_date:
#    print(f"{current_date}\t{user_count}")


import happybase
import sys

# Connect to HBase
connection = happybase.Connection()
table = connection.table('user_growth')

# Read from standard input and insert into HBase
for line in sys.stdin:
    try:
        user_id, created_at = line.strip().split('\t')
        table.put(user_id.encode('utf-8'), {'growth:created_at': created_at.encode('utf-8')})
    except Exception as e:
        print(f"Error inserting data: {str(e)}")

# Close the HBase connection
connection.close()

