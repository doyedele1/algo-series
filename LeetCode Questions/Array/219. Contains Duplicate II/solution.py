from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i-k])
            # print(nums[i], seen)
                
        return False
        
        '''
            - Iterate through the array
                - If element in the hash table, return true
                - Add element to the hash table
                - If the size of the hash table is greater than k, remove the oldest element from the hash table
            - Return false
            
            TC - O(n) for search, removal and insertion which with constant TC
            SC - O(min(k, n)) where n is the size of the list. Only min(k, n) items are stored in the hash table
        '''