'''
    TC: O(mnk)
    SC: O(mnk)
'''

from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        visited = set()
        q = deque()
        q.append((0,0,k))
        steps = 0
        
        while q:
            for _ in range(len(q)):
                current = q.popleft()
                
                # If current is the destination, return steps
                if current[0] == m - 1 and current[1] == n - 1: return steps
                
                # Else, go to all valid directions
                for dir in directions:
                    i = current[0] + dir[0]
                    j = current[1] + dir[1]
                    obs = current[2]
                    
                    # Traverse through valid cells
                    if i >= 0 and i < m and j >= 0 and j < n:
                        
                        # If cell is empty, visit the cell and add in queue
                        if grid[i][j] == 0 and ((i, j, obs)) not in visited:
                            q.append((i,j,obs))
                            visited.add((i,j,obs))
                        elif grid[i][j] == 1 and obs > 0 and ((i,j,obs-1)) not in visited:
                            q.append((i,j,obs-1))
                            visited.add((i,j,obs-1))
            steps += 1

        return -1