'''
    Explanation I: Recursive Pre-Order Traversal
    
    
    TC: O(n)
    SC: O(n) worst case is when each node has only left or right child node. O(log n) best case is when the tree is completely balanced

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        