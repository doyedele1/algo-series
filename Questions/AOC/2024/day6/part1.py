def find_guard_position_and_direction(grid):
    directions = "^>v<"
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in directions:
                return r, c, directions.index(cell)

def move_guard(grid, guard_row, guard_col, guard_dir, visited, directions):
    # Returns updated (guard_row, guard_col, guard_dir) and a flag indicating if the guard leaves the grid.
    m, n = len(grid), len(grid[0])
    dx, dy = directions[guard_dir]
    next_row, next_col = guard_row + dx, guard_col + dy

    # Out of bounds
    if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
        return guard_row, guard_col, guard_dir, True

    if grid[next_row][next_col] == "#":
        guard_dir = (guard_dir + 1) % 4
    else:
        guard_row, guard_col = next_row, next_col
        visited.add((guard_row, guard_col))

    return guard_row, guard_col, guard_dir, False

def solution(file):
    with open(file, 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    # Direction vectors (up, right, down, left)
    directions = [
        (-1, 0),  # Up
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
    ]

    guard_row, guard_col, guard_dir = find_guard_position_and_direction(grid)

    visited = set()
    visited.add((guard_row, guard_col))

    while True:
        guard_row, guard_col, guard_dir, has_guard_left_grid = move_guard(grid, guard_row, guard_col, guard_dir, visited, directions)
        if has_guard_left_grid:
            break

    return len(visited)

# def turn_right(direction):
#     direction_order = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Up, Right, Down, Left
#     new_index = (direction_order.index(direction) + 1) % 4
#     return direction_order[new_index]

# def can_move(grid, position, direction):
#     """Checks if the guard can move forward."""
#     x, y = position
#     dx, dy = direction
#     nx, ny = x + dx, y + dy
#     return 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] != '#'

# def mark_visited(grid, position):
    """Marks a position as visited with an 'X'."""
    x, y = position
    if grid[y][x] != '#':  # Avoid overwriting obstacles
        grid[y][x] = 'X'

print(solution("input.txt"))