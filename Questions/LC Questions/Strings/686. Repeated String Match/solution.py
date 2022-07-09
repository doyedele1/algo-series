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
        def kmp(a, b):
                for i in range(len(a) - len(b) + 1):
                    for j in range(len(b)):
                        if a[i+j] != b[j]: break
                    if j == len(b): return True
                return False
        
        res = 1
        tempA = a
        
        while len(a) < len(b):
            a += tempA
            res += 1
            
        if kmp(a, b): return res
        if kmp(a + tempA, b): return res + 1
        return -1
        
# print(Solution.kmp("abcdabcdabcd","cdabcdab"))