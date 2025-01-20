'''
    Explanation:
        Create a dictionary of num as the key and (row, col) as the value
        Iterate through arr and paint the row and col by keeping track of the row_painted and col_painted in two arrays
        
        Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
        
        lookup = {
            3: (0,0),
            2: (0,1),
            5: (0,2),
            1: (1,0),
            4: (1,1),
            6: (1,2),
            8: (2,0),
            7: (2,1),
            9: (2,2)
        }

        row_painted = [0,0,0], col_painted = [0,0,0]
        Iterating through arr, [2,8,7,4,1,3,5,6,9]
        For num 2, row_painted = [1,0,0], col_painted = [0,1,0]
        For num 8, row_painted = [1,0,1], col_painted = [1,1,0]
        For num 7, row_painted = [1,0,2], col_painted = [1,2,0]
        For num 4, row_painted = [1,1,2], col_painted = [1,3,0]

        Since we have a 3 in col_painted which is the same as the length of the row, then we return the index of num 4 in arr

        TC: O(mn)
        SC: O(mn)
'''
from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        lookup = {}
        for i in range(m):
            for j in range(n):
                lookup[mat[i][j]] = (i, j)

        row_painted = [0] * m
        col_painted = [0] * n

        for i, num in enumerate(arr):
            x, y = lookup[num]
            row_painted[x] += 1
            col_painted[y] += 1
            if row_painted[x] == n or col_painted[y] == m:
                return i
        return -1