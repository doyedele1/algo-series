'''
    Explanation: Two-pointer approach
        index i is to iterate through the array
        index j is the swap index which represents the position to place the next non-zero number
        
        Dry run:
        [0, 1, 0, 3, 12]

        First Iteration --> [0, 1, 0, 3, 12]
                             i
                             j
        Second Iteration -->[1, 0, 0, 3, 12]
                                i
                             j
        Third Iteration --> [1, 0, 0, 3, 12]
                                   i
                                j
        Fourth Iteration --> [1, 3, 0, 0, 12]
                                       i
                                 j
        Fifth Iteration --> [1, 3, 12, 0, 0]
                                          i
                                    j

        TC - O(n)
        SC - O(1)
'''

from typing import List

class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        j = 0

        for i in range(n):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            
# Variant question asked by Meta- Move the zeroes to the beginning instead of the end
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        j = n - 1

        for i in range(n - 1, -1, -1):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j -= 1