# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        
        if root:
            # traverse
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)

            # swap
            root.left = right
            root.right = left

            return root