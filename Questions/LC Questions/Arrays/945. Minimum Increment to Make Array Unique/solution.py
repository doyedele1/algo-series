'''
    Explanation I: Sorting
        [3,2,1,2,1,7]
        Sort: [1,1,2,2,3,7]
        No first iteration as we are starting from index 1
        Second iteration: res = 1, nums[1] = 2
        Third iteration: res = 2, nums[2] = 3
        Fourth iteration: res = 4, nums[3] = 4
        Fifth iteration: res = 6, nums[4] = 5

        TC: O(nlogn), SC: O(n)

    Explanation II: Counting Sort
        num     count
        1       2
        2       2
        3       1
        7       1

        If count is greater than 1, find the extra
        Get the next count by incrementing extra to the count

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