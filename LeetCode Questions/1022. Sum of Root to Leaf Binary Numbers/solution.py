# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root):
    
        def helper(root, sum):
            if not root: return 0
            sum = (sum << 1) + root.val
            if not root.left and not root.right:
                return sum
            return (helper(root.left, sum) + helper(root.right, sum))
        
        return helper(root, 0)
    
#     TC- O(N)
#     SC - O(H) = O(1) where h is the height of the stack