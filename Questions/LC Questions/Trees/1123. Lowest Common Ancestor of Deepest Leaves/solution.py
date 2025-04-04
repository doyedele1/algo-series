'''
    Explanation:
        Observations
        1. If we have only one deepest leaf, the LCA is that leaf
        2. If we have multiple deepest leaves, we should assume the farthest two leaves

        First solution:
        - We can do a BFS to find all the nodes at the last level
        - Then, we can run a LCA(p, q) to find the lowest common ancestor. LCA(p, q) is a solution from LeetCode 236
        TC: O(n), SC: O(n)

        Second solution:
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

        TC: O(n), SC: O(n)
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLCA(self, curr):
        if not curr:
            return (None, 0)
        
        left_lca, left_depth = self.findLCA(curr.left)
        right_lca, right_depth = self.findLCA(curr.right)

        if left_depth == right_depth:
            return (curr, 1 + left_depth)
        elif left_depth > right_depth:
            return (left_lca, 1 + left_depth)
        else:
            return (right_lca, 1 + right_depth)

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lca, depth = self.findLCA(root)
        return lca