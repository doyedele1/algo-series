'''
    Explanation I: Recursive DFS (Pre-Order) Traversal
        - If the tree is empty, the max depth is 0
        - If the tree contains only the root node, the max depth is 1
        - If the tree contains either a left child and right child or both, the max depth is 1 + max(max depth of left child and right child)
        - So, with this, we can recursively call maxDepth on either subtree and find the maximum and add to 1
    
        - TC: O(n)
        - SC: O(n) worst case is when each node has only left or right child node. O(log n) best case is when the tree is completely balanced
    
    Explanation II: Iterative BFS Traversal
        - With BFS, the levels of the tree is the maximum depth of the tree
        - TC: O(n)
        - SC: O(n) worst case is when the tree is balanced. O(1) best case is when the tree is completely unbalanced. i.e each node has only left and right child node.
        
    Explanation III: Iterative DFS (Pre-Order) Traversal
        - With DFS, we can keep track of the nodes and the depth in a stack
        - Pop the current node and push the child nodes to the stack. Update the depth
        - The maximum depth is the maximum of the depths in the stack
        
        - TC: O(n)
        - SC: O(n) worst case is when the tree is completely unbalanced. i.e each node has only left and right child node. O(log n) best case is when the tree is balanced
'''

import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        res = 0
        q = collections.deque([root])
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            res += 1
        return res

class Solution3:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [[root, 1]]
        
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res