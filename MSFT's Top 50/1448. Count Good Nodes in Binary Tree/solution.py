'''
    Explanation I: PreOrder (DFS) Traversal
        - From the root node, go to the node, check if it is greater than the maximum value seen so far
        - Update the maximum value seen so far
        - Go to the left child next, check if it is greater than the maximum value seen so far
        - Go to the right child next, check if it is greater than the maximum value seen so far
        
        - TC: O(n) where n is the number of nodes
        - SC: O(n) where n is the height of the tree (worst case- tree with a single path)
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def goodNodes(self, root: TreeNode) -> int: 
        def dfs(node, maxVal):
            nonlocal res
            if not node: return 0
            if maxVal <= node.val: res += 1
            maxVal = max(maxVal, node.val)
            if node.left: dfs(node.left, maxVal)
            if node.right: dfs(node.right, maxVal)
        
        res = 0   
        dfs(root, root.val)
        return res