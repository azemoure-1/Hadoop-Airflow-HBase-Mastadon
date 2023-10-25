#!/usr/bin/env python3

#import sys
#import json

#for line in sys.stdin:
#    try:
#        post_data = json.loads(line.strip())
#        media_attachments = post_data.get('media_attachments', [])
#        if media_attachments:
#            print("Media\t1")
#        else:
#            print("No Media\t1")
#    except json.JSONDecodeError:
#        pass


import sys
import json

for line in sys.stdin:
    try:
        data = json.loads(line.strip())
        user_id = data["account"]["id"]
        media_count = len(data.get("media_attachments", []))
        print(f"{user_id}\t{media_count}")
    except Exception as e:
        print(f"Error processing data: {str(e)}")

