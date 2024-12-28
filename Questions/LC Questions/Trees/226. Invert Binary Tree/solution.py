'''
    Explanation I: Recursive DFS (Pre-order)
        Visit every node in the binary tree
        When we visit a parent node, swap the children
        Recursively run the invert function on the left subtree and right subtree

        TC: O(n)
        SC: O(h) where h is the height of the tree

    Explanation II: Iterative BFS
        TC: O(n)
        SC: O(n/2) for a full binary tree since the leaf node has n/2 leaves
'''
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invert_tree_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root
    
    def invert_tree_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = deque([root])

        while q:
            curr = q.popleft()

            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return root