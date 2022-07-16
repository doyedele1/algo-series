class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0   
        
        def dfs(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in visited and grid[r][c] == 1):
                return 0
            visited.add((r, c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area