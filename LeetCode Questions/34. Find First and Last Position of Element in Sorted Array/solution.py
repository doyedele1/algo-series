class Solution:
    def searchRange(self, nums, target):
        return [self.startingIndex(nums, target), self.endingIndex(nums, target)]
    
    def startingIndex(self, nums, target):
        idx = -1
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            # print(middle)
            if nums[middle] >= target:
                right = middle - 1  
            else:
                left = middle + 1
            if nums[middle] == target:
                idx = middle  
        return idx
        
    def endingIndex(self, nums, target):
        idx = -1
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            # print(middle)
            if nums[middle] <= target:
                left = middle + 1
            else:
                right = middle - 1      
            if nums[middle] == target:
                idx = middle
                
        return idx
    