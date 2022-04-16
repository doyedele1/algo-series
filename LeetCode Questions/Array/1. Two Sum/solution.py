# Brute force solution - TC - O(n-squared), SC - O(1)
class Solution:
    def twoSum(self, nums, target):
        i = 0
        j = len(nums) - 1
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return[i,j]

# Another Optimal solution - TC - O(n), SC - O(n)
# Explanation:
    # [2,7,11,15], target = 9
    # complement = {}
    # - First iteration
    # match = 7
    # complement = {7: 0}

    # - Second iteration
    # match = 2
    # nums[i] is in complement, then return the indices
    
# class Solution:
#     def twoSum(self, nums, target):
#         complement = {}
        
#         for i in range(len(nums)):
#             match = target - nums[i]
#             if nums[i] in complement:
#                 return [complement[nums[i]], i]
#             else:
#                 complement[match] = i

# # Optimal solution - TC - O(n), SC - O(1)
# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(0,len(nums)):
#             diff = target - nums[i]
                
#             if diff in nums and nums.index(diff) != i:
#                 return [i,nums.index(diff)]