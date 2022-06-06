'''
    Explanation: Recursive Solution
                0 1 2 3 4 5 6 7
        nums = [1,3,5,2,4,8,2,2]
        If index is even, i.e. i % 4 is equal to 0, we find min
        If index is odd, i.e. i % 4 is not equal to 1, we find max
    

'''


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1: return nums[0]
        
        newNums = []
        for i in range(0, n, 2):
            if i % 4 == 0:
                newNums.append(min(nums[i], nums[i + 1]))
            else:
                newNums.append(max(nums[i], nums[i + 1]))
                
        return self.minMaxGame(newNums)