'''
    Explanation:
        Property of a square:
            when at an index, length(row_path) = length(col_path) = length(diagonal_path). Then this makes it a square
        
        With this property, we can conclude the following:
        if we are on 1, then
        dp[i,j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        Example:
        1   0   1   1   1
        1   0   1   1   1
        1   1   1   1   1
        1   0   0   1   0

        Let's create m+1 x n+1 dp table: First rows and first columns are filled with 0 since they are out of bounds and they are used to take care of the out of bounds cases
        Then, we can fill the dp table using this: dp[i,j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        0   0   0   0   0   0
        0   1   0   1   1   1
        0   1   0   1   2   2
        0   1   1   1   2   3   
        0   1   0   0   1   0

        TC: O(mn), SC:O(mn)
'''
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        largest = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    largest = max(largest, dp[i][j])
        return largest * largest