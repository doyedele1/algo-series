# Recursive solution. T(C) - O(m + n), S(C) - O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(t) == 0: return False
        
        if s[0] == t[0]: return self.isSubsequence(s[1:], t[1:])
        return self.isSubsequence(s, t[1:])


# Iterative solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s) == 0): return True
        
        i = 0
        for char in range(len(t)):
            if t[char] == s[i]: i+=1
            if i == len(s): return True
        return i == len(s)