from typing import List

# TC: O(n), SC: O(1)
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        minSeenSoFar = nums[0]

        for i in range(1, n):
            if nums[i] > minSeenSoFar:
                res = max(res, nums[i] - minSeenSoFar)
            else:
                minSeenSoFar = nums[i]
                
        return res