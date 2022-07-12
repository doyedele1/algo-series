# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        
        def inorder(root, nodes):
            if not root: return
            
            inorder(root.left, nodes)
            nodes.append(root)
            inorder(root.right, nodes)
            
        def helper(nodes, start, end):
            if start > end: return None
            
            middle = (start + end) // 2
            root = nodes[middle]
            
            root.left = helper(nodes, start, middle - 1)
            root.right = helper(nodes, middle + 1, end)
            
            return root
        
        inorder(root, nodes)
        return helper(nodes, 0, len(nodes) - 1)