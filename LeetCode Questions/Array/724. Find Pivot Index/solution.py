'''
    Explanation: Prefix sum
        - Compute the sum of numbers
        - At index i, we can get the rightSum if we know the leftSum. rightSum = sum - leftSum - num
        - leftSum = leftSum + num
        
        - TC: O(n) where n is the length of nums
        - SC: O(1)
'''

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        numsSum = sum(nums)
        
        for index, num in enumerate(nums):
            rightSum = numsSum - leftSum - num
            if leftSum == rightSum: return index
            leftSum += num
        return -1