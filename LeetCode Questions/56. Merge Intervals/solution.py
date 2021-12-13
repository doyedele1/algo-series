from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting by the start value
        intervals.sort(key = lambda i : i[0])
        
        # declaring an output to append the merged intervals
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            # get the end value of the most recently added interval
            last_end = output[-1][1]
            
            if start <= last_end:
                # get the end of the merged interval and add to the output tuple
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
                
        return output
            
        
        
        # T(C) - O(nlogn) where n is the numnber of intervals given
        # S(C) - O(n). we allocate linear space to store a copy of intervals and sort that