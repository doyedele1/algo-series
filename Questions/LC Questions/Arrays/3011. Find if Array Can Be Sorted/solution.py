'''
    Explanation I: Bubble Sort (based on adjacent comparison)
        * Only adjacent numbers can be swapped
        * Only when they have same count of set bits

        [4, 2, 13, 7]
        First, let's find the count of set bits. We can use the method below or use bin(nums[j]).count('1) == bin(nums[j+1]).count('1')
        If in correct order (sorted in ascending order), then continue
        Else, you should swap if they have the same count of set bits

        To avoid modifying the input directly, we can create a copy of the input array as values = nums.copy() and use values instead of nums

        Another example: [3, 4, 2]
                
        TC: O(n-squared log n)
        - findCountOfSetBits = O(log n)
        - the main solution = O(n-sqaured)
        SC: O(1)

    Explanation II: Sortable Segments
        [4, 2, 8, 13, 7, 14, 32, 16, 64, 30, 15]
        * Numbers with same count of set bits can be assumed to group together. 
        (4, 2, 8) has set bit of 1
        (13, 7, 14) has set bit of 3
        (32, 16, 64) has set bit of 1
        (30, 15) has set bit of 3

        * Swap is only possible in a group
        * For sorting in ascending order with adjacent swaps only,
        max(previous group) <= min(current adjacent group)
        In the groups of (4, 2, 8) and (13, 7, 14), it is not possible to sort these two groups because 8 is greater than 7
        But if we don't have 8, we can sort the two groups as (2, 4) and (7, 13, 14)

        With these observations, we can come up with an optimal solution
        [4, 2, 13, 7, 14]. We need these four variables prev_segment_max, curr_segment_max, curr_segment_min and set_bit_count
        First iteration: prev_segment_max = -infinity, curr_segment_max = 4, curr_segment_min = 4, set_bit_count = 1
        Second iteration: prev_segment_max = -infinity, curr_segment_max = 4, curr_segment_min = 2, set_bit_count = 1
        Anytime we move to a new group, we always check if prev_segment_max <= curr_segment_min, else array will not sortable
        Third iteration: prev_segment_max = 4, curr_segment_max = 13, curr_segment_min = 13, set_bit_count = 3
        Fourth iteration: prev_segment_max = 4, curr_segment_max = 13, curr_segment_min = 7, set_bit_count = 3
        Fifth iteration: prev_segment_max = 4, curr_segment_max = 14, curr_segment_min = 7, set_bit_count = 3
        At the end of the array, we always check if prev_segment_max <= curr_segment_min, else array will not sortable

        TC: O(nlogn) where O(logn) is for finding the count of set bits
        SC: O(1)
'''

from typing import List

class Solution1:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)

        def findCountOfSetBits(n):
            count = 0 
            while n:
                n = n & (n - 1)
                count += 1
            return count

        for i in range(1, n):
            for j in range(n - i):
                print(i, j)
                if nums[j] <= nums[j + 1]:
                    continue
                else:
                    if findCountOfSetBits(nums[j]) == findCountOfSetBits(nums[j + 1]):
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    else:
                        return False
        return True
    
class Solution2:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)

        prev_segment_max = float("-inf")
        curr_segment_max = nums[0]
        curr_segment_min = nums[0]
        set_bit_count = bin(nums[0]).count("1")

        for i in range(n):
            if bin(nums[i]).count("1") == set_bit_count:
                curr_segment_max = max(curr_segment_max, nums[i])
                curr_segment_min = min(curr_segment_min, nums[i])
            else:
                if prev_segment_max > curr_segment_min:
                    return False
            
                prev_segment_max = curr_segment_max
                curr_segment_max = nums[i]
                curr_segment_min = nums[i]
                set_bit_count = bin(nums[i]).count("1")

        if prev_segment_max > curr_segment_min:
            return False 
        return True