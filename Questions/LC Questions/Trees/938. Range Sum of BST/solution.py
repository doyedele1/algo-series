from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def range_sum_BST_dfs_recursive(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0

        def dfs(node):
            if not node:
                return 0
            
            nonlocal res
            if low <= node.val <= high:
                res += node.val
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
        
        dfs(root)
        return res
    
    def range_sum_BST_dfs_iterative(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        stack = [root]

        while stack:
            curr = stack.pop()

            if curr:
                if low <= curr.val <= high:
                    res += curr.val
                if curr.val > low:
                    stack.append(curr.left)
                if curr.val < high:
                    stack.append(curr.right)
        return res
    
    def range_sum_BST_bfs_iterative(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        if not root:
            return 0
        
        q = deque([root])
        
        while q:
            curr = q.popleft()
            
            if curr:
                if low <= curr.val <= high:
                    res += curr.val
                if curr.left and curr.val > low:
                    q.append(curr.left)
                if curr.right and  curr.val < high:
                    q.append(curr.right)  
        return res