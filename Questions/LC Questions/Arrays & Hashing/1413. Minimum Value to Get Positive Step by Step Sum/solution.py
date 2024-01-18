'''
    Explanation: Prefix Total
        [-3, 2, -3, 4, 2]
        sumNums = 0,  res = 0
        sumNums = -3, res = -3
        sumNums = -1, res = -3
        sumNums = -4, res = -4
        sumNums = 0, res = -4
        sumNums = 2, res = -4
        res = 1 - (-4) = 5
'''

from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        res, total = 0, 0
        
        for num in nums:
            total += num
            res = min(res, total)
            
        return 1 - res