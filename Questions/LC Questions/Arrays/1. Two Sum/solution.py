'''
    Explanation:
        Use a hashmap and map the value to its index
        
        [2,7,11,15], target = 9
        seen = {}
        
        First iteration:
            diff = 7, seen = {2:0}
        Second iteration:
            diff = 2, diff is in seen, then return the indices

        TC: O(n), SC: O(n)
'''

from typing import List
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, val in enumerate(nums):
            diff = target - val

            if diff in seen:
                return [seen[diff], i]
            else:
                seen[val] = i

        return []