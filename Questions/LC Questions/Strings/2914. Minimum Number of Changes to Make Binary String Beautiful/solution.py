'''
    Explanation:
        10011100
        
        Partition to the smallest even substrings
        10
        01
        11
        00

        Check these four substrings and increment res if they are not all the same
        Res = 2

        TC: O(n)
        SC: O(1)
'''

class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(0, n, 2):
            if s[i] != s[i + 1]:
                res += 1
        return res