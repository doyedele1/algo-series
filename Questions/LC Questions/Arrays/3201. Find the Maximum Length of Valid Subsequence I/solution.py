'''
    Explanation:
        We know that if we have [a,b,c,d,e,f], there are three cases where we can have valid solution
        Case 1: a, b, c, d, e, f are all odd
            Example: 1, 3, 5, 7, 9, 11

        Case 2: a, b, c, d, e, f are all even
            Example: 2, 4, 6, 8, 10, 12

        Case 3: a, b, c, d, e, f are alternating between odd and even or even and odd. i.e.
            a, c, e are odd; b, d, f are even
                Example: 1, 2, 3, 4, 5, 6

            a, c, e are even; b, d, f are odd
                Example: 2, 3, 4, 5, 6, 7

        With these three cases, we can find the maximum of the odd_count, even_count and alternating_count.

        TC: O(n), SC:O(1)
'''

from typing import List

class Solution:
    def isOdd(self, num: int) -> bool:
        return num % 2
    
    def isEven(self, num: int) -> bool:
        return num % 2 == 0

    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)

        odd_count = 1 if self.isOdd(nums[0]) else 0
        even_count = 1 if self.isEven(nums[0]) else 0
        alternating_count = 1
        expecting_even = True if self.isOdd(nums[0]) else False

        for i in range(1, n):
            if self.isOdd(nums[i]):
                odd_count += 1
                if not expecting_even:
                    alternating_count += 1
                    expecting_even = not expecting_even
            else:
                even_count += 1
                if expecting_even:
                    alternating_count += 1
                    expecting_even = not expecting_even

        return max(odd_count, even_count, alternating_count)