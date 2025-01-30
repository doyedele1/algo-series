'''
    Explanation:
        * All the levels till the 2nd last level must be completely filled
        * Last level may or may not be completely filled
            - If not completely filled, then the nodes should be filled from left to right
            - If completely filled, then this is a perfect binary tree

        * For a perfect binary tree which is a complete binary tree, number of nodes = 2^level - 1
        * For the case where it is not a perfect binary tree, we perform the left extreme call and the right extreme call
                    1
            2               3
        4       5       6     

        At node 1, 
        left = 3, right = 2. Since they are not the same, we go into node 2 and 3 and perform the left and right extreme calls

        At node 2,
        left = 2, right = 2. Since they are the same, that means the tree from node 2 is a perfect tree.
        Number of nodes at this tree is 2^2 - 1 = 3

        At node 3,
        left = 2, right = 1. Since they are not the same, we go into node 6 and None node and perform the left and right extreme calls

        At node 6,
        left = 1, right = 1. Since they are the same, that means the tree from node 6 is a perfect tree.
        Number of nodes at this tree is 2^1 - 1 = 1

        Then, we go back to node 3 and return 1 from node 6 and itself = 1 + 1 = 2 nodes
        Then, we also go back to node 1 and return 3 at node 2 and 2 at node 3 and itself = 3 + 2 + 1 = 6 nodes

        TC: O(logAlogB) where A is the level of the tree and B is the leaf nodes
        SC: O(1)
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_level = 1
        l = root.left
        while l:
            l = l.left
            left_level += 1
        
        right_level = 1
        r = root.right
        while r:
            r = r.right
            right_level += 1
        
        if left_level == right_level:
            return 2 ** left_level - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)