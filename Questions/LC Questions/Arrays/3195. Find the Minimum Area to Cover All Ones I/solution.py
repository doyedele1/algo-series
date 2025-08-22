'''
    Explanation:
        Find the topMost point (low_x), bottomMost point (high_x), leftMost point (low_y) and rightMost point (high_y)
        Then minimize the low_x and low_y points and maximize the high_x and high_y points

        So initially, low_x = INF, high_x = -1, low_y = INF, high_y = -1

        For grid = [[0, 1, 0], [1, 0, 1]]

        Where we see 1:
            (r,c) = (0, 1)
            low_x = min(INF, 0) = 0
            high_x = max(-1, 0) = 0
            low_y = min(INF, 1) = 1
            high_y = max(-1, 1) = 1
        
            (r,c) = (1, 0)
            low_x = min(0, 1) = 0
            high_x = max(0, 1) = 1
            low_y = min(1, 0) = 0
            high_y = max(1, 0) = 1

            (r,c) = (1, 2)
            low_x = min(0, 1) = 0
            high_x = max(1, 1) = 1
            low_y = min(0, 2) = 0
            high_y = max(1, 2) = 2
            
            With the final values, we know the topMost, bottomMost, leftMost and rightMost points
            We can use this to calculate the area
            Area = (high_x - low_x + 1) * (high_y - low_y + 1)
            Area = (1 - 0 + 1) * (2 - 0 + 1) = 2 * 3 = 6

            TC: O(mn) where mn is the size of the grid
            SC: O(1)
'''
from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        low_x = float("inf")
        high_x = -1
        low_y = float("inf")
        high_y = -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    low_x = min(low_x, i)
                    high_x = max(high_x, i)
                    low_y = min(low_y, j)
                    high_y = max(high_y, j)
        
        return (high_x - low_x + 1) * (high_y - low_y + 1)