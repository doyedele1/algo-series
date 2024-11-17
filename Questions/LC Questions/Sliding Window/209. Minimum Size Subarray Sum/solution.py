'''
    Explanation: Sliding Window
        [1, 3, 2, 2, 3], target = 7
         l
         r

         - Since we have positive integers, we know that the sum will keep increasing

        TC: O(n)
        SC: O(1)
'''

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, current_sum = 0, 0
        res = float("inf") # could also be len(nums) + 1 or even -1

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                res = min(res, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return 0 if res == float("inf") else res