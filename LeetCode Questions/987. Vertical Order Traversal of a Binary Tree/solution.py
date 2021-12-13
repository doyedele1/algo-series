# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root == None: return res
        cache = {}
        self.min_col = 0
        self.max_col = 0
        
        def dfs(node, row, col):
            if node == None: return None
            if col in cache: cache[col].append([row, node.val])
            else: cache[col] = [[row, node.val]]
            self.min_col = min(self.min_col, col)
            self.max_col = max(self.max_col, col)
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
            
        for c in range(self.min_col, self.max_col + 1):
            col = sorted(cache[c], key = lambda i: (i[0], i[1]))
            col_sorted = []
            for p in col:
                col_sorted.append(p[1])
            res.append(col_sorted)
        
        return res
        
        
        '''
            Explanation:
                - We will use a dfs preorder traversal to traverse the tree
                    - dfs(node, row, col)
                - We will initialize an empty cache that stores the column of the node as key and the row and value of the node as value. Key-value pair
                    - If the column is not in the cache, we will add it to the cache
                    - If the column is in the cache, we will append the row and value of the node to the cache of specific key (or column)
                - After the dfs helper function terminates, we will need to get the min_column and max_column from the cache that was created
        '''