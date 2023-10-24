''' 
    TC: O(n)
    SC: O(n)
'''
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        arrNums = [0] * (max(nums) + 1)

        for num in nums:
            arrNums[num] += num

        e1, e2 = 0, 0
        for num in arrNums:
            currEarn = max(e2, num + e1)
            e1 = e2
            e2 = currEarn
        return e2