from typing import List

# TC: O(n), SC: O(1)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            res[i] = nums[nums[i]]
        return res