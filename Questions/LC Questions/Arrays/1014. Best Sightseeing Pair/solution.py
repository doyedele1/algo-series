'''
    Explanation:
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