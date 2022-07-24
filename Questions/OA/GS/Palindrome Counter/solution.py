class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindromesAroundMiddle(s, low, high):
            res = 0
            
            while low >= 0 and high < len(s):
                if s[low] != s[high]: break
                    
                low -= 1
                high += 1
                res += 1
            return res
        
        res = 0
        
        for i in range(len(s)):
            res += palindromesAroundMiddle(s, i, i)
            
            res += palindromesAroundMiddle(s, i, i + 1)
            
        return res