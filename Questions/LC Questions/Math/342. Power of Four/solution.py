'''
    Explanation II:
        For a number to be a power of 4,
            1. It must be greater than 0
            2. It must be a power of 2
                4, 16, 64 etc. But 2, 8, 32 are powers of 2, but not powers of 4. So we need another condition
            3. The number minus 1 must be divisible by3.
                4^0 - 1 = 0
                4^1 - 1 = 3
                4^2 - 1 = 15
                4^3 - 1 = 63

        TC: O(1), SC: O(1)
'''

# TLE in LC
# TC: O(log n), SC: O(1)
class Solution1:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
            
        while n % 4 == 0:
            n // 4
        return n == 1
    
class Solution2:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0