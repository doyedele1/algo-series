'''
    Explanation I: Recursive Pre-Order Traversal
        - If the tree only contains the root node, the max depth is 1
        - If the tree contains either a left child and right child or both, the max depth is 1 + max(max depth of left child and right child)
        - So, with this, we can recursively call maxDepth on either subtree and find the maximum and add to 1
    
    TC: O(n)
    SC: O(n) worst case is when each node has only left or right child node. O(log n) best case is when the tree is completely balanced

'''     

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

