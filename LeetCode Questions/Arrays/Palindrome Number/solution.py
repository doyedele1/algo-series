class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_x = self.reverse(x)
        if x == rev_x: return True
        return False
        
    def reverse(self, x):
        prev = 0
        res = 0
        
        while x != 0:
            pop = x % 10
            x = x // 10
            
            res = res * 10 + pop
            if (res - pop) / 10 != prev: return 0
            prev = res
            
        return res