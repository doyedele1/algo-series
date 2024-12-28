'''
    Explanation I: Brute-force
        Visit every single node in the tree and and compute its left height and right height, returning the maximum diameter found.
        T(C): O(n-squared)

    Explanation II: DFS - Bottom-up approach, to cut out the repeated work
        Observations
            Longest path must be between two nodes
            In a tree, number of nodes = edges + 1

        What we need --> Diameter, Height
        Diameter = max(diameter, left_height + right_height)
        Height = max(left_height, right_height) + 1

        Case 1:
                        1
                2               3
            4       5
        At node 4, diameter = 0, height = 1
        At node 5, diameter = 0, height = 1
        At node 2, diameter = 2, height = 2
        At node 3, diameter = 2, height = 1
        At node 1, diameter = 3, height = 3

        Case 2:
                        1
                2               3
            4       5       6       7
        At node 4, diameter = 0, height = 1
        At node 5, diameter = 0, height = 1
        At node 2, diameter = 2, height = 2
        At node 6, diameter = 2, height = 1
        At node 7, diameter = 2, height = 1
        At node 3, diameter = 2, height = 2
        At node 1, diameter = 4, height = 3

        TC: O(n)
        SC: O(n) where n is the height of the tree. O(n) if the tree is skewed (worst case). Else, O(logn) if the tree is balanced
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def compute_height(self, node):
        if not node:
            return 0
        return 1 + max(self.compute_height(node.left), self.compute_height(node.right))
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.compute_height(root.left)
        right_height = self.compute_height(root.right)

        diameter = left_height + right_height
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)
    
class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            if not node:
                return 0
            
            nonlocal diameter
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            diameter = max(diameter, left_height + right_height)
            height = 1 + max(left_height, right_height)
            return height

        dfs(root)
        return diameter