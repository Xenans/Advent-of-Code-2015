file = open('./Day 3/input.txt', 'r')
inputs = file.read()
print(inputs)

# No literal constructor for python sets unfortunately...
santa_pos = (0, 0)
santa_traversed = {santa_pos}

for char in inputs:
    if char == '>':
        santa_next = (santa_pos[0] + 1, santa_pos[1])
    elif char == '^':
        santa_next = (santa_pos[0], santa_pos[1] + 1)
    elif char == '<':
        santa_next = (santa_pos[0] - 1, santa_pos[1])
    elif char == 'v':
        santa_next = (santa_pos[0], santa_pos[1] - 1)
    santa_pos = santa_next
    santa_traversed.add(santa_pos)
print(len(santa_traversed))


# Santa and robo version
santa_pos = (0, 0)
robo_pos = (0, 0)
traversed = {robo_pos}

for i, char in enumerate(inputs):
    if (i % 2 == 0):
        current_pos = santa_pos
    else:
        current_pos = robo_pos

    if char == '>':
        next = (current_pos[0] + 1, current_pos[1])
    elif char == '^':
        next = (current_pos[0], current_pos[1] + 1)
    elif char == '<':
        next = (current_pos[0] - 1, current_pos[1])
    elif char == 'v':
        next = (current_pos[0], current_pos[1] - 1)

    if (i % 2 == 0):
        santa_pos = next
        traversed.add(santa_pos)
    else:
        robo_pos = next
        traversed.add(robo_pos)
print(len(traversed))
