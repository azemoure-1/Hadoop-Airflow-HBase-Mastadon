#!/usr/bin/env python3

import sys
import json
import re

# Regular expression to match URLs in text
url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

for line in sys.stdin:
    try:
        user_data = json.loads(line.strip())
        content = user_data.get('content', '')

        # Find all URLs in the content
        urls = re.findall(url_pattern, content)

        for url in urls:
            # Output the URL with a count of 1
            print(f"{url}\t1")

    except json.JSONDecodeError:
        # Handle invalid JSON data, if necessary
        pass