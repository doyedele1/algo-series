'''
    Valid condition: len(a) >= len(b)

    - Can we check the maximum number of times it would take len(b) >= len(a)? THe answer is len(b) / len(a). If decimal, we round it up. i.e. 2.5 = 3
'''

from math import ceil

class Solution1:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        maxTimes = ceil(len(b)/len(a))
        tempA = a
        
        for times in range(1, maxTimes + 2):
            if b in tempA: return times
            tempA += a
        
        return -1

class Solution2:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        max_times = ceil(len(b) / len(a))
        tempA = a * max_times
        
        if b in tempA: return max_times
        if b in a + tempA: return max_times + 1
        return -1

'''
    Valid condition: len(a) >= len(b)
'''

class Solution3:
    def repeatedStringMatch(self, a: str, b: str) -> int: 
        def kmp(string, pattern):
            prefixsuffix = [0] * len(pattern)
            left = 0
            right = 1
            while right < len(pattern):
                if pattern[left] == pattern[right]:
                    prefixsuffix[right] = left + 1
                    left += 1
                    right += 1
                else:
                    if left == 0: 
                        prefixsuffix[right] = 0
                        right += 1
                    else:
                        left = prefixsuffix[left-1]

            p = 0
            s = 0
            while s < len(string) and p < len(pattern):
                if string[s] == pattern[p]:
                    s += 1
                    p += 1
                elif p == 0:
                    s += 1
                else:
                    p = prefixsuffix[p-1]

            if p == len(pattern): return True
            return False
            
        res = 1
        tempA = a
        if len(b) >= len(a):
            res = ceil(len(b) / len(a))
            a *= res
            
        if kmp(a, b): return res
        if kmp(a + tempA, b): return res + 1
        return -1