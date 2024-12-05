order_map = {}
page_orders = []

middle_count = 0

with open('input.txt', 'r') as file:
    for i, line in enumerate(file, start=1):
        if i > 1176:
            break
        line = line.strip()
        if '|' in line:
            key, value = line.split('|')

            key = int(key)
            value = int(value)

            if key in order_map:
                if value not in order_map[key]:
                    order_map[key].append(int(value))
            else:
                order_map[key] = [value]

with open('input.txt', 'r') as file:
    for i, line in enumerate(file, start=1):
        if i <= 1177:
            continue
        line = line.strip()
        if line:
            numbers = [int(num) for num in line.split(',')]
            page_orders.append(numbers)


def is_valid_order(sublist):
    for i in range(len(sublist)):
        if i + 1 < len(sublist):
            if sublist[i + 1] not in order_map[sublist[i]]:
                return False

    return True


for page_order in page_orders:
    if is_valid_order(page_order):
        middle_count += page_order[len(page_order)//2]

print(middle_count)