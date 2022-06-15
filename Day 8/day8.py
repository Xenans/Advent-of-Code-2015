import re
file = open('./Day 8/input.txt', 'r')
input = [line.strip() for line in file]
count = 0
encode_count = 0
for line in input:
    count += 2
    encode_count += 2
    matches = re.findall(r'(\\\\|\\"|\\x..)', line)
    encode_matches = re.findall(r'("|\\)', line)
    if matches:
        for match in matches:
            if ('x' in match):
                count += 3
            else:
                count += 1
    if encode_matches:
        for match in encode_matches:
            encode_count += 1
print(count)
print(encode_count)
