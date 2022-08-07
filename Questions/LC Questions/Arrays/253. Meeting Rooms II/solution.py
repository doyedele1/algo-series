from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        maxRoomsInUse = 0
        intervals.sort(key= lambda i: i[0])
        
        heapq.heappush(heap, intervals[0][1])
        
        for i in intervals[1:]:
            if i[0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, i[1])
        
        return len(heap)