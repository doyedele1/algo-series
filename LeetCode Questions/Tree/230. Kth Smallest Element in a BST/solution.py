from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 1
        self.k_smallest = None
        
        def helper(node):
            if not node or self.k_smallest:
                return
            
            helper(node.left)
            if self.counter == k:
                self.k_smallest = node.val
            self.counter += 1
            helper(node.right)
        
        helper(root)
        
        return self.k_smallest


        '''
            TC - O(n)
            SC - memeory used by the recursion stack- O(n) for a skewed tree, O(log n) for a complete balanced tree
        '''