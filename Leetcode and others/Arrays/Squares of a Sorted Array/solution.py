# Brute force solution: T(C) - O(nlogn), S(C) - O(1)
class Solution:
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums

# Optimal solution: T(C) - O(n), S(C) - O(n)
class Solution:
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        res_idx = len(nums) - 1
        result = [0 for num in nums]
        # print(result)

        while res_idx >= 0:
            if abs(nums[left]) >= abs(nums[right]):
                result[res_idx] = nums[left] * nums[left]
                left += 1
                res_idx -= 1
            else:
                result[res_idx] = nums[right] * nums[right]
                right -= 1
                res_idx -= 1
        return result
        
    # [-4,-1,0,3,10]