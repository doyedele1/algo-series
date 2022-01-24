from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting by the start value in Python is straightforward. i stands for the interval
        intervals.sort(key = lambda i : i[0])
        
        # declaring an output to append the merged intervals and initializing with the first interval to cover some edge case
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            # get the end value of the most recently added interval
            last_end = output[-1][1]
            
            # this means they are overlapping
            if start <= last_end:
                # get the end of the merged interval and merge - add to the output tuple
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
                
        return output
            
        
        '''
            Explanation:
                - Is input in sorted order?
                - If not in sorted order,
                    - [[1,3], [8, 10], [15, 18], [2,6]]
                - After drawing the number line, we sort the interval by the start value
                - Iterate through each start value, check does the most recent interval overlap with the previous interval, we merge
                -Else we leave it like that

            TC - O(nlogn) where n is the numnber of intervals given
            SC - O(n). we allocate linear space to store a copy of intervals and sort that
        '''