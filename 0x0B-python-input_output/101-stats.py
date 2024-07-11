#!/usr/bin/python3
"""
Python script that reads lines from stdin
(like it's being piped from another program)
and computes some metrics based on those lines.
"""
import sys
from collections import defaultdict


totalFileSize = 0
codeCount = defaultdict(int)
lineCount = 0

setStatusCode = {200, 301, 400, 401, 403, 404, 405, 500}
for code in setStatusCode:
    codeCount[code] = 0

try:
    for line in sys.stdin:
        lineCount += 1
        parts = line.split()
        fileSize = int(parts[-1])
        totalFileSize += fileSize
        statusCode = int(parts[-2])
        if statusCode in setStatusCode:
            codeCount[statusCode] += 1
        if lineCount % 10 == 0:
            print(f"File size: {totalFileSize}")
            for code in sorted(codeCount.keys()):
                if codeCount[code] > 0:
                    print(f"{code}: {codeCount[code]}")
            print()
            sys.stdout.flush()

except KeyboardInterrupt:
    print(f"File size: {totalFileSize}")
    for code in sorted(codeCount.keys()):
        if codeCount[code] > 0:
            print(f"{code}: {codeCount[code]}")
