'''
        Explanation I: Brute-force Solution
            - We have n-squared different subarrays inside of the array
            - We are doing a ton of repeated work by getting the sum of all the single subarrays

        Explanation II: Optimal Solution
            - We will use a hashmap where the key is the prefix_sum and the value is the count of how many times that prefix_sum occurs
            - Can we chop off a prefix to get the required k target number. i.e. for the contiguous array of 4 for [1,1,1,1,1,1], 
                - sum = 4, sum - k = 1. 1 is present in the array
                - Does there exist a prefix starting from the beginning that has a value of 1?
                    - We can, using the count
                - There is an empty prefix of 0 with a count of 1. For case of [1,1,1,1,1,1] and k = 3 for the contiguous array of first 3
        
            [1,-1,1,1,1,1]
            - 0: 1

            - Sum = 1-3 = -2
            - Does -2 exist in the prefix map? No, then we continue and add the prefix just computed of 1 and add to the map and increment count by 1
            - 1: 1

            - Sum = 0-3 = -3
            - No -3 in the prefix map.
            - 0: 2

            - Sum = 1-3 = -2
            - 1: 2

            - Sum = 2-3 = -1
            - 2: 1

            - Sum = 3-3 = 0
            - We do have the prefix sum of 0
            - Count = 2, add to res. Res = 2
            - 3: 1

            - Sum = 4-3 = 1
            - We do have the prefix of 1
            - Count = 2, add to res. Res = 4

            TC - O(n)
            SC - O(n). We use the hashmap that can contain n distinct inputs in the worst case
'''

from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = defaultdict(int)
        prefixSums[0] = 1

        res = 0
        currSum = 0

        for num in nums:
            currSum += num
            diff = currSum - k

            if diff in prefixSums:
                res += prefixSums[diff]

            prefixSums[currSum] += 1
        
        return res
    
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr_sum = 0
        prefix_sum = { 0: 1 }
        
        for n in nums:
            curr_sum += n
            diff = curr_sum - k

            if diff in prefix_sum:
                res += prefix_sum.get(diff, 0)
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        return res