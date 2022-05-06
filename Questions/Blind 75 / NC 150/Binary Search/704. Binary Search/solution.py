'''
    - TC: O(log n)
    - SC: O(1)
'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1

        while i <= j:
            middle = i + ((j - i) // 2)
            if target == nums[middle]: return middle
            elif target < nums[middle]: j = middle - 1
            else: i = middle + 1
        
        return -1