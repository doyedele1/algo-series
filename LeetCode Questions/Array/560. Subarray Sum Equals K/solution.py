from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        run_sum = 0
        dict = {}
        dict[0] = 1
        
        for i in range(len(nums)):
            run_sum += nums[i]
            if (run_sum - k) in dict:
                count += dict[run_sum - k]
            if not run_sum in dict:
                dict[run_sum] = 0
            dict[run_sum] = dict.get(run_sum) + 1
            
                    
        return count
    
    '''
        T(C) - O(n)
        S(C) - We use a hashmap that can contain n distinct inputs in the worst case
    '''