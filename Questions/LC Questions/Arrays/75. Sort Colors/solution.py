'''
    Explanation:
        Brute force solution that came to mind - Bucket sort
        - Count the occurences of 0, 1 and 2
        - Then overwrite the nums array with the counts starting from 0
        This is a two-pass algorithm

        Dutch National Flag Algorithm
        - Use three points (low, mid, high) to partition the array

        TC: O(n), SC: O(1)
'''

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        low, mid = 0, 0
        high = n - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1