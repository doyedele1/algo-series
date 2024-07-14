'''
    Explanation II: Counting Sort

    TC: O(n + max(nums)), SC: O(n + max(nums))
'''

from collections import Counter
from typing import List

class Solution1:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        res = 0

        for i in range(1, N):
            if nums[i - 1] >= nums[i]:
                res += 1 + (nums[i - 1] - nums[i])
                nums[i] = nums[i - 1] + 1
        return res
    
class Solution2:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        N = len(nums)
        count = Counter(nums)
        res = 0

        for i in range(N + max(nums)):
            if count[i] > 1:
                extra = count[i] - 1
                count[i + 1] += extra
                res += extra
        return res