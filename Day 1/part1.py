left_list = []
right_list = []

with open('input.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        left, right = map(int, parts)
        left_list.append(left)
        right_list.append(right)

total_dis = []

while left_list or right_list:
    min_left = min(left_list)
    min_right = min(right_list)

    left_list.remove(min_left)
    right_list.remove(min_right)

    distance = abs(min_left - min_right)
    total_dis.append(distance)

print(sum(total_dis))