'''
    - Initialize three vqriables
        - res = 0
        - sum = neededTime[0]
        - maxTime = neededTime[0]
    - Loop through the string
        - If there are duplicates, alter sum to be sum + neededTime[i] and maxTime = max(maxTime, neededTIme[i])
        - Else, add res to (sum - maxTime) and reset the sum and maxTime pointers
    - Add the res to (sum - maxTime)
    - Return res
    
    TC: O(n)
    SC: O(1)
'''


from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        sum = maxTime = neededTime[0]
        
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                sum += neededTime[i]
                maxTime = max(maxTime, neededTime[i])
            else:
                res += (sum - maxTime)
                sum = maxTime = neededTime[i]
        res += (sum - maxTime)
        return res