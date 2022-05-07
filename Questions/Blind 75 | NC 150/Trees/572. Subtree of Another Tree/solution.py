'''
    Explanation: Recursive solution with sameTree helper function
        - If subRoot is empty, we know the empty node (null) is a subtree of root, so we can return True
        - If root is empty, then the subRoot is not a subtree of an empty node, so we can return False
        - If the root and subRoot are not empty, and if it's the same tree, then we return True
        - Else, we recursively return the isSubtree function on either the left subtree and the subRoot or the right subtree and the subRoot

        - Same tree helper function:
            - If both trees are empty, resturn True
            - If both trees are non-empty and the values are the same,
                - Then we can recursively return the sameTree function on the left subtree and right subtree of both trees
            - Else, return False

        - TC: O(root + subRoot) => O(n)
        - SC: O(log n) for completely balanced tree, O(n) for completely unbalanced tree)
'''


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        
        if self.sameTree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def sameTree(self, p, q):
        if not p and not q: return True
        if p and q and p.val == q.val:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        return False