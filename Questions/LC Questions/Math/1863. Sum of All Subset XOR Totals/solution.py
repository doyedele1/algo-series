'''
    Explanation I: Recursion
        If nums = [4,3,5], then we will have a recursion tree of
                        4
                3               3
            5       5       5       5
        left child = don't include it in your subset
        right child = include it in your subset

        TC: O(2^n) where n is the height of the tree
        SC: O(n)

    Explanation II: Math (Combinatorics) and Bit Manipulation - quite difficult to understand
        Let's assume nums = [4,3,5]
        4 = 0100
        3 = 0011
        5 = 0101

        To know the number of contributions of the subsets, we need to check if any of the bits is a 1
        For example, for number 4 (0100), the 2nd bit from the right is a 1 and that means it will contribute to half of the possible subsets which is 8/2 = 4
        Hence, we can say the number of subset contribution = 2 ^ (n - 1) where n is the size of nums

        To know the if any of the bits has a 1, we can do a bitwise OR of 4, 3 and 5

        Then, to get the total contributions of all bits = number of subset contribution * weight of the bit

        Dry run:
        For [4,3,5], 
        4 OR 3 OR 5 = 0111 = 7

        Since there's a 1, number of set contribution = 2 ^ (3 - 1) = 4
        Total contributions of all bits = (4*4) + (4*2) + (4*1) = 16 + 8 + 4 = 28

        TC: O(n)
        SC: O(1)
'''
from typing import List

class Solution1:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, total):
            if i == len(nums):
                return total
            left = dfs(i + 1, total) # don't include the number
            right = dfs(i + 1, total ^ nums[i]) # include the number

            return left + right
        
        return dfs(0, 0)
    
class Solution2:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        orr = 0

        for num in nums:
            orr |= num
        return orr * (2 ** (n - 1))
        # return orr * (1 << (n - 1))