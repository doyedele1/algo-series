'''
    Explanation:
        For k consecutive zeros, number of subarrays = k * (k + 1) / 2
            If k = 1, subarrays = (1 * 2) / 2 = 1
            If k = 2, subarrays = (2 * 3) / 2 = 3
            If k = 3, subarrays = (3 * 4) / 2 = 6

        Or we can do this,
            If k = 1, subarrays = previous + number of zeros = 0 + 1 = 1
            If k = 2, subarrays = previous + number of zeros = 1 + 2 = 3
            If k = 3, subarrays = previous + number of zeros = 3 + 3 = 6

        TC: O(n)
        SC: O(1)
'''
from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        consecutive_zeros = 0

        for num in nums:
            if num == 0:
                consecutive_zeros += 1
                res += consecutive_zeros
            else:
                consecutive_zeros = 0
        return res