'''
    Explanation: Sliding Window
        [2, 3, 1, 2, 4, 3], target = 7

        [2, 3, 1, 2], sum = 8 which is greater than 7
        Since the values in the array are positive, then we know that [2, 3, 1] wasn't going to give us a value greater than or equal to 7

        [2, 3, 1, 2, 4, 3]
         i  j
        total = 5
'''

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        return