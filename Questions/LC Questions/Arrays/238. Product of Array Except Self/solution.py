'''
    Explanation I:
        [1, 2, 3, 4]
        - We could use left and right arrays
            - left rep the product of elem to the left and right represents the product of elem to the right
            - left = [], right = []
            - After all iterations: left = [1, 1, 2, 6]
            - After all iterations: right = [24, 12, 4, 1]
            - res = left[i] * right[i] = [24, 12, 8, 6]
        
        - TC: O(n)
        - SC: O(n), space occupied by the left and right arrays
        
    Explanation III:
        - We could do the left and right arrays operation inside the output array
        - [1, 2, 3, 4]
        - At each iteration,
            - left = [1, 1, 2, 6] which is res after the left operation
            - right = 24, 12, 4, 1 gotten from the input array
            - res = [1, 1, 2, 6] and res after the right operation = [1 * 24, 1 * 12, 2 * 4, 6 * 1] = [24, 12, 8, 6]
        
        - TC: O(n)
        - SC: O(1) since the res doesn't count as extra space
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

class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4, 5]
        # [120, 60, 40, 30, 24]
        # prefixProduct = [1, 2, 6, 24, 120]
        # suffixProduct = [120, 120, 60, 20, 5]
        lenNums = len(nums)
        prefixProduct = [0 for i in range(lenNums)]
        suffixProduct = [0 for i in range(lenNums)]
        result = [0 for i in range(lenNums)]

        for ind, num in enumerate(nums):
            if ind == 0:
                prefixProduct[ind] = num
            else:
                prefixProduct[ind] = prefixProduct[ind - 1] * num
        for ind in range(lenNums - 1, -1, -1):
            if ind == lenNums - 1:
                suffixProduct[ind] = nums[ind]
            else:
                suffixProduct[ind] = nums[ind] * suffixProduct[ind + 1]
        for ind, num in enumerate(nums):
            left = prefixProduct[ind - 1] if ind > 0 else 1
            right = suffixProduct[ind + 1] if ind < lenNums - 1 else 1
            result[ind] = left * right

        return result
    
class Solution3:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        left = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res