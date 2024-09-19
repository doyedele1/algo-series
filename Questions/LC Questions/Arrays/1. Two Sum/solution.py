'''
    Explanation:
        - Use a hashmap and map the value to its index
        [2,7,11,15], target = 9
        nums_map = {}
        
        - First iteration, diff = 7, nums_map = {2:0}
        - Second iteration, diff = 2, diff is in nums_map, then return the indices

        TC: O(n), SC: O(n)
'''

from typing import List
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}

        for idx, val in enumerate(nums):
            diff = target - val

            if diff in diffMap:
                return [diffMap[diff], idx]
            else:
                diffMap[val] = idx
        # return an empty list if no solution is found
        return []