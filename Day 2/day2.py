import re

file = open('./Day 2/input.txt', 'r')
inputs = [row.strip() for row in file]
# print(inputs)

paper_area = 0
ribbon_length = 0

for row in inputs:
    length, width, height = re.match('(\d+)x(\d+)x(\d+)', row).groups()
    length, width, height = int(length), int(width), int(height)
    volume = length*width*height
    area1, area2, area3 = length*width, width*height, height*length
    smallest_area = min(area1, area2, area3)
    perimeter1, perimeter2, perimeter3 = 2 * \
        (length + width), 2*(width + height), 2*(height + length)
    smallest_perimeter = min(perimeter1, perimeter2, perimeter3)
    paper_area += 2*area1 + 2*area2 + 2*area3 + smallest_area
    ribbon_length += smallest_perimeter + volume
print(
    f'The elves will need a total of {paper_area} square feet of wrapping paper')
print(f'The elves will also need {ribbon_length} feet of ribbons!')
