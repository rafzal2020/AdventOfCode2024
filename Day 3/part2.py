import re

pattern = r'mul\(\s*([-+]?\d*\.?\d+)\s*,\s*([-+]?\d*\.?\d+)\s*\)'

with open('input.txt', 'r') as file:
    content = file.read()

commands = re.findall(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', content)

total_sum = 0
enabled = True

for command in commands:
    if command == "do()":
        enabled = True
    elif command == "don't()":
        enabled = False
    elif enabled and command.startswith("mul"):
        x, y = command[4:-1].split(',')
        x = int(x)
        y = int(y)
        prod = x * y
        total_sum += prod

print(total_sum)
