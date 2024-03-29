'''
    Explanation:
        - Hashmap of columnTable
            key = column
            value = list of node.value

        - Initial queue = [(root, 0)]
       
        SC: O(n) where n is the number of nodes in the tree
            Hash table: We used a hash table to group nodes on the same column. The values would consume O(n) memory
            Queue: In a full binary tree where parent node has either two or no children, the maximum number of nodes at a level is (n+1)/2 and the queue can hold no more two levels of nodes
                (n+1)/2 * 2 = O(n+1), amortized is O(n)
            Result: Reordering the hash table and creating an array from it is O(n)
'''

from typing import List, Optional
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC: O(nlogn) when the binary tree is extremely imbalanced- each node has only left child node, SC: O(n)
class Solution1:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        columnTable = defaultdict(list)
        q = deque([(root, 0)])

        while q:
            node, column = q.popleft()

            if node:
                columnTable[column].append(node.val)

                q.append((node.left, column - 1))
                q.append((node.right, column + 1))
        
        return [columnTable[x] for x in sorted(columnTable.keys())]

# This solution works because there won't be any missing column index in the given range of minColumn and maxColumn
# TC: O(n), SC: O(n)
class Solution2:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        
        columnTable = defaultdict(list)
        minColumn, maxColumn = 0, 0
        q = deque([(root,0)])

        while q:
            node, column = q.popleft()

            if node:
                columnTable[column].append(node.val)
                minColumn = min(minColumn, column)
                maxColumn = max(maxColumn, column)
    
                q.append((node.left, column - 1))
                q.append((node.right, column + 1))
            
        return [columnTable[x] for x in range(minColumn, maxColumn + 1)]