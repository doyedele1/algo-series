'''
    Explanation I: BFS + Lowest Common Ancestor

        Find all deepest node by traversing the tree using BFS
        Using the BFS, find the leftMost and rightMost nodes on every level
        Find LCA of the last leftMost and rightMost nodes - this will be your answer

    Explanation II: PostOrder DFS Traversal
        TC: O(n)
        SC:O(n)
'''
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BFSSolution:
    def lca(self, node, p, q):
        if not node or node == p or node == q:
            return node
        
        left = self.lca(node.left, p, q)
        right = self.lca(node.right, p, q)

        if left and right:
            return node
        if left:
            return left
        return right

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])

        while q:
            size = len(q)

            for i in range(size):
                curr = q.popleft()

                if i == 0:
                    leftMost = curr
                if i == size - 1:
                    rightMost = curr
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return self.lca(root, leftMost, rightMost)
    
class DFSSolution:
    def post_order(self, node, depth):
        if not node:
            return -1
        
        # If it's a leaf node
        if not node.left and not node.right:
            if depth > self.max_depth:
                self.candidate = node
                self.max_depth = depth
            return depth

        left = self.post_order(node.left, depth + 1)
        right = self.post_order(node.right, depth + 1)

        # We have our lca if the depth of the two children are the same and the depth is the maximum depth
        if left == right == self.max_depth:
            self.candidate = node
        
        return max(left, right)
    
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        self.candidate = None
        self.max_depth = -1

        self.post_order(root, 0)
        return self.candidate