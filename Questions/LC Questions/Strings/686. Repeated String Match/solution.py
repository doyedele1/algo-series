from math import ceil

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        maxTimes = ceil(len(b)/len(a))
        tempA = a
        
        for times in range(1, maxTimes + 2):
            if b in tempA: return times
            tempA += a
        
        return -1