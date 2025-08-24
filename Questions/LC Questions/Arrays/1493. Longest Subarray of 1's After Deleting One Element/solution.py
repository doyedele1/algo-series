'''
    Explanation: Sliding Window
        nums = [0,1,1,1,0,1,1,0,1]

        First iteration:
            left = 0, right = 0, zero_count = 1, res = 0
        
        Second iteration:
            left = 0, right = 1, zero_count = 1, res = 1

        Third iteration:
            left = 0, right = 2, zero_count = 1, res = 2

        Fourth iteration:
            left = 0, right = 3, zero_count = 1, res = 3
        
        Fifth iteration:
            left = 0, right = 4, zero_count = 2
            Since zero_count > 1, shrink the left pointer.
            zero_count = 1, left = 1, res = 3

        Sixth iteration:
            left = 1, right = 5, zero_count = 1, res = 4

        Seventh iteration:
            left = 1, right = 6, zero_count = 1, res = 5

        Eigth iteration:
            left = 1, right = 7, zero_count = 2
            Since zero_count > 1, shrink the left pointer.
            zero_count = 1, left = 5, res = max(5, 2) = 5

        Nineth iteration:
            left = 5, right = 8, zero_count = 1, res = max(3, 5) = 5

        TC: O(n), SC: O(1)
'''
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        zero_count = 0
        res = 0

        for right in range(n):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            res = max(res, right - left)
        return res