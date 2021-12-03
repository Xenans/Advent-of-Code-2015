import re
import numpy as np
file = open('./Day 6/input.txt', 'r')
input = [line.strip() for line in file]

board1 = np.zeros((1000, 1000))
board2 = np.zeros((1000, 1000))

for instruction in input:
    match = re.match(
        '(turn on|turn off|toggle) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)', instruction)
    command = match.group(1)
    x1 = int(match.group(2))
    y1 = int(match.group(3))
    x2 = int(match.group(4))
    y2 = int(match.group(5))
    print(command, x1, y2, x2, y2)
    width = x2 - x1 + 1
    height = y2 - y1 + 1
    if (command == 'turn on'):
        board1[x1:x2+1,y1:y2+1] = np.ones((width, height))
        board2[x1:x2+1,y1:y2+1] += 1
    elif (command == 'turn off'):
        board1[x1:x2+1,y1:y2+1] = np.zeros((width, height))
        board2[x1:x2+1,y1:y2+1] -= 1
        board2 = board2.clip(min=0)
    elif (command == 'toggle'):
        board1[x1:x2+1,y1:y2+1] = np.logical_not(board1[x1:x2+1,y1:y2+1])
        board2[x1:x2+1,y1:y2+1] += 2

print(int(board1.sum()))
print(int(board2.sum()))