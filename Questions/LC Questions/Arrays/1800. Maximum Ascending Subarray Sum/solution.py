from typing import List

# TC: O(n), SC: O(1)
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)

        total = nums[0]
        ascending = nums[0]

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                total += nums[i]
            else:
                ascending = max(ascending, total)
                total = nums[i]
        return max(total, ascending)