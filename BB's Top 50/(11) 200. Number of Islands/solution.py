class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        def dfs(grid, x, y, r, c):
            if x < 0 or x >= r or y < 0 or y >= c or grid[x][y] != "1":
                return
            
            grid[x][y] = "2"
            
            dfs(grid, x, y-1, r, c) # down
            dfs(grid, x+1, y, r, c) # right
            dfs(grid, x, y+1, r, c) # top
            dfs(grid, x-1, y, r, c) # left
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(grid, r, c, rows, cols)
                    islands += 1
        return islands


# Iterative solution using bfs
#         if not grid:
#             return 0

#         rows, cols = len(grid), len(grid[0])
#         visited = set()
#         islands = 0

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r,c) not in visited:
#                     bfs(r,c)
#                     islands += 1
#         return islands

# def bfs(r,c):
#     q = collections.deque()
#     visited.add((r,c))
#     q.append((r,c))

#     while q:
#         row, col = q.popleft()
#         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#         for dr, dc in directions:
#             r, c = row+dr, col+dc
#             if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited):
#                 q.append((r,c))
#                 visited.add((r,c))

