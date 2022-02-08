from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        print(nums)
        
        for i in range(j, len(nums)):
            nums[i] = 0

        # One-line solution
        # nums[:] = [x for x in nums if x != 0] + [0]*nums.count(0)
        
        # TC - O(n)
        # SC - O(1)