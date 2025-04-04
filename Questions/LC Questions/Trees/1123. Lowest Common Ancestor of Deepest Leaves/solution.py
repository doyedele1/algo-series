'''
    Explanation:
        Observations
        1. If we have only one deepest leaf, the LCA is that leaf
        2. If we have multiple deepest leaves, we should assume the farthest two leaves

        Solution 1: TC: O(n), SC: O(n)
        - We can do a BFS to find all the nodes at the last level
        - Then, we can run a LCA(p, q) to find the lowest common ancestor. LCA(p, q) is a solution from LeetCode 236

        Solution 2: TC: O(n), SC: O(n)
        LSD -> Left Subtree Depth, RSD -> Right Subtree Depth
        - If LSD = RSD, the current node is our LCA
        - If LSD > RSD, the LCA is in the LSD
        - If RSD > LSD, the LCA is in the RSD

        Hence, we will go with the second solution
        Step 1: Use DFS to precompute the depth
        Step 2: Use DFS to find the LCA of the deepest leaves

        But we can even do better and do just one DFS. By tracking the LCA values and depth values together

        if LSD = RSD, return {currNode, 1 + LSD}
        if LSD > RSD, return {LCA of the left subtree, 1 + LSD}
        if RSD > LSD, return {LCA of the right subtree, 1 + RSD}
'''
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
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

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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
    
class Solution2:
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

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lca, depth = self.dfs(root)
        return lca