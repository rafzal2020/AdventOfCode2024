word = "MAS"
"""
M   S
  A
M   S
"""

grid =[]
marked_a = []
with open("input.txt", 'r') as file:
    for line in file:
        grid.append(list(line.strip()))

def search_xmas(grd):
    count = 0
    rows, cols = len(grd), len(grd[0])
    directions = [(1,1),(1,-1)]

    def is_valid(x,y):
        return 0 <= x < rows and 0 <= y < cols

    def is_valid_x(x,y,dx,dy):
            nx = x
            ny = y
            for i in range(len(word)):
                if not is_valid(nx,ny) or grd[nx][ny] != word[i]:
                    break
                if word[i] == 'A':
                    marked_a.append(i)

                nx += dx
                ny += dy
            else:
                return True

    for i in range(rows):
        for j in range(cols):
            if grd[i][j] == word[0]:
                if 0 < j + 2 < cols:
                    if is_valid_x(i, j, 1, 1) and is_valid_x(i, j+2, 1, -1):
                        count += 1

    return count


print(search_xmas(grid))


