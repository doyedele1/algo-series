'''
    Explanation:
    - TC: O(n) where n is the number of nodes; we visit each node exactly once
    - SC: O(log n)- the recursive call stack requires O(log n) space since the tree is height-balanced. The space used to create the output is not accounted for
'''

from typing import List, Optional
from random import randint

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(start, end):
            # base case
            if start > end: return None
            
            middle = start + (end - start) // 2
            # length of nums is even
            if (start + end) % 2:
                # choose random middle node as a root
                middle += randint(0, 1)
                
            root = TreeNode(nums[middle])
            root.left = helper(start, middle - 1)
            root.right = helper(middle + 1, end)
            return root
            
        return helper(0, len(nums) - 1)