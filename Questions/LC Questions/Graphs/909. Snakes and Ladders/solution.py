'''
    Explanation: Matrix Flattening
        Flatten the 2D array to a 1D array
        General case: when we have a normal 2D array (top-down order)
        index (r, c) = r * n + c
        
        We can conclude that, r = index / n and c = index % n

        Our case: bottom-up order
        top_r = (index - 1) / n
        r = n - top_r - 1
        c = (index - 1) % n
        If row is odd, (i.e. r % 2 == 1)
            c = n - c - 1

        Dry run: BFS (since the hop is 1 and it is the same for every hop/cost). If hop/cost is not the same, then you can use Dijkstra's
        
        16  15  14  13
        9   10  11  12
        8   6   7   5
        1   2   3   4

        There is a ladder from 8 to 14 and a snake from 12 to 2

        First iteration:
            level is 0

            For 1, we can go to 2, 3, 4, 5, 6, 7. Add those to the q
            q = [2, 3, 4, 5, 6, 7]

        Second iteration:
            level is now 1

            For 2, we can go to 3, 4, 5, 6, 7, 8 (but only 8 is not visited and 8 jumps to 14)
            q = [3, 4, 5, 6, 7, 14]

            For 3, we can go 4, 5, 6, 7, 8, 9
            q = [4, 5, 6, 7, 14, 9]

            For 4, we can go 5, 6, 7, 8, 9, 10
            q = [5, 6, 7, 14, 9, 10]

            For 5, we can go 6, 7, 8, 9, 10, 11
            q = [6, 7, 14, 9, 10, 11]

            For 6, we can go 7, 8, 9, 10, 11, 12 (but 12 goes to 2 which is already visited). So don't add 12 to the q
            q = [7, 14, 9, 10, 11]

            For 7, we can go 8, 9, 10, 11, 12, 13
            q = [14, 9, 10, 11, 13]
        
        Third iteration:
            level is now 2

            For 14, we can go to 15, 16
            q = [9, 10, 11, 13, 15, 16]

            For 9, we can go to 10, 11, 12, 13, 14, 15, 16
            q = [10, 11, 13, 15, 16]

            For 10, we can go to 11, 12, 13, 14, 15, 16
            q = [11, 13, 15, 16]

            For 11, we can go to 12, 13, 14, 15, 16
            q = [13, 15, 16]

            For 13, we can go to 13, 14, 15, 16
            q = [15, 16]
        
        Fourth iteration:
            level is now 3

            For 15, we can go to 16
            q = [16]

            For 16, this is our destination, so we can return level which is the minimum number of hops

        What could be the resulting path: 1 -> 6; 6 -> 8, 8 -> 14, 14 -> 16
        Going from 6 -> 8 and then 8 -> 14 is just one hop because of the ladder

        Note: There could be multiple resulting paths

        TC: O(n-squared)
        SC: O(n-squared)
'''
from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        destination = n * n

        q = deque([1])
        visited = [False] * (destination + 1)
        visited[1] = True

        level = 0

        while q:
            size = len(q)

            for _ in range(size):
                curr = q.popleft()

                if curr == destination:
                    return level

                for next_pos in range(curr + 1, min(curr + 6, destination) + 1):
                    dest = next_pos
                    # Calculate board position
                    row = (next_pos - 1) // n
                    col = (next_pos - 1) % n
                    if row % 2 == 1:  # Odd rows are right-to-left
                        col = n - 1 - col
                    
                    row = n - 1 - row  # Convert to board coordinates
                    
                    if board[row][col] != -1:
                        dest = board[row][col]
                    
                    if not visited[dest]:
                        visited[dest] = True
                        q.append(dest)
            
            level += 1
        
        return -1