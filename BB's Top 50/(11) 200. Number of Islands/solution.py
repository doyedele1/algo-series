'''
    Explanation:
        DFS
            [
                [1,1,1,1],
                [1,1,1,1],
                [1,1,1,1],
                [1,1,1,1]
            ]
            Space Complexity: O(m*n), recursive call stack calls all the 1s
'''

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

'''
        BFS
            [
                [1,1,1,1],
                [1,1,1,1],
                [1,1,1,1],
                [1,1,1,1]
            ]

            neighbors = [(0,0)]
            
            [
                [0,0,1,1],
                [0,1,1,1],
                [1,1,1,1],
                [1,1,1,1]
            ]

            neighbors = [(1,0), (0,1)]
            
            [
                [0,0,1,1],
                [0,0,1,1],
                [0,1,1,1],
                [1,1,1,1]
            ]

            neighbors = [(0,1), (2,0), (1,1)]
            
            [
                [0,0,0,1],
                [0,0,1,1],
                [0,1,1,1],
                [1,1,1,1]
            ]

            neighbors = [(2,0), (1,1), (0,2)]
            
            [
                [0,0,0,1],
                [0,0,1,1],
                [0,0,1,1],
                [0,1,1,1]
            ]

            neighbors = [(1,1), (0,2), (2,1), (3,0)]
            
            [
                [0,0,0,1],
                [0,0,0,1],
                [0,0,1,1],
                [0,1,1,1]
            ]

            neighbors = [(0,2), (2,1), (3,0), (1,2)]
            
            [
                [0,0,0,0],
                [0,0,0,1],
                [0,0,1,1],
                [0,1,1,1]
            ]

            neighbors = [(2,1), (3,0), (1,2), (0,3)]
            
            Space Complexity: O(min(nr, nc))
'''
import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    neighbors = collections.deque([(r,c)])
                    grid[r][c] = "2"
                    
                    while neighbors:
                        row, col = neighbors.popleft()
                        if row - 1 >= 0 and grid[row-1][col] == "1":
                            neighbors.append((row-1, col))
                            grid[row-1][col] = "2"
                        if row + 1 < rows and grid[row+1][col] == "1":
                            neighbors.append((row+1, col))
                            grid[row+1][col] = "2"
                        if col - 1 >= 0 and grid[row][col-1] == "1":
                            neighbors.append((row, col-1))
                            grid[row][col-1] = "2"
                        if col + 1 < cols and grid[row][col+1] == "1":
                            neighbors.append((row, col+1))
                            grid[row][col+1] = "2"
                            
                    islands += 1
                        
        return islands

