'''

    TC: O(mn logmn)
    SC: O(mn) for the set and minheap
'''
from typing import List
import heapq

class Solution:
    def isInBounds(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n

    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        min_heap = []
        heapq.heappush(min_heap, (0, 0, 0))

        visited = [[False for _ in range(n)] for _ in range(m)]

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while min_heap:
            cost, x, y = heapq.heappop(min_heap)

            if visited[x][y] == True:
                continue
            
            if x == m - 1 and y == n - 1:
                return cost
            
            visited[x][y] = True

            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if self.isInBounds(new_x, new_y, m, n) and not visited[new_x][new_y]:
                    if (i + 1) == grid[x][y]:
                        new_cost = cost
                    else:
                        new_cost = cost + 1
                    heapq.heappush(min_heap, (new_cost, new_x, new_y))
        return 0