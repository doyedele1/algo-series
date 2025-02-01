from typing import List

# TC: O(n), SC: O(1)
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(1, n):
            if (nums[i] & 1) == (nums[i - 1] & 1):
                # or do this (nums[i] % 2) == (nums[i - 1] % 2)
                return False
        return True