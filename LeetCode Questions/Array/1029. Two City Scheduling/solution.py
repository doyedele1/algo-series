from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key = lambda x: x[0] - x[1])
        # costs after sorting = [[30, 200], [10, 20], [30, 20], [400, 50]]
        
        n = len(costs)
        cost = 0
        # for i in range(int(len(costs)/2)):
        for c in costs[:int(n/2)]:
            # cost += costs[i][0]
            cost += c[0]
            
        # for i in range(int(len(costs)/2), len(costs)):
        for c in costs[int(n/2):]:
            # cost += costs[i][1]
            cost += c[1]
            
        return cost

        '''
            Explanation:
                - We have to pick equal number of A and B
                Initially,
                - Can we see if we can send all candidates to city A?
                - Now, which of the candidates can we send to B? We will pick the candidate for which we gained the maximum (the most negative number)
                
                10      +  30   +   400   +  30
                +10     +170        -350     -10
                
                --> (A-B) = cost saved on flying a particular candidate to city B instead of city A = money saved by sending candidate to B instead of A
                -10, -170, 350, 10
                Sorting returns (-170, -10, 10, 350)
                
                
                
                TC - O(nlogn) because of sorting the input array
                SC - O(1) since it's a constant space solution
        '''