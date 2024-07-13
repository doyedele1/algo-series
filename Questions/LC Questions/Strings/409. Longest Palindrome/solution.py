from collections import defaultdict

class Solution1:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        res = 0

        for char in s:
            count[char] += 1
            if count[char] % 2 == 0:
                res += 2
            
        for freq in count.values():
            if freq % 2:
                res += 1
                break
        return res
    
class Solution2:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        res = 0

        for char in s:
            if char in seen:
                seen.remove(char)
                res += 2
            else:
                seen.add(char)
        return res + 1 if seen else res