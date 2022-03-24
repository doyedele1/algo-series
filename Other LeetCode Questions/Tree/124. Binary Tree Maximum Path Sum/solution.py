from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_curr_sum = root.val
        
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            
            self.max_curr_sum = max(self.max_curr_sum, node.val + left, node.val + right, node.val, node.val + left + right)
            
            return max(node.val, node.val + left, node.val + right)
        
        helper(root)
        
        return self.max_curr_sum