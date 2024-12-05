word = "MAS"
"""
M   S
  A
M   S

"""
"""
S   M
  A 
S   M
"""

"""
M   M
  A
S   S
"""
"""
S   S
  A 
M   M
"""

grid = []
with open("input.txt", 'r') as file:
    for line in file:
        grid.append(list(line.strip()))


def search_xmas(grd):
    count = 0
    rows, cols = len(grd), len(grd[0])

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def is_valid_x(x, y):
        if not is_valid(x, y) or grd[x][y] != 'A':
            return False

        if is_valid(x, y) and grd[x][y] == 'A':
            # Check for case with M's on left side
            if ((is_valid(x - 1, y - 1) and grd[x - 1][y - 1] == 'M' and is_valid(x + 1, y + 1) and grd[x + 1][
                y + 1] == 'S') and
                    (is_valid(x + 1, y - 1) and grd[x + 1][y - 1] == 'M' and is_valid(x - 1, y + 1) and grd[x - 1][
                        y + 1] == 'S')):
                return True
            # Check for case with M's on right side
            elif ((is_valid(x - 1, y + 1) and grd[x - 1][y + 1] == 'M' and is_valid(x + 1, y - 1) and grd[x + 1][
                y - 1] == 'S') and
                  (is_valid(x + 1, y + 1) and grd[x + 1][y + 1] == 'M' and is_valid(x - 1, y - 1) and grd[x - 1][
                      y - 1] == 'S')):
                return True
            # Check for case with M's on the top
            elif ((is_valid(x - 1, y - 1) and grd[x - 1][y - 1] == 'M' and is_valid(x + 1, y + 1) and grd[x + 1][
                y + 1] == 'S') and
                  (is_valid(x - 1, y + 1) and grd[x - 1][y + 1] == 'M' and is_valid(x + 1, y - 1) and grd[x + 1][
                      y - 1] == 'S')):
                return True
            # Check for case with M's on the bottom
            elif ((is_valid(x + 1, y - 1) and grd[x + 1][y - 1] == 'M' and is_valid(x - 1, y + 1) and grd[x - 1][
                y + 1] == 'S') and
                  (is_valid(x + 1, y + 1) and grd[x + 1][y + 1] == 'M' and is_valid(x - 1, y - 1) and grd[x - 1][
                      y - 1] == 'S')):
                return True

    for i in range(rows):
        for j in range(cols):
            if is_valid_x(i, j):
                count += 1

    return count


print(search_xmas(grid))
