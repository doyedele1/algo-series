'''
    Explanation: Dynamic Programming
        rows - number of steps n
        columns - 0 to 9 possible digits
        
        dp[2][0] = dp[1][4] + dp[1][6]
        Generally, dp[n][1] = dp[n-1][6] + dp[n-1][8]
        
        The DP table:
            0   1   2   3   4   5   6   7   8   9
        0   0   0   0   0   0   0   0   0   0   0
        1   1   1   1   1   1   1   1   1   1   1
        2   2   2   2   2   
        3
        .
        .
        .
        n
        

'''

class Solution:
    def knightDialer(self, n: int) -> int:
        MODULO = 10**9 + 7
        dp = [1] * 10
        
        while n > 1:
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
        return sum(dp) % MODULO