class Solution:
    def search(self, nums, target):
        i = 0
        j = len(nums) - 1

        while(i <= j):
            middle = (i + j) // 2
            if(nums[middle] == target):
                return middle
            elif(nums[middle] < target):
                i = middle + 1
            else:
                j = middle - 1
        return -1