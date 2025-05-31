"""
5
4 1 5 2 3
5
1 3 7 9 5
"""

import sys

input = sys.stdin.readline

_ = input().strip()
data = list(map(int, input().strip().split()))
_ = input().strip()
target_data = list(map(int, input().strip().split()))

hashtable = {}
for value in data:
    hashtable[value] = True

result = ""
for value in target_data:
    try:
        hashtable[value]
        result += "1\n"
    except:
        result += "0\n"

print(result.rstrip())