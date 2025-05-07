from typing import List

# TC: O(n), SC: O(n)
class Solution1:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            res[i] = nums[nums[i]]
        return res
    
# Encoding and Decoding values approach
# TC: O(n), SC: O(1)
# stored_value = original_val +  new_value_for_this_slot * CONSTANT
    
class Solution2:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            new_value = nums[nums[i]] % n
            nums[i] = nums[i] + new_value * n

        for i in range(n):
            nums[i] = nums[i] // n
        
        return nums