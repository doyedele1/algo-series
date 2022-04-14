'''
    Explanation I: Recursive Post-Order (DFS) Traversal
        - base case: if no children, i.e. we are at the leaf node: return 1
        - traverse through the children, set min_depth as the minimum between min_depth and recursive min_depth on children
        - return min_depth + 1
        
        - TC: O(n), SC: O(n) worst case, O(log n) best case
        
    Explanation II: Iterative Post-Order (DFS) Traversal
        - Initialize a stack with root and the corresponding depth which is 1
        - Iterate through the stack, pop the current node and push the child nodes to the stack
        - The min_depth is updated at each leaf node
    
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        children = [root.left, root.right]
        if not any(children): return 1
        
        min_depth = float("inf")
        for child in children:
            if child:
                min_depth = min(min_depth, self.minDepth(child))
        return min_depth + 1