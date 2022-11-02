'''
    Explanation:
        - TC: O(n log n). The getHeight function is called on a node p, O(log n) times. We stop recursion as soon as the height of a node's children are not within 1, and our algorithm is then bounded by O(n) as it checks only the height of the first two subtrees
        - SC: O(n)- the recursion call stack may contain all nodes if the tree is skewed
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        def getHeight(node):
            if not node: return -1
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        return abs(getHeight(root.left) - getHeight(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)