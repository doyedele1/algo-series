from typing import List

# TC: O(n), SC: O(n)
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        onlyPositiveNums = set()

        for num in nums:
            if num > 0:
                onlyPositiveNums.add(num)

        if len(onlyPositiveNums) == 0:
            return max(nums)
        else:
            return sum(onlyPositiveNums)