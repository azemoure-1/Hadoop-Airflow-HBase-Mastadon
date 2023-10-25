#!/usr/bin/env python3

#import sys
#import json

#for line in sys.stdin:
#    try:
#        user_data = json.loads(line.strip())
#        language = user_data.get('language', 'Unknown')
#        print(f"{language}\t1")
#    except json.JSONDecodeError:
#       pass






import sys
import json

for line in sys.stdin:
    try:
        data = json.loads(line.strip())
        user_id = data["account"]["id"]
        language = data["language"]
        print(f"{user_id}\t{language}")
    except Exception as e:
        print(f"Error processing data: {str(e)}")


