'''
    DFS
        TC: O(rows * cols)
        SC: O(rows * cols), recursive call stack calls all the 1s in the worst case
'''

# Modifying input to a value of 0 for parent nodes and neighbors
class Solution1:
    def numIslands(self, grid):
        def dfs(grid, row, col):            
            grid[row][col] = "0"
            
            if row - 1 >= 0 and grid[row-1][col] == "1": dfs(grid, row - 1, col)
            if row + 1 < len(grid) and grid[row+1][col] == "1": dfs(grid, row + 1, col)
            if col - 1 >= 0 and grid[row][col-1] == "1": dfs(grid, row, col - 1)
            if col + 1 < len(grid[0]) and grid[row][col+1] == "1": dfs(grid, row, col + 1)
        
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(grid, r, c)    
        return islands

# Using hash set to keep track of parent nodes and neighbors
class Solution2:
    def numIslands(self, grid):
        visited = set()
        
        def dfs(grid, row, col):
            visited.add((row,col))
            
            if row - 1 >= 0 and grid[row-1][col] == "1" and (row - 1, col) not in visited: 
                dfs(grid, row - 1, col)
                visited.add((row - 1, col))
            if row + 1 < len(grid) and grid[row+1][col] == "1" and (row + 1, col) not in visited:
                dfs(grid, row + 1, col)
                visited.add((row + 1, col))
            if col - 1 >= 0 and grid[row][col-1] == "1" and (row, col - 1) not in visited:
                dfs(grid, row, col - 1)
                visited.add((row, col - 1))
            if col + 1 < len(grid[0]) and grid[row][col+1] == "1" and (row, col + 1) not in visited:
                dfs(grid, row, col + 1)
                visited.add((row, col + 1))
            
        if not grid: return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(grid, r, c)
        return islands

'''
    Explanation: BFS
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

        neighbors = [(2,1), (3,0), (1,2), (0,3)] - this still continues
        
        TC: O(rows * cols)
        SC: O(min(rows, cols))
'''

import collections
from typing import List

# Modifying input to a value of 0 for parent nodes and neighbors
class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    neighbors = collections.deque([(r,c)])
                    grid[r][c] = "0"
                    
                    while neighbors:
                        row, col = neighbors.popleft()
                        if row - 1 >= 0 and grid[row-1][col] == "1":
                            neighbors.append((row-1, col))
                            grid[row-1][col] = "0"
                        if row + 1 < rows and grid[row+1][col] == "1":
                            neighbors.append((row+1, col))
                            grid[row+1][col] = "0"
                        if col - 1 >= 0 and grid[row][col-1] == "1":
                            neighbors.append((row, col-1))
                            grid[row][col-1] = "0"
                        if col + 1 < cols and grid[row][col+1] == "1":
                            neighbors.append((row, col+1))
                            grid[row][col+1] = "0"
                    islands += 1
                        
        return islands

# Using hash set to keep track of parent nodes and neighbors
class Solution4:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    neighbors = collections.deque([(r,c)])
                    visited.add((r, c))
                    
                    while neighbors:
                        row, col = neighbors.popleft()
                        if row - 1 >= 0 and grid[row-1][col] == "1" and (row - 1, col) not in visited:
                            neighbors.append((row - 1, col))
                            visited.add((row - 1, col))
                        if row + 1 < rows and grid[row+1][col] == "1" and (row + 1, col) not in visited:
                            neighbors.append((row + 1, col))
                            visited.add((row + 1, col))
                        if col - 1 >= 0 and grid[row][col-1] == "1" and (row, col - 1) not in visited:
                            neighbors.append((row, col - 1))
                            visited.add((row, col - 1))
                        if col + 1 < cols and grid[row][col+1] == "1" and (row, col + 1) not in visited:
                            neighbors.append((row, col + 1))
                            visited.add((row, col + 1))
                    islands += 1
                        
        return islands