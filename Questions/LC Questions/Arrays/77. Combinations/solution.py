'''
    Explanation: Backtracking
        n = 4, k = 2
                                []
               [1]                 [2]                [3]                [4]
        [1,2] [1,3] [1,4]       [2,3] [2,4]          [3,4]

        * To prevent duplicate combinations like [2,1], we only represent the node greater than its own

        Add the first element 1, so we have combination = [1]
        Lock this 1 and find all combinations that start with 1

        [1,2] is a combination, since we've reached length of k, we remove 2 from the combination array and find the next combination
        [1,3] is a combination, since we've reached length of k, we remove 3 from the combination array and find the next combination
        [1,4] is a combination, since we've reached length of k and we have all combinations that start with 1, we backtrack by removing 1 from the combination array

        Add the next element 2, so we have combination = [2]
        Lock this 2 and find all combinations that start with 2

        [2,3] is a combination, since we've reached length of k, we remove 3 from the combination array and find the next combination
        [2,4] is a combination, since we've reached length of k and we have all combinations that start with 2, we backtrack by removing 2 from the combination array

        Add the next element 3, so we have combination = [3]
        Lock this 3 and find all combinations that start with 3

        [3,4] is a combination, since we've reached length of k and we have all combinations that start with 3, we backtrack by removing 3 from the combination array

        TC: O(nCk)
        SC: O(k)
'''

from typing import List

class BacktrackSolution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(start: int, combination: List[int]):
            if len(combination) == k:
                res.append(combination[:]) # Make a copy of the combination
                return
            
            for num in range(start, n + 1):
                combination.append(num)
                backtrack(num + 1, combination)
                combination.pop() # Remove the last number to backtrack
                
        res = []
        backtrack(1, [])
        return res
    
class RecursiveSolution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        if n < k:
            return []

        with_n = self.combine(n - 1, k - 1)
        for comb in with_n:
            comb.append(n)

        without_n = self.combine(n - 1, k)

        return with_n + without_n