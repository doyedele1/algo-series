'''
    Explanation:
        [6, 4, 2, 7, 1]
        6 = 110
        4 = 100
        2 = 010
        7 = 111
        1 = 001

        Preserving 1st bit = (7,1)
        Preserving 2nd bit = (6,2,7)
        Preserving 3rd bit = (6,4,7)
        Preserving 4th bit = ()
        
        if (value & (1<<i) > 0) = to check if a certain bit is set

        Why are we looping through 32 bits, because the maximum of candidates[i] = 10 pow 7
        log2(10 pow 7) is 24, so we go with 32 bits instead of 16 bits

        TC: O(32n) = O(n)
        SC: O(1)
'''

from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        n = len(candidates)

        maxFreq = 0
        for i in range(32):
            freq = 0
            for value in candidates:
                if (value & (1<<i) != 0):
                    freq += 1
            maxFreq = max(maxFreq, freq)
        
        return maxFreq