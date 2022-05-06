'''
    Explanation: Pre-Order Traversal
    - Visit every node in the binary tree
    - When we visit a parent node, swap the children
    - Recursively run the invert function on the left subtree and right subtree

    - TC: O(n)
    - SC: O(h) where h is the height of the tree. Still equates to O(n)
'''


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # swap the nodes
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root