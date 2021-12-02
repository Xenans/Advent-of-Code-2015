import re
file = open('./Day 5/input.txt', 'r')
inputs = [line.strip() for line in file]
print(inputs)


def isNiceOne(string: str) -> bool:
    # Condition 1: at least 3 vowels
    cond_1 = re.search('[aeiou].*[aeiou].*[aeiou]', string)
    # Condition 2: at least one repeated character
    cond_2 = re.search('(.)\\1', string)
    # Condition 3: none of 'ab', 'cd', 'pq', or 'xy'
    cond_3 = not re.search('(ab|cd|pq|xy)', string)
    # print(cond_1, cond_2, cond_3)
    if (cond_1 and cond_2 and cond_3):
        return True
    return False


def isNiceTwo(string: str) -> bool:
    # Condition 1: a pair of letters that repeats somewhere in the string without overlap
    cond_1 = re.search('(..).*\\1', string)
    # Condition 2: a letter that repeats with a letter inbetween
    cond_2 = re.search('(.).\\1', string)
    if (cond_1 and cond_2):
        return True
    return False


nice_count_one = 0
nice_count_two = 0
for string in inputs:
    if (isNiceOne(string)):
        nice_count_one += 1
    if (isNiceTwo(string)):
        nice_count_two += 1
print(f'There are {nice_count_one} nice (1) strings!')
print(f'There are {nice_count_two} nice (2) strings!')
