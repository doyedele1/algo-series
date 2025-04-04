'''
    TC: O(n)
    SC: O(1), but can be O(n) because the maximum amount of space utilized by the recursion stack would be n where n could be the height of a skewed binary tree
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root
            
        # Case 1: If both left and right are null, return null
        if not root.left and not root.right:
            return None

        left = self.lowestCommonAncestor(root.left, p, q) if root.left else None
        right = self.lowestCommonAncestor(root.right, p, q) if root.right else None

        # Case 2: If both left and right are not null, return root
        if left and right:
            return root
        # Case 3: If left is null and right is not null, return right, else otherwise
        return right if left is None else left