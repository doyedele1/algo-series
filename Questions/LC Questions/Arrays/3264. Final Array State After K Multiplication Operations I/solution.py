'''
    TC: O(n + klogn)
    Building the heap takes O(n) time
    Removal and insertion in heap takes O(log n) time. But for k times, O(klogn)

    SC: O(n) for the heap. n is the size of nums array
'''
from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        min_heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(min_heap)

        while k > 0:
            k -= 1
            min_value, index = heapq.heappop(min_heap)

            new_num = min_value * multiplier
            nums[index] = new_num
            heapq.heappush(min_heap, (new_num, index))

        return nums