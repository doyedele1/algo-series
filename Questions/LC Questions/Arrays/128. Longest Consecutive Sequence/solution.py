'''
    Explanation:
        [100,4,200,1,3,2]
        Can we sort the input array, then check for consecutive numbers and keep track of the length of the sequence?
        TC - O(n logn) where n is the length of the nums array

        How can we do better? Let's have the possible sequences of the nums
        [1,2,3,4] [100] [200]
        What can we notice here? The first number in each sequence (1, 100, 200) must not have a number (1 unit) below it in the nums array (0, 99, 199)
        
        set = (100, 4, 200, 1 , 3, 2)
        For num 100,
            99 not in set, so that's the start of a sequence
            Is 100 + 0 in set? No, res = 0
        
        For num 4,
            3 in set, so 4 cannot start the sequence
        
        For num 200,
            199 not in set, so that's the start of a sequence
            Is 200 + 0 in set? No, res = 0
        
        For num 1,
            0 not in set, so that's the start of a sequence
            Is 1 + 0 in set? Yes, sequence_length = 1
            Is 1 + 1 in set? Yes, sequence_length = 2
            Is 1 + 2 in set? Yes, sequence_length = 3
            Is 1 + 3 in set? Yes, sequence_length = 4
            Is 1 + 4 in set? No, res = 4

        For num 3,
            2 in set, so 3 cannot start the sequence

        For num 2,
            1 in set, so 2 cannot start the sequence
        
        TC: O(n)
        SC: O(n)
'''

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for num in nums:
            if (num - 1) not in num_set:
                sequence_length = 0
                while (num + sequence_length) in num_set:
                    sequence_length += 1
                res = max(res, sequence_length)

        return res