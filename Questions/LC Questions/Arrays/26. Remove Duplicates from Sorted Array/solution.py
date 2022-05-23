class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0: return 0

        index = 0
        
        for i in range(0, len(nums) - 1):
            if nums[i] != nums[i + 1]:
                index += 1
                nums[index] = nums[i + 1]
        return index + 1