'''
    Explanation I: Selection sort and swapping
        TC: O(n-squared)
    
    Explanation II: Sorting and two-pointer approach
        Step 1: Find the index of each number and store the number and index in a new array
        Step 2: Sort the new array by number, not index
        Step 3:
            1. Find groups based on |nums[i] - nums[j]| <= limit and store their initial indices in a group array
            2. Sort the group array which consists only of indices of each group
            3. Place every number in copy to where the indices are in the sorted indices

        Example:
        [10, 3, 5, 11, 2, 8], limit = 2

        Step 1: 
            copy = [(10, 0), (3, 1), (5, 2), (11, 3), (2, 4), (8, 5)]
        
        Step 2:
            copy = [(2, 4), (3, 1), (5, 2), (8, 5), (10, 0), (11, 3)]
        
        Step 3:
            group = [4, 1, 2 | 5, 0, 3]

            Sort group => [1, 2, 4 | 0, 3, 5]
            
            copy = [2, 3, 5, 8, 10, 11]
            Place number 2 in index 1
            Place number 3 in index 2
            Place number 5 in index 4
            Place number 8 in index 0
            Place number 10 in index 3
            Place number 11 in index 5
            nums = [8, 2, 3, 10, 5, 11]

        TC: O(nlogn)
        SC: O(n)
'''
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        copy = [(nums[i], i) for i in range(n)]

        copy.sort()

        l, r = 0, 1

        while r < n:
            group = [copy[l][1]]
            while r < n and abs(copy[r][0] - copy[r - 1][0]) <= limit:
                group.append(copy[r][1])
                r += 1
            
            group.sort()

            for i in range(r - l):
                nums[group[i]] = copy[l + i][0]
            
            l = r
            r += 1
            
        return nums