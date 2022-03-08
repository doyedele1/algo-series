'''
    Explanation:
        - On the root node, we can have range of (-infinity, +infinity)
        - On the left subtree, we can have a range of (-infinity, root.val)
        - On the right subtree, we can have a range of (root.val, +infinity)
        - If the node.val is not in the ranges, then it is not a BST
        - We call the function recursively on (roor.left, lower, root.val) and (root.right, root.val, upper)

        # TC - O(n)
        # SC - O(n)
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Traversal with Valid Range
class Solution:
    def isValidBST(self, root) -> bool:
        return self.validate(root, float("-inf"), float("inf"))

    def validate(self, node, lower, upper):
        if node == None:
            return True

        if node.val <= lower or node.val >= upper:
            return False

        return self.validate(node.left, lower, node.val) and self.validate(node.right, node.val, upper)

# Recursive Inorder Traversal
class Solution:
    def isValidBST(self, root) -> bool:
    
        def inorder(root):
            if root == None: return True
            if not inorder(root.left): return False
            if root.val <= self.prev: return False
            self.prev = root.val
            return inorder(root.right)
    
        self.prev = float("-inf")
        return inorder(root)