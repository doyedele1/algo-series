# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, minVal, maxVal):
            if not node:
                return True
            
            if node.val <= minVal:
                return False
        
            if node.val >= maxVal:
                return False
            
            return (validate(node.left, minVal, node.val) and validate(node.right, node.val, maxVal))
        
        return validate(root, float("-inf"), float("inf"))
        