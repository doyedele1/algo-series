'''
    Explanation:
        values[i] + values[j] + i - j
        We can rearrange the above expression as (values[i] + i) + (values[j] - j)
        where first = values[i] + i and second = values[j] - j
        
        second = values[j] - j
        res = max(res, first + second)
        first = max(first, values[j] + j)
        
        Dry run:
        [8,1,5,2,6]

        First iteration:
        Initially, first = values[j] + j = 8 + 0 = 8
        second = 1 - 1 = 0
        res = max(0, 8 + 0) = 8
        first = max(8, 1 + 1) = 8

        Second iteration:
        first = 8
        second = 5 - 2 = 3
        res = max(8, 8 + 3) = 11
        first = max(8, 5 + 2) = 8

        Third iteration:
        first = 8
        second = 2 - 3 = -1
        res = max(11, 8 - 1) = 11
        first = max(8, 2 + 3) = 8

        Fourth iteration:
        first = 8
        second = 6 - 4 = 2
        res = max(11, 6 + 4) = 11
        first = max(8, 6 + 4) = 10

        TC: O(n)
        SC: O(1)
'''
from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        first = values[0]
        res = 0

        for j in range(1, n):
            second = values[j] - j
            res = max(res, first + second)
            first = max(first, values[j] + j)
        return res