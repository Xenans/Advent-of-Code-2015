from functools import lru_cache
import re
file = open('./Day 7/input.txt', 'r')
input = [line.strip() for line in file]
values = {}
for instruction in input:
    match = re.match('(.+) -> (.+)', instruction)
    name = match.group(2)
    value = match.group(1)
    values[name] = value


@lru_cache(maxsize=300)
def calculate(wire):
    if wire.isnumeric():
        return int(wire)
    instruction = values[wire]
    # print(f'Calculating {instruction}...')
    match = re.match('(.*)(NOT|OR|AND|LSHIFT|RSHIFT)(.*)', instruction)
    if match:
        wire1 = match.group(1).strip()
        operator = match.group(2)
        wire2 = match.group(3).strip()
        if (operator == 'NOT'):
            return ~calculate(wire2)
        elif (operator == 'OR'):
            return calculate(wire1) | calculate(wire2)
        elif (operator == 'AND'):
            return calculate(wire1) & calculate(wire2)
        elif (operator == 'LSHIFT'):
            return calculate(wire1) << calculate(wire2)
        elif (operator == 'RSHIFT'):
            return calculate(wire1) >> calculate(wire2)
    else:
        # Signal assignment case
        return calculate(instruction)


answer_1 = calculate('a')
print(answer_1)  # 3176
calculate.cache_clear()
values['b'] = f'{answer_1}'
answer_2 = calculate('a')
print(answer_2)  # 1471
