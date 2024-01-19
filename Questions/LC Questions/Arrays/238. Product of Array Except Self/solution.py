'''
    Explanation I:
        [1, 2, 3, 4]
        - We could use left and right arrays
        - left represents the product of numbers to the left and right represents the product of numbers to the right
        left = [], right = []
        - After first loop, left = [1, 1, 2, 6]
        - After second loop, right = [24, 12, 4, 1]
        - res = left[i] * right[i] = [24, 12, 8, 6]
        
        TC: O(n)
        SC: O(n), space occupied by the left and right arrays
        
    Explanation II:
        - We could do the left and right arrays operation inside the res array
        [1, 2, 3, 4]
        - At first loop,
            - res = left = [1, 1, 2, 6]
        - At second loop,
            First iteration,
                res = [1, 1, 2, 6], right = 1 * 4 = 4
            Second iteration,
                res = [1, 1, 8, 6], right = 4 * 3 = 12
            Third iteration,
                res = [1, 12, 8, 6], right = 12 * 2 = 24
            Fourth iteration,
                res = [24, 12, 8, 6], right = 24 * 1 = 24
        
        TC: O(n)
        SC: O(1)
'''

from typing import List

class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, res = [1] * len(nums), [1] * len(nums), [1] * len(nums)
        
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        return res
 
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res
    
# TC: O(n), SC: O(n)
class Solution3:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4, 5]
        # prefixProduct = [1, 2, 6, 24, 120]
        # suffixProduct = [120, 120, 60, 20, 5]
        # res = [1 * 120, 1 * 60, 2 * 20, 6 * 5, 24 * 1]
        # res = [120, 60, 40, 30, 24]

        prefixProduct = [0] * len(nums)
        suffixProduct = [0] * len(nums)
        result = [0] * len(nums)

        for i, num in enumerate(nums):
            if i == 0:
                prefixProduct[i] = num
            else:
                prefixProduct[i] = prefixProduct[i - 1] * num

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffixProduct[i] = nums[i]
            else:
                suffixProduct[i] = suffixProduct[i + 1] * nums[i]

        for i, num in enumerate(nums):
            left = prefixProduct[i - 1] if i > 0 else 1
            right = suffixProduct[i + 1] if i < len(nums) - 1 else 1
            result[i] = left * right

        return result