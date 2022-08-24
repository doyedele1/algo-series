'''
    Time Complexity : O(n + log k * log n)

    Creating a heap is O(n).

    At each step, we were removing at least 1/4 of the total sum. The original total sum is 2 * k, because k is the largest element, and we know that if the algorithm continues, then the rest can't add up to more than k. So, we need to take O(logk) steps to reduce the array down. Each of these steps is the cost of a heap add and remove, i.e. O(logn). In total, this is O(logk * logn)

    Space Complexity : O(n)
'''

import heapq
from typing import List

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # Handle the n = 1 case.
        if len(target) == 1:
            return target == [1]

        total_sum = sum(target)

        target = [-num for num in target]
        heapq.heapify(target)
        while -target[0] > 1:
            largest = -target[0]
            rest = total_sum - largest

            # This will only occur if n = 2.
            if rest == 1:
                return True

            x = largest % rest

            # If x is now 0 (invalid) or didn't
            # change, then we know this is impossible.
            if x == 0 or x == largest:
                return False
            heapq.heapreplace(target, -x)
            total_sum = total_sum - largest + x

        return True