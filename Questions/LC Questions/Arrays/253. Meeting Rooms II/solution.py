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
        
        - TC: O(nlogn). nlogn for sorting and another nlogn for n add operations to the heap
        - SC: O(n) for the min heap we constructed


    Explanation II: Sorting, then Two Pointers
    [[0,30],[5,10],[15,20]]
    - Sort startArr = [0, 5, 15]
    - Sort endArr = [30, 10, 20]
    
    [0, 5, 15]          [30, 10, 20]
    s                     e
    res = 0
    - If startArr[s] >= endArr[e], then it means the room is free and we can move the end pointer and decrement our result
    - If startArr[s] < endArr[e], then it means the room is not free and we can move the start pointer and increment our result
    [0, 5, 15]          [30, 10, 20]
        s                 e
    res = 1
    
    [0, 5, 15]          [30, 10, 20]
            s             e
    res = 2
    
    - TC: O(nlogn) for sorting startArr and endArr
    - SC: O(n) for the space taken by the startArr and endArr
'''

from typing import List
import heapq

class Solution1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort(key= lambda i: i[0])
        
        heapq.heappush(heap, intervals[0][1])
        
        for i in intervals[1:]:
            if i[0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, i[1])
        
        return len(heap)


class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res, start, end = 0, 0, 0
        
        startArr = sorted([i[0] for i in intervals])
        endArr = sorted([i[1] for i in intervals])
        
        while start < len(intervals):
            if startArr[start] >= endArr[end]:
                res -= 1
                end += 1
            
            res += 1
            start += 1
            
        return res