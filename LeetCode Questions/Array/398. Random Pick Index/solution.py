import collections
from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        # Naive solution
        self.nums = collections.defaultdict(list)
        for index, num in enumerate(nums):
            self.nums[num].append(index)
            
        # Most optimal solution

    def pick(self, target: int) -> int:
        # Naive solution
        return random.choice(self.nums[target])
    
        # Most optimal solution 


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


'''
    Explanation:
        - Create a hashmap to store the indices of any given number that appears in the array
            - Number as the key --> indices as the value
            
        - For the pick method, TC - O(1), SC - O(n)
'''