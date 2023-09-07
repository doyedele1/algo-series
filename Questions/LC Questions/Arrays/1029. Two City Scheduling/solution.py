'''
    Explanation:
        - We have to pick equal number of cities A and B
        Initially,
        - Can we see if we can send all candidates to city A?
        - Now, which of the candidates can we send to B? We will pick the candidate for which we gained the maximum (the most negative number)
        
        --> (A-B) = by sending person to city A, the company would lose A-B

        [[10,20],[30,200],[400,50],[30,20]]
        -10, -170, 350, 10
        Sorting returns (-170, -10, 10, 350)

        
        TC - O(nlogn) because of sorting the input array
        SC - O(n). Timsort algorithm is used in Python; which is a combination of Merge Sort and Insertion Sort
'''

from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key = lambda x: x[0] - x[1])
        # costs after sorting = [[30, 200], [10, 20], [30, 20], [400, 50]]
        
        res = 0
        n = len(costs) // 2
        
        for i in range(n):
            res += costs[i][0] + costs[i + n][1]
            
        return res