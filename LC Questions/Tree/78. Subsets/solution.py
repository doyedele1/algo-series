from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        # i is the index of the value we are making a decision on
        def dfs(i):
            if i >= len(nums): 
                res.append(subset.copy()) # the subset will be modified
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            
            # decision to not include nums[i]
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res
        
        
        '''
            Explanation:
                - We do not care about the order. It is not a permutation, but a subset. We don't want to include duplicates
                
                - [1,2,3]
                    2 exp n = number of subsets. n = size of the input, 2 is the choice for every single input element
                    - TC: O(n * 2 exp n)
                    
                    [1,2,3]
                    - We have a choice for each single element
                    - We can draw a decision tree
        
        '''