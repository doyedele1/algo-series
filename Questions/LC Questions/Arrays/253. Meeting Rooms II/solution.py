'''
    Explanation: Min Heap Solution
        [[0,30],[5,10],[15,20]]

        0-----------------------------------------------30
            5---------10
                                15----------20
        
        - Use a heap to keep track of the end times
        - Sort intervals based on the start times since it makes sense to allocate a meeting room for 7am before 3pm
        - heap = [30]
        - For the second interval:
            - Check if the start time is greater than or equal to the top of the heap which is an end time
                - 5 < 30
            - heap = [10, 30]
        - For the third interval:
            - 15 > 10, then we can pop the top of the heap. i.e. heap = [30] and push 20 to the heap
            - heap = [20, 30]
        - Return length of heap which is 2
        
        - TC: O(nlogn). nlogn for sorting and nlogn for n add operations to the heap
        - SC: O(n) for the min heap we constructed
'''

from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort(key= lambda i: i[0])
        
        heapq.heappush(heap, intervals[0][1])
        
        for i in intervals[1:]:
            if i[0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, i[1])
        
        return len(heap)