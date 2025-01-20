'''
    TC: O(mn logmn)
    SC: O(mn) for the set and minheap
'''
from typing import List
import heapq

class Solution:
    def isInBounds(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])

        # We need a minimum of 3x3 matrix to trap water
        if m < 3 or n < 3:
            return 0

        # Let's push all boundary elements to a minheap and set
        min_heap = []
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        level = 0
        trapped_water = 0

        # RLDU
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while min_heap:
            height, x, y = heapq.heappop(min_heap)
            level = max(level, height)

            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if self.isInBounds(new_x, new_y, m, n) and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    heapq.heappush(min_heap, (heightMap[new_x][new_y], new_x, new_y))
                    if heightMap[new_x][new_y] < level:
                        trapped_water += (level - heightMap[new_x][new_y])
        
        return trapped_water