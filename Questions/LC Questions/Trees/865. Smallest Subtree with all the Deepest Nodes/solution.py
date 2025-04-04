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
        if node.val == p.val or node.val == q.val:
            return node

        if not node.left and not node.right:
            return None
        
        left = self.lca(node.left, p, q) if node.left else None
        right = self.lca(node.right, p, q) if node.right else None

        if left and right:
            return node
        return right if left is None else left

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
    def dfs(self, curr):
        if not curr:
            return (None, 0)
        
        left_lca, left_depth = self.dfs(curr.left)
        right_lca, right_depth = self.dfs(curr.right)

        if left_depth == right_depth:
            return (curr, left_depth + 1)
        elif left_depth > right_depth:
            return (left_lca, left_depth + 1)
        else:
            return (right_lca, right_depth + 1)

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lca, depth = self.dfs(root)
        return lca