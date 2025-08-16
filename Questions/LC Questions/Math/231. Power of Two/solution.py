class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        
        while n % 2 == 0:
            n /= 2
        return n == 1

class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0