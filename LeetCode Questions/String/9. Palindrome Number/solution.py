class Solution:
    def isPalindrome(self, x: int) -> bool:
        # s = str(x)
        # reversed_str = ""
        
        # for i in range(len(s) - 1, -1, -1):
        #     reversed_str += s[i]
        
        # return reversed_str == s 
        
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