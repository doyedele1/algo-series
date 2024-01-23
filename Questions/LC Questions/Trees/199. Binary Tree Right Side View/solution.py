'''
        Explanation:
            - Initialize res array
            - Add the root node to a queue
            - While queue is not empty,
                - Get the length of the current level which is the length of the queue
                - Iterate over the queue,
                    - Pop the current node
                    - If index i is equal to length_of_each_level - 1, then we know that's the last node in the level
                    - Add the child nodes to the queue
            - Return res

            TC - O(n) where n is the number of nodes visited
            SC - O(d) for the queue, where d is the tree diameter. The last level could take up to n/2 tree nodes in the case of a complete binary tree
'''

from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root

        q = deque([root])
        res = []

        while q:
            length_of_each_level = len(q)

            for i in range(len(q)):
                node = q.popleft()
                if i == length_of_each_level - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res