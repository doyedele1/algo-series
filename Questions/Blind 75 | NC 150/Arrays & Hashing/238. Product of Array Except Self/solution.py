'''
    Explanation:
        - [1, 2, 3, 4]
        - We could use left and right arrays - left represents the product of elem to the left and right represents the product of elem to the right
            - left = [], right = []
            - After all iterations: left = [1, 1, 2, 6]
            - After all iterations: right = [24, 12, 4, 1]
            - res = left[i] * right[i] = [24, 12, 8, 6]
        - TC: O(n)
        - SC: O(n), space occupied by the left and right arrays
'''

from typing import List

class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, res = [1] * len(nums), [1] * len(nums), [1] * len(nums)
        
        left[0] = 1
        for i in range(1, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]
        
        right[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]
        
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        return res