'''
    Explanation:
        Observations:
            1. If k is equal to the length of s, then we can return True
            2. If k is greater than the length of s, it is impossible to contstruct k palindrome strings, so return False
            3. If k is greater than or equal to the count of odd frequencies of characters in s, then return True, else return False

        s = abac
        a: 2, b: 1, c: 1

        If k = 1, return False, because it's not possible to form 1 palindrome string since the count of odd frequencies is 2
        If k = 2, we can split: (1 char + 3 chars or 2 chars + 2 chars or 3 chars + 1 char), return True because it is possible to form 2 palindrome strings -> b and aca
        If k = 3, we can split: (1 + 1 + 2 or 1 + 2 + 1 or 2 + 1 + 1), return True because it is possible to form 3 palindrome strings -> aa, b and c
        If k = 4, we can split: (1 + 1 + 1), return True because it is possible to form 4 palindrome strings -> a, a, b and c
        If k = 5, that's more than the length of s, so return False

        TC: O(n), SC: O(1)
'''
from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k == len(s):
            return True
        if k > len(s):
            return False
        
        s_count = Counter(s)
        odd_freq = 0
        for count in s_count.values():
            if count % 2 == 1:
                odd_freq += 1
        
        return k >= odd_freq