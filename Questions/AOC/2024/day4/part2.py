def valid(grid, x, y):
    top_left, top_right, bottom_left, bottom_right = grid[x-1][y-1], grid[x-1][y+1], grid[x+1][y-1], grid[x+1][y+1]

    if (top_left == "M" and bottom_right == "S") and (top_right == "S" and bottom_left == "M"):
        return True
    if (top_left == "M" and bottom_right == "S") and (top_right == "M" and bottom_left == "S"):
        return True
    if (top_left == "S" and bottom_right == "M") and (top_right == "S" and bottom_left == "M"):
        return True
    if (top_left == "S" and bottom_right == "M") and (top_right == "M" and bottom_left == "S"):
        return True

def solution(file_path):
    grid = [list(l.strip()) for l in open(file_path)]
    m = len(grid)
    n = len(grid[0])

    count = 0
    for x in range(1, m - 1):
        for y in range(1, n - 1):
            if grid[x][y] == "A":
                count += bool(valid(grid, x, y))
    return count

print(solution("input.txt"))