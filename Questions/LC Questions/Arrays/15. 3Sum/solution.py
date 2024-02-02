'''
    Explanation:
        [-3, 3, 4, -3, 1, 2]

        TC: O(nlogn + n-squared) = O(n-squared)
        SC: O(1)
'''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            # since we want to skip positive integers
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i - 1] != nums[i]:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    threeSum = nums[i] + nums[l] + nums[r]
                    if threeSum > 0:
                        r -= 1
                    elif threeSum < 0:
                        l += 1
                    else:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return res
            
        