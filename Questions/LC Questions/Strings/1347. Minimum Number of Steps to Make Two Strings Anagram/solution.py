'''
    Explanation:
        - "bab", "aba"
            sFreq = {b:2, a:1}
            tFreq = {a:2, b:1}
            - Checking sFreq.items() which is [('b', 2), ('a', 1)],
                First iteration - b:
                    Is b in tFreq and count of b in sFreq is greater than the count of b in tFreq? Yes, then add the difference to res
                    Else if b is not in tFreq, add count of b in sFreq to res

                    count = 2 - 1 = 1
                    res = 1

                Second iteration - a:
                    a is in tFreq but the count of a in sFreq is less than the count of a in tFreq
                    We don't run the loop since the conditions fail, hence res is still 1
            
        TC: O(n)
        SC: O(m+n)
'''

from collections import defaultdict

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sFreq, tFreq = defaultdict(int), defaultdict(int)
        
        res = 0
        for char in s:
            sFreq[char] += 1
        for char in t:
            tFreq[char] += 1

        for char, count in sFreq.items():
            if char not in tFreq:
                res += count
            elif char in tFreq and count > tFreq[char]:
                res += (count - tFreq[char])

        return res