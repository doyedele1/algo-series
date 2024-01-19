'''
    Explanation I:
        Sort, then check if the two sorted strings are equal
        TC: O(n logn), SC: O(1)
    
    Explanation II - IV:
        TC: O(s + t), SC: O(1)
'''

from collections import Counter

class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s, dict_t = {}, {}
        
        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0) # If s[i] doesn't exist, we return value to be 0
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0) # If t[i] doesn't exist, we return value to be 0
        return dict_s == dict_t

class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict = {}

        for i in range(len(s)):
            dict[s[i]] = dict.get(s[i], 0) + 1
            dict[t[i]] = dict.get(t[i], 0) - 1

        for key, freq in dict.items():
            if freq != 0:
                return False
        return True