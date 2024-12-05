word = "XMAS"

grid =[]
with open("input.txt", 'r') as file:
    for line in file:
        grid.append(list(line.strip()))

def search_xmas(grd):
    count = 0
    rows, cols = len(grd), len(grd[0])
    directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]

    def is_valid(x,y):
        return 0 <= x < rows and 0 <= y < cols

    def search(x,y,dx,dy):
            nx = x
            ny = y
            for i in range(len(word)):
                if not is_valid(nx,ny) or grd[nx][ny] != word[i]:
                    break
                nx += dx
                ny += dy
            else:
                return True

    for i in range(rows):
        for j in range(cols):
            if grd[i][j] == word[0]:
                for dx, dy in directions:
                    if search(i, j, dx, dy):
                        count += 1

    return count


print(search_xmas(grid))


