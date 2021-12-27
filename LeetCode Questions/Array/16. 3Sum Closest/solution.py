from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
            [-1,2,1,-4], 1
            diff = 6
            
            TC - O(n-squared)
            SC - O(log n) or O(n) for the sorting algorithm
        '''
        
        nums.sort()
        left = 0
        right = len(nums) - 1
        diff = float("inf")
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if abs(target - sum) < abs(diff):
                    res_i = i
                    res_left = left
                    res_right = right
                    diff = target - sum
                
                if sum < target: left += 1
                else: right -= 1
        
        return target - diff