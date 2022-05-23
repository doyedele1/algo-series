'''
    Explanation I: (Top, right, bottom and left) boundaries update
        Initialize the four boundaries and an output array
        Traverse the elements in spiral order and add each element to the output array
            left --> right
            up --> down
            Before moving from right to left, we need to ensure we are not on a row already visited
            Before moving from down to up, we need to ensure we are not on a column already visited
            Update the boundaries as expected
        Return result
        
        TC: O(m * n), where m = number of rows and n = number of columns
        SC: O(1)
        
    Explanation II: Know visited elements - we turn to the next direction when we run into a visited cell
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
        m, n = len(matrix), len(matrix[0])
        up = left = 0
        down, right = m - 1, n - 1
        res = []
        
        while len(res) < m * n:
            # left --> right
            for col in range(left, right + 1):
                res.append(matrix[up][col])
            
            # up --> down
            for row in range(up + 1, down + 1):
                res.append(matrix[row][right])
            
            # To ensure we are not on a row we've visited or we are now on a different row
            if up != down:
                # right --> left
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[down][col])
            
            # To ensure we are not on a column we've visited or we are now on a different column
            if left != right:
                # down --> up
                for row in range(down - 1, up, -1):
                    res.append(matrix[row][left])
            
            # Update boundaries
            left += 1
            right -= 1
            up += 1
            down -= 1
        
        return res

class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # The four possible directions - right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        row = col = 0
        visited = 101
        currentDirection = changeDirection = 0
        res = [matrix[0][0]]
        matrix[0][0] = visited
        
        while changeDirection < 2:
            while True:
                nextRow = row + directions[currentDirection][0]
                nextCol = col + directions[currentDirection][1]
                
                # Edge case - if the next step is out of bounds
                if not (0 <= nextRow < m and 0 <= nextCol < n): break
                
                # If the next step is on a visited cell
                if matrix[nextRow][nextCol] == visited: break
                
                # Reset changeDirection to 0
                changeDirection = 0
                row, col = nextRow, nextCol
                res.append(matrix[row][col])
                matrix[row][col] = visited
            
            # Change direction
            currentDirection = (currentDirection + 1) % 4
            
            # Increment changeDirection
            changeDirection += 1
        
        return res