'''
    Explanation:
        We shouldn't give a O(mn) or O(m + n) space solution

        To do it in-place, we can do the following:
        - Check if 0th row and 0th col has any zero using two booleans
        - Mark 0th row and 0th col if there's a zero by iterating from (1,1) to (m-1, n-1). Because the row 0 and col 0 have been taken care from the above step
        - Iterate on 0th row and mark the respective cols
        - Iterate on 0th col and mark the respective rows
        - Mark 0th row and 0th col if required using the booleans

        TC: O(mn)
        SC: O(1)
'''

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        # check if the 0th row has any zero
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        # check if the 0th col has any zero
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        
        # mark 0th row and 0th col
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # zero out marked rows and cols
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # mark 0th row if needed
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # mark 0th column if needed
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0