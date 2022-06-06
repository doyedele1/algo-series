'''
    Explanation: Recursive Solution
        - We loop through the nums array in steps of 2. i.e 0, 2, 4, 6
        - If index is a multiple of 4, i.e. i % 4 is equal to 0, we call the min method on nums[index] and nums[index + 1]
        - If index is not a multiple of 4, i.e. i % 4 is not equal to 1, we call the max method on nums[index] and nums[index + 1]
        
         0  1  2  3  4  5  6  7
        [1, 3, 5, 2, 4, 8, 2, 2]
        
        newNums = []
        First iteration: index 0 is a multiple of 4, call min, newNums = [1]
        Second iteration: index 2 is not a multiple of 4, call max, newNums = [1, 5]
        Third iteration: index 4 is a multiple of 4, call min, newNums = [1, 5, 4]
        Fourth iteration: index 6 is not a multiple of 4, call min, newNums = [1, 5, 4, 2]
        
        The recursive base case. Is len(newNums) == 1? No, continue the iteration
        First iteration: index 0 is a multiple of 4, call min, newNums = [1]
        Second iteration: index 2 is not a multiple of 4, call max, newNums = [1, 4]
        
        The recursive base case. Is len(newNums) == 1? No, continue the iteration
        First iteration: index 0 is a multiple of 4, call min, newNums = [1]
        
        The recursive base case. Is len(newNums) == 1? Yes, it is, then return newNums[0] = 1
        
        TC: O(log n)
        SC: O(log n)
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