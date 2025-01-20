'''
    Explanation I: BFS + Lowest Common Ancestor

        Find all deepest node by traversing the tree using BFS
        Using the BFS, find the leftMost and rightMost nodes on every level
        Find LCA of the last leftMost and rightMost nodes - this will be your answer
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