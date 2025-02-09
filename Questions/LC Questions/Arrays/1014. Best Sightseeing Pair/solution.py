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
        second = 1 - 1 = 0
        res = 8
        first = 8

        Second iteration:
        second = 5 - 2 = 3
        res = 11
        first = 8

        Third iteration:
        second = 2 - 3 = -1
        res = 11
        first = 8

        Fourth iteration:
        second = 6 - 4 = 2
        res = 11
        first = 10

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