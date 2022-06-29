from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def helper(index, sum):
            if index == len(nums):
                return 1 if sum == target else 0
            
            if (index, sum) in cache: return cache[(index, sum)]
            
            cache[(index, sum)] = (helper(index + 1, sum + nums[index]) + helper(index + 1, sum - nums[index]))
            
            return cache[(index, sum)]
        
        return helper(0, 0)