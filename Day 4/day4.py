import hashlib
file = open('./Day 4/input.txt', 'r')
key = file.read()
print('key:', key)

smallest_5 = 0
smallest_6 = 0

num = 0
while True:
    num += 1
    input = f'{key}{num}'
    hash = hashlib.md5()
    hash.update(input.encode('utf8'))
    digested = hash.digest()
    # print(digested)
    # print(digested.hex())
    if (digested.hex()[0:5] == '00000' and not smallest_5):
        smallest_5 = num
    if (digested.hex()[0:6] == '000000'):
        smallest_6 = num
        break

print('Smallest number that produces 5 leading zeroes:', smallest_5)
print('Smallest number that produces 6 leading zeroes:', smallest_6)
