'''
    Explanation I: Recursive Solution
        - From the root node
            - If the p value is less than the root value and the q value is less than the root value, then we need to recursively return the lca on the left subtree
            - If the p value is greater than the root values and the q value is greater than the root values, then we need to recursively return the lca on the right subtree
            - Else, the lca is the root itself
        
        - TC: O(log n) for balanced BST, but O(n) for skewed BST
        - SC: O(1) for balanced BST, but O(n) for skewed BST
        
    Explanation II: Iterative Solution
        - Same approach as the recursive solution
        - Here we initialize node as root and iterate while node is not null, perform the checks to run the left or right subtree
        - Else, return the node
        
        - TC: O(log n) for balanced BST, but O(n) for skewed BST
        - SC: O(1) since we are not using any extra data structure
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else: return root

class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root

        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else: return node