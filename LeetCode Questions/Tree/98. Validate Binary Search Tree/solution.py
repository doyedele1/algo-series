'''
    Explanation: Recursive Traversal with Valid Range
        - On the root node, we can have any number so we are safe to bound the root node in the range of (-infinity, +infinity)
        - The values in the left subtree are upper bounded by the root node
            - On the left subtree, we can have a range of (-infinity, root.val)
        - The values in the right subtree are lower bounded by the root node
            - On the right subtree, we can have a range of (root.val, +infinity)
        - If the node.val is not in the ranges, then it is not a BST
        - We call the function recursively on (root.left, lower, root.val) and (root.right, root.val, upper)

        # TC - time taken by the validate method --> O(n) where n is the number of nodes in the tree
        # SC - O(n) - for the recursive call stack to save the root node, lower and upper bounds. This happens when the tree is skewed or is a linked list and we call the validate function.

    Explanation: Recursive Inorder Traversal
        - For inorder traversal, we first need to go to the left subtree, then process the root node and finally go to the right subtree.
        - The inorder traversal of a BST will return values in a sorted (increasing) order
        - At each step, we will make sure that the value of the node being processed is greater than the previous value we have already processed
            - We can initialize previous value as -infinity
            - If the value of the node during inorder traversal is less than the previous value, then the tree is not a BST.
            - If it is greater than the previous value, then we can continue the inorder traversal, but previous value will be the current node's value
        TC - O(n) in the worst case when the tree is a BST or the "bad" element is a rightmost leaf
        SC - O(n) for the space on the runtime stack
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Traversal with Valid Range
class Solution:
    def isValidBST(self, root) -> bool:
        def validate(node, lower, upper):
            if node == None:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            return validate(node.left, lower, node.val) and validate(node.right, node.val, upper)
        return validate(root, float("-inf"), float("inf"))

# Recursive Inorder Traversal
class Solution:
    def isValidBST(self, root) -> bool:
        def inorder(root):
            if root == None: return True
            if not inorder(root.left): return False # if root's left subtree is not a BST, then return False
            if root.val <= self.prev: return False
            self.prev = root.val
            return inorder(root.right)
    
        self.prev = float("-inf")
        return inorder(root)