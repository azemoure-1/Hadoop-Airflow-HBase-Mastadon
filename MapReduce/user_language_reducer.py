#!/usr/bin/env python3


#import sys

#language_count = {}

#for line in sys.stdin:
#    language, count = line.strip().split('\t')
#    count = int(count)

#    if language not in language_count:
#        language_count[language] = count
#    else:
#        language_count[language] += count

#for language, count in language_count.items():
#    print(f"{language}\t{count}")




import happybase
import sys

# Connect to HBase
connection = happybase.Connection()
table = connection.table('user_languages1')

# Read from standard input and insert into HBase
for line in sys.stdin:
    try:
        user_id, language = line.strip().split('\t')
        table.put(user_id.encode('utf-8'), {'language:preference': language.encode('utf-8')})
    except Exception as e:
        print(f"Error inserting data: {str(e)}")

# Close the HBase connection
connection.close()


