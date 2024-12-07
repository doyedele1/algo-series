def find_guard_position_and_direction(grid):
    directions = "^>v<"
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col in directions:
                return r, c, directions.index(col)

def move_guard_with_obstacle(grid, guard_row, guard_col, guard_dir, obstacle_row, obstacle_col):
    # Returns True if the guard falls into a loop; False if the guard exits the grid
    directions = [
        (-1, 0),  # Up
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
    ]

    m, n = len(grid), len(grid[0])
    visited = set()
    visited.add((guard_row, guard_col, guard_dir))

    while True:
        dx, dy = directions[guard_dir]
        next_row, next_col = guard_row + dx, guard_col + dy

        # Out of bounds
        if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
            return False

        next_cell = (
            "#"
            if (next_row == obstacle_row and next_col == obstacle_col)
            else grid[next_row][next_col]
        )

        if next_cell == "#":
            guard_dir = (guard_dir + 1) % 4
        else:
            guard_row, guard_col = next_row, next_col

        state = (guard_row, guard_col, guard_dir)
        if state in visited:
            return True
        visited.add(state)

def solution(file):
    with open(file, 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    count = 0
    m, n = len(grid), len(grid[0])
    guard_row, guard_col, guard_dir = find_guard_position_and_direction(grid)

    for r in range(m):
        for c in range(n):
            # Skip positions that are not empty or are the starting position
            if grid[r][c] == "#" or (r == guard_row and c == guard_col):
                continue
            # Simulate guard movement with an obstacle at (r, c)
            if move_guard_with_obstacle(grid, guard_row, guard_col, guard_dir, r, c):
                count += 1
    return count

print(solution("input.txt"))