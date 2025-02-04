'''
    Explanation I:
        Sort, then check for adjacent values
        TC: O(n logn), SC: O(1)
    
    Explanation II: 
        Use hashset and check if a certain value exists
            [1, 2, 3, 1]
            Is 1 in our hashset, no, then we add to the hashset. numsSet = {1}
            Is 2 in our hashset, no, then we add to the hashset? numsSet = {1, 2}
            Is 3 in our hashset, no, then we add to the hashset? numsSet = {1, 2, 3}
            Is 1 in our hashset, yes, then we return True

        TC: O(n), SC: O(n)
'''

from typing import List

class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        
        for num in nums:
            if num in nums_set: return True
            nums_set.add(num)
        return False