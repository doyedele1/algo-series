class Solution:
    def removeDuplicates(self, nums):
        # i = 0
        
        # if(len(nums) == 0):
        #     return 0
    
        # for j in range(1, len(nums)):
        #     if(nums[i] != nums[j]):
        #         i+=1
        #         nums[i] = nums[j]
        # return i + 1

        index = 0
        
        for i in range(0, (len(nums) - 1)):
            if(nums[i] != nums[i+1]):
                index += 1
                nums[index] = nums[i+1]
        return index + 1
        