file = open('./Day 1/input.txt', 'r')
input = file.read()
# print(input)

count = 0
in_basement = False
for i, char in enumerate(input):
    if (char == '('):
        count += 1
    else:
        count -= 1
    if count == -1 and not in_basement:
        print('Entered basement at character position:', i + 1)
        in_basement = True
print('Santa will end up at floor', count)  # 232
