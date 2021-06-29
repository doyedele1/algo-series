class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        
        for i in range(1,33):
            ans = ans << 1
            ans = ans | (n & 1)
            n = n >> 1
            
        return ans