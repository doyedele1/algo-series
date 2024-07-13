'''
    Explanation:
        abccccdd
        a: 1
        b: 1
        c: 4
        d: 2

        a, count = {a:1}, res = 0
        ab, count = {a:1, b:1}, res = 0
        abc, count = {a:1, b:1, c:1}, res = 0
        abcc, count = {a:1, b:1, c:2}, res = 2
        abccc, count = {a:1, b:1, c:3}, res = 2
        abcccc, count = {a:1, b:1, c:4}, res = 4
        abccccd, count = {a:1, b:1, c:4, d:1}, res = 4
        abccccdd, count = {a:1, b:1, c:4, d:2}, res = 6

        There is at least one odd frequency of characters in the word, so just add 1 to res

        TC: O(n), SC: O(1)
'''

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