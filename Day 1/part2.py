left_list = []
right_list = []


def min_count(list, num):
    count = list.count(num)

    return count


with open('input.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        left, right = map(int, parts)
        left_list.append(left)
        right_list.append(right)

sim_score = []

for num in left_list:
    count = min_count(right_list, num)
    similarity = num * count
    sim_score.append(similarity)


print(sum(sim_score))