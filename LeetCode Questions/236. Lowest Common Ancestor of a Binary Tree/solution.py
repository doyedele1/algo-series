# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        
        def search(node):
            if node == None:
                return False
            
            leftSearch = search(node.left)
            rightSearch = search(node.right)
            current = node == p or node == q
            
            if (leftSearch and rightSearch) or (current and leftSearch) or (current and rightSearch):
                self.ans = node
                return
            return leftSearch or rightSearch or current
        
        search(root)
        return self.ans