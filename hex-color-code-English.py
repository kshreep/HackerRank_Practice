import re

n = int(input())
for i in range(n):
    words = re.findall("(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})(?=[;,)])", input())
    for word in words:
        print(word)