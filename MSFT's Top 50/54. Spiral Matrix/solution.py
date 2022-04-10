'''
    Explanation I: (Top, right, bottom and left) boundaries update
        - Initialize the four boundaries and an output array
        - Traverse the items in spiral order and add each item to the output array
            - left --> right
            - up --> down
            - before moving from right to left, we need to ensure we are not on a row already visited
            - before moving from down to up, we need to ensure we are not on a column already visited
            - Update the boundaries as expected
        - Return result
        
        - TC: O(m*n). where m = number of rows and n = number of columns
        - SC: O(1)
'''


from typing import List

class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        up, left = 0, 0
        down, right = m - 1, n - 1
        res = []
        
        while len(res) < m * n:
            # left --> right
            for col in range(left, right + 1):
                res.append(matrix[up][col])
            
            # up --> down
            for row in range(up + 1, down + 1):
                res.append(matrix[row][right])
            
            # to ensure we are not on a row we've visited or we are now on a different row
            if up != down:
                # right --> left
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[down][col])
            
            # to ensure we are not on a column we've visited or we are now on a different column
            if left != right:
                # down --> up
                for row in range(down - 1, up, -1):
                    res.append(matrix[row][left])
            
            # update boundaries
            left += 1
            right -= 1
            up += 1
            down -= 1
        
        return res