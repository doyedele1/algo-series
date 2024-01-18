'''
    Explanation II:
        Use a hashmap and map the value to its index
        [2,7,11,15], target = 9
        nums_map = {}
        
        First iteration, diff = 7, nums_map = {2:0}

        Second iteration, diff = 2, diff is in nums_map, then return the indices

        TC: O(n), SC: O(n)
'''

from typing import List

# TC: O(n-squared), SC: O(1)
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return[i,j]
    
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_map:
                return [nums_map[diff], i]
            nums_map[num] = i