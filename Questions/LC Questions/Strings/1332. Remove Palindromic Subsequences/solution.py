# TC: O(n), SC: O(1)
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def validPalindrome(s):
            left = 0
            right = len(s) - 1
            
            while left < right:
                if s[left] != s[right]: return False
                left += 1
                right -= 1
            return True
        
        if len(s) == 0: return 0
        if validPalindrome(s): return 1
        return 2