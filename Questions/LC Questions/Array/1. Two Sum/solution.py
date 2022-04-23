from typing import List

# Brute force solution - TC - O(n-squared), SC - O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return[i,j]



# Most Optimal solution - TC - O(n), SC - O(n)
'''
    Explanation:
    - Use a hashmap and map the value to its index
        # [2,7,11,15], target = 9
        # numsMap = {}
        # - First iteration
        # diff = 7
        # numsMap = {2: 0}

        # - Second iteration
        # diff = 2
        # diff is in numsMap, then return the indices
'''
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff in numsMap:
                return [numsMap[diff], index]
            numsMap[num] = index



# Another optimal solution - TC - O(n-squared worst case), SC - O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            diff = target - num
            if diff in nums and nums.index(diff) != index:
                return [index, nums.index(diff)]