'''
    Explanation:
        nums = [1, 2, 3, 4, 5]

        We need two regions. Region 1 and region 2
        - Both regions are non-decreasing
        - The largest in region 2 is less than or equal to the smallest in region 1

        [5, 1, 2, 3, 4]
        [4, 5, 1, 2, 3]
        [3, 4, 5, 1, 2]. In this case, the qualified regions are [3, 4, 5] and [1, 2]
        [2, 3, 4, 5, 1]
        [1, 2, 3, 4, 5]

        With this understanding, we can find the first region (1st non-decreasing set of values) and the second region (2nd non-decreasing set of values)
        Region 1: a[i] >= a[i-1]
        Region 2: a[i] >= a[i-1] and a[i] <= a[0]

        Example: [3, 4, 4, 5, 1, 1, 2]

        Region 1 = [3, 4, 4, 5]
        Region 2 = [1, 1, 2]

        TC: O(n)
        SC: O(1)
'''

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        i = 1
        while i < n and nums[i] >= nums[i - 1]:
            i += 1

        if i == n:
            return True
        if nums[i] > nums[0]:
            return False
        if i == n - 1:
            return True
        
        i += 1
        while i < n and nums[i] <= nums[0] and nums[i] >= nums[i - 1]:
            i += 1
        return i == n