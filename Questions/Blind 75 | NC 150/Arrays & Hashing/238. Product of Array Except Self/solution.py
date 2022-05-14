'''
    Explanation:
        - 
        
        - TC: O(n)
        - SC: O(1), the result array does not count as extra space

'''



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        L = 1
        for i in range(len(nums)):
            res[i] = L
            L *= nums[i]
            
        R = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= R
            R *= nums[i]
        
        return res