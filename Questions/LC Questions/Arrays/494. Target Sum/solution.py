'''
    Explanation:
        - We use a cache that contains (index, sum) at every node of the tree?
                                            (0, 0)
                            (1, 1)                            (1, -1)
                    (2, 2)          (2, 0)
                               (3, 1)
                          (4, 2)
                      (5, 3)
        - (index, sum). Maximum value for index is len(nums) = n, Possible range for sum of values in nums is -5 to 5 = t. 
        - TC: O(n*t)
        - SC: O(n*t)
'''

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def helper(index, sum):
            # base case
            if index == len(nums): return 1 if sum == target else 0
            
            # base case - if the pair (index, sum) already exists
            if (index, sum) in cache: return cache[(index, sum)]
            
            add = sum + nums[index]
            subtract = sum - nums[index]
            cache[(index, sum)] = (helper(index + 1, add) + helper(index + 1, subtract))
            
            return cache[(index, sum)]
        
        return helper(0, 0)