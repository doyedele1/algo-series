'''
    Explanation:    
        [[1,3], [8, 10], [15, 18], [2,6]]
        1-----3
                        8------10
                                        15--------18
            2------6
        - Sort intervals based on the start times
        [[1,3], [2,6], [8, 10], [15, 18]]
        - Add the first interval to the res nested array
        - Iterate through the intervals starting from the second interval,
            - Check the most recent added interval to res
            - If the current start time overlap with the end time of the most recent added interval, we merge
            - Else, we leave it like that

        TC - O(nlogn)
        SC - O(1)
'''
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i: i[0])
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            recentEnd = res[-1][1]
            if start <= recentEnd:
                res[-1][1] = max(recentEnd, end)
            else:
                res.append([start, end])
        return res