'''
    Explanation: Dynamic Programming
        rows - n which is the length of the digits we can dial
        columns - 0 to 9 possible digits
        
        dp[2][0] = dp[1][4] + dp[1][6], since we can perform n-1 jumps
        Generally, dp[n][1] = dp[n-1][6] + dp[n-1][8]
        
        For n = 2, we can dial 04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94
        
        The DP table:
            0   1   2   3   4   5   6   7   8   9
        0   0   0   0   0   0   0   0   0   0   0
        1   1   1   1   1   1   1   1   1   1   1
        2   2   2   2   2   3   0   3   2   2   2
        .
        .
        .
        n
        
        We don't need a 2D array. A 1D array will do the job. dp[i] = number of steps, i itself will be the possible digits 0-9.
'''

class Solution:
    MODULO = 10**9 + 7
    
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        
        while n >= 2:
            temp = dp.copy()
            
            dp[0] = temp[4] + temp[6]
            dp[1] = temp[6] + temp[8]
            dp[2] = temp[7] + temp[9]
            dp[3] = temp[4] + temp[8]
            dp[4] = temp[0] + temp[3] + temp[9]
            dp[5] = 0
            dp[6] = temp[0] + temp[1] + temp[7]
            dp[7] = temp[2] + temp[6]
            dp[8] = temp[1] + temp[3]
            dp[9] = temp[2] + temp[4]
            n -= 1
            
        return sum(dp) % self.MODULO