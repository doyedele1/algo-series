'''
    Explanation: Greedy (math)

        smallest_one = smallest sum with 1 as remainder
        smallest_two = smallest sum with 2 as remainder

    TC: O(n), SC: O(1)
'''
from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = 0
        smallest_one = float("inf")
        smallest_two = float("inf")

        for num in nums:
            total += num
            if num % 3 == 1:
                smallest_two = min(smallest_two, num + smallest_one)
                smallest_one = min(smallest_one, num)
            if num % 3 == 2:
                smallest_one = min(smallest_one, num + smallest_two)
                smallest_two = min(smallest_two, num)

        if total % 3 == 0:
            return total
        if total % 3 == 1:
            return total - smallest_one
        if total % 3 == 2:
            return total - smallest_two