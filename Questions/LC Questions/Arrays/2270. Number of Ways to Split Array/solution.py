from typing import List

class Solution:
    def ways_to_split_array(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        count = 0
        prefix_sum = 0
        for i in range(n - 1):
            prefix_sum += nums[i]

            if prefix_sum >= total - prefix_sum:
                count += 1

        return count