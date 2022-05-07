'''
    Solution1: Nested loops - TC: O(n-squared), SC: O(1)
    Solution2: Sort, then check for adjacent values - TC: O(n logn), SC: O(1)
    Solution3: Use hashset and check if a certain value exists
        [1, 2, 3, 1]
        Is the first 1 in our hashset, then we add to the hashset. Hashset: {1}
        Is 2 in our hashset? Hashset = {1, 2}
        Is 3 in our hashset? Hashset = {1, 2, 3}
        Is 1 in our hashset, yes, then we return True

        TC: O(n), SC: O(n)
'''

from typing import List

class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        
        for num in nums:
            if num in hashSet: return True
            hashSet.add(num)
        return False

class Solution4:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freqCounter = {}
        
        for i in range(len(nums)):
            freqCounter[nums[i]] = 1 + freqCounter.get(nums[i], 0)
        
        for num in freqCounter:
            if freqCounter[num] > 1: return True
            
        return False