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
        
    def validate(self, node, min_value, max_value):
        if node == None:
            return True

        if (min_value != None and node.val <= min_value) or (max_value != None and node.val >= max_value):
            return False

        return self.validate(node.left, min_value, node.val) and self.validate(node.right, node.val, max_value)

    # TC - O(n)
    # SC - O(n)

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