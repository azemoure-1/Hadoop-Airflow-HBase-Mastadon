#!/usr/bin/env python3

import sys
import json
import re

for line in sys.stdin:
    try:
        post_data = json.loads(line.strip())
        content = post_data.get('content', '')

        # Find hashtags (tags)
        tags = re.findall(r'#\w+', content)
        for tag in tags:
            print(f"{tag}\t1")

    except json.JSONDecodeError:
        pass

