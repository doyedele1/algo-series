# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def post_order(self, node, depth):
        if not node:
            return -1

        if not node.left and not node.right:
            if depth > self.max_depth:
                self.candidate = node
                self.max_depth = depth
            return depth
            
        left = self.post_order(node.left, depth + 1)
        right = self.post_order(node.right, depth + 1)

        if left == right == self.max_depth:
            self.candidate = node
        
        return max(left, right)

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        self.candidate = None
        self.max_depth = -1

        self.post_order(root, 0)
        return self.candidate