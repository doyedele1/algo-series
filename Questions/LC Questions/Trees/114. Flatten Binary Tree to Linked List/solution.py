'''
    Explanation:
                5
        2               1
    6       23      11
14
            turns to when we perform recursion on the left and right subtrees
                        5
        2 (LEFT)                         1 (RIGHT)
            6                               11
                44
                    23 (LEFTTAIL)
        
        - The connections:
            LEFTTAIL.right = RIGHT
            root.right = root.left
            root.left = None
        
        - TC: O(n)
        - SC: O(n)
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node: return node
            
            leftTail = dfs(node.left)
            rightTail = dfs(node.right)
            
            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None
            
            return rightTail or leftTail or node
        
        dfs(root)