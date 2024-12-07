def is_in_bound(m, n, x, y):
    return 0 <= x < m and 0 <= y < n

def solution(file_path):
    with open(file_path, 'r') as f:
        grid = [line.strip() for line in f]

    m = len(grid)
    n = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0),  # Up
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, -1), # Diagonal up-left
        (-1, 1)   # Diagonal up-right
    ]
    count = 0

    def dfs(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_in_bound(m, n, nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    for x in range(m):
        for y in range(n):
            for dx, dy in directions:
                if dfs(x, y, dx, dy):
                    count += 1

    return count

print(solution("input.txt"))