'''
    Explanation: Know visited elements - we turn to the next direction when we run into a visited cell
        * When we reach a visited cell, we turn and when we meet another visited cell immediately after changing direction, it means we reached the last element in the matrix
        
        Initialize a 2D array to represent the four possible directions
        Initialize row and col to be 0 since that's the initial position
        Initialize visited to 101 to mark visited cells
        Initialize currentDirection to 0 to signify that we are moving right at the beginning and changeDirection to 0
        
        Traverse in the currentDirection and reset changeDirection to 0 at every step
        Traverse to the next cell by updating row and col accordingly
        Append the element to the result and mark the cell visited
        
        Update the direction and changeDirection. If changeDirection > 1, then we've visited all of the elements
        
        TC: O(m * n), where m = number of rows and n = number of columns
        SC: O(1)
'''

from typing import List

class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initial direction: moving right
        currDirection = 0
        changeDirection = 0
        row = col = 0
        res = [matrix[0][0]]
        visited.add((0, 0))

        while changeDirection < 2:
            while True:
                # next place that we will move to
                nextRow = row + directions[currDirection][0]
                nextCol = col + directions[currDirection][1]

                # Break if next step is out of bounds
                if not (0 <= nextRow < rows and 0 <= nextCol < cols):
                    break
                
                # Break if next step is already visited
                if (nextRow, nextCol) in visited:
                    break

                # Since we didn't change direction, reset this to 0
                changeDirection = 0
                # Update our current position to the next step
                row, col = nextRow, nextCol
                res.append(matrix[row][col])
                visited.add((row, col))
            
            # Change our direction
            currDirection = (currDirection + 1) % 4
            changeDirection += 1
        
        return res

class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        row = col = 0
        VISITED = 101
        currentDirection = changeDirection = 0
        res = [matrix[0][0]]
        matrix[0][0] = VISITED
        
        while changeDirection < 2:
            while True:
                nextRow = row + directions[currentDirection][0]
                nextCol = col + directions[currentDirection][1]
                
                if not (0 <= nextRow < m and 0 <= nextCol < n): 
                    break
                
                if matrix[nextRow][nextCol] == VISITED: 
                    break
                
                changeDirection = 0
                row, col = nextRow, nextCol
                res.append(matrix[row][col])
                matrix[row][col] = VISITED
            
            currentDirection = (currentDirection + 1) % 4
            changeDirection += 1
        
        return res