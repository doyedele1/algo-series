import random
from typing import List
# import collections

class Solution:

    def __init__(self, nums: List[int]):
        # Naive solution
        # self.nums = collections.defaultdict(list)
        # for index, num in enumerate(nums):
        #     self.nums[num].append(index)
            
        # Most optimal solution
        self.nums = nums

    def pick(self, target: int) -> int:
        # Naive solution
        # return random.choice(self.nums[target])
    
        # Most optimal solution
        res = None
        count = 0
        
        for index, num in enumerate(self.nums):
            if num == target:
                if random.randint(0, count) == count:
                    res = index
                count += 1
        return res

'''
    Explanation I:
        - Create a hashmap to store the indices of any given number that appears in the array
            - Number as the key --> indices as the value
        
        - For the constructor method, TC - O(n), SC - O(n)
        - For the pick method, TC - O(1), SC - O(n)
        
    Explanation II:
        - First time we see a target number, we want to keep it. One over one probability of keeping that index number as the return value. Probability = 1
        - Second time we see the target number again, we will reduce the previous memory to be one-half and the current index has one-half of the chance to be the new memory. Probability = 1 * 1/2, 1/2
        - Third time we see the target number, we decide whether we want to update the memory to return the current third index number of the final result. Probability = 1/2 * 2/3 = 1/3, 1/3
        - To make sure that every occurence of the target value has equal probabilities
        
        - For the constructor method, TC - O(1), SC - O(1)
        - For the pick method, TC - O(n), SC - O(1)
'''

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)