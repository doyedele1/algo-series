'''
    Explanation:
    Example 1: [[0,30],[5,10],[15,20]]
    
    0-----------------------------------------------30
            5---------10
                                15----------20
    - When 30 > 5, i.e. there is an overlap. The person can't attend 0---30 meeting and 5---10 meeting, so we return False.
    
    Example 2: [[7,10],[2,4]]
    2-----4
                7---------10
    - There is no overlap here. So we return True
    
    TC: O(nlogn)
    SC: O(1)
'''

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key= lambda i: i[0])
        
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True