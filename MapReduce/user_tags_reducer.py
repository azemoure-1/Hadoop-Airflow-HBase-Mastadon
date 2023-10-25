#!/usr/bin/env python3

import sys

#current_tag = None
#tag_count = 0

#for line in sys.stdin:
#    try:
#        tag, count = line.strip().split('\t')
#        count = int(count)

#        if current_tag == tag:
#            tag_count += count
#        else:
#            if current_tag:
#                print(f"{current_tag}\t{tag_count}")
#            current_tag = tag
#            tag_count = count

#    except ValueError:
#        continue

# Output the last tag
#if current_tag:
#    print(f"{current_tag}\t{tag_count}")


#!/usr/bin/env python3

import sys
import happybase

# Connect to HBase
connection = happybase.Connection()
table = connection.table('user_tags')

current_tag = None
tag_count = 0

for line in sys.stdin:
    try:
        tag, count = line.strip().split('\t')
        count = int(count)

        if current_tag == tag:
            tag_count += count
        else:
            if current_tag:
                # Insert the tag and count into HBase
                table.put(current_tag.encode('utf-8'), {'tags:count': str(tag_count).encode('utf-8')})
            current_tag = tag
            tag_count = count

    except ValueError:
        continue

# Output the last tag
if current_tag:
    # Insert the last tag and count into HBase
    table.put(current_tag.encode('utf-8'), {'tags:count': str(tag_count).encode('utf-8')})

# Close the HBase connection
connection.close()

