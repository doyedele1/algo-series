'''
    Explanation: Sliding Window
        [2, 3, 1, 2, 4, 3], target = 7

        [2, 3, 1, 2], current_sum = 8 which is greater than 7
        Since the values in the array are positive, then we know that [2, 3, 1] wasn't going to give us a value greater than or equal to 7

        [2, 3, 1, 2, 4, 3]
         i  j
        current_sum = 5

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