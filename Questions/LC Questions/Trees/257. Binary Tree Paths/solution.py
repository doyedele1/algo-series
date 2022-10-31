# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Iterative DFS solution
class Solution1:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = [(root, str(root.val))]
        res = []
        
        while stack:
            node, path = stack.pop()
            
            if not node.left and not node.right: res.append(path)
            if node.left: stack.append((node.left, path + "->" + str(node.left.val)))
            if node.right: stack.append((node.right, path + "->" + str(node.right.val)))
        
        return res

# Recursive DFS solution
class Solution2:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, path):
            if not node.left and not node.right: res.append(path)
            if node.left: dfs(node.left, path + "->" + str(node.left.val))
            if node.right: dfs(node.right, path + "->" + str(node.right.val))
        
        dfs(root, str(root.val))
        return res