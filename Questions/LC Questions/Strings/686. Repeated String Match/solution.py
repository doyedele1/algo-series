from math import ceil

class Solution:
    # def repeatedStringMatch(self, a: str, b: str) -> int:
        
    #     maxTimes = ceil(len(b)/len(a))
    #     tempA = a
        
    #     for times in range(1, maxTimes + 2):
    #         if b in tempA: return times
    #         tempA += a
        
    #     return -1

    def kmp(a, b):
            for i in range(len(a) - len(b) + 1):
                for j in range(len(b)):
                    if a[i+j] != b[j]: break
                if j == len(b): return True
            return False
        
print(Solution.kmp("abcdabcdabcd","cdabcdab"))