# TC: O(n * n^(1/x)). Inner loop runs n times, outer loop runs until i^x > n, hence i = n^(1/x)
# SC: O(n)
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            val = i ** x

            if val > n:
                break
            
            for j in range(n, val - 1, -1):
                dp[j] = (dp[j] + dp[j - val]) % MOD
        return dp[n]