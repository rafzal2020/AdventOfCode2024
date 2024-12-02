def is_safe(nums):
    if nums == sorted(nums, reverse=True):
        return True
    elif nums == sorted(nums):
        return True
    else:
        return False


count = 0

with open('input.txt', 'r') as file:
    for line in file:
        numbers = list(map(int, line.strip().split()))
        if is_safe(numbers):
            print(numbers)
            count += 1

print(count)
