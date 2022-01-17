import collections
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS with Two Queues Approach
        res = []
        next_level = collections.deque([root])
        
        if root == None: return res
        
        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = collections.deque()
            while curr_level:
                node = curr_level.popleft()
                # add the child nodes of the current level to the queue of the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # The current level is finished and its last element is the rightmost one
            res.append(node.val)
        return res
    
    
        # Another Optimal Solution
        res = []
        q = collections.deque([root])
        
        while q:
            right_side = None
            q_len = len(q)
            
            for i in range(q_len):
                node = q.popleft()
                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)
            if right_side:
                res.append(right_side.val)
        
        return res
        
    
    '''
        Explanation:
            - Edge case: Some nodes on the left/right subtree might not be blocked by nodes. In this case, we add those nodes into the result array
            - For each level of the tree, we want the rightmost node
            
            
            TC - O(n) where n is the number of nodes visited
            SC - O(d) where d is the diameter of the tree. The last level could take up to n/2 tree nodes in the case of a complete binary tree
    '''