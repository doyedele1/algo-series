# Brute force solution - TC - O(n-squared), SC - O(1)
class Solution:
    def twoSum(self, nums, target):
        i = 0
        j = len(nums) - 1
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return[i,j]

# Optimal solution - TC - O(n), SC - O(n)
class Solution:
    def twoSum(self, nums, target):
        complement_dict = {}
        
        for i in range(len(nums)):
            match = target - nums[i]
            if(nums[i] in complement_dict):
                return [complement_dict[nums[i]], i]
            else:
                complement_dict[match] = i

# Explanation:
# [2,7,11,15], target = 9
# complement_dict = {}
# - First iteration
# match = 7

# complement_dict = {7: 0}
# - Second iteration
# match = 2
# nums[i] is in complement_dict, then return the indices