from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if not (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and (r, c) not in visited and grid[r][c] == 1):
                return 0
            
            visited.add((r, c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
        
        visited = set()
        res = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, dfs(r, c))
        return res