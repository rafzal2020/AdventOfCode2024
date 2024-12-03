import re

text = "mul(,)"

pattern = r'mul\(\s*([-+]?\d*\.?\d+)\s*,\s*([-+]?\d*\.?\d+)\s*\)'
regex = re.compile(pattern)

with open('input.txt', 'r') as file:
    content = file.read()

matches = regex.findall(content)

total_sum = 0

for x, y in matches:
    num_x = float(x)
    num_y = float(y)
    prod = num_x * num_y
    total_sum += prod

print(total_sum)
