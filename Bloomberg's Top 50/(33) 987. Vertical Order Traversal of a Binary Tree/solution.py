'''           
    Explanation I:
        - We will use a dfs preorder traversal to traverse the tree
            - dfs(node, row, col)
            - Start traversal from the root
            - We will initialize an empty cache that stores the column of the node as key and the row and value of the node as value. Key-value pair
                - If the column is not in the cache, we will add it to the cache
                - If the column is in the cache, we will append the row and value of the node to the cache of specific key (or column)
            - We will keep track of the smallest and largest columns in the traversal
        - After the dfs helper function terminates, we will loop through from the min_column and max_column, we get the elements corresponding to each column in the cache
        - Since we have more than one value of column in the cache, we need to sort the values in the cache by row and then by value

        TC - O(n logn).
            - Traverse the input tree using dfs takes O(n) time
            - Sorting the cache takes O(n logn) time

        SC - O(n)
            - We have a cache that contains coordinates of each node. The size of the cache is O(n)
            - The DFS approach takes O(n) space in the recursion stack

    Explanation II: Efficient DFS
    Explanation III: Efficient BFS
'''


from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution1:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        cache = {}
        self.min_col = 0
        self.max_col = 0

        if root == None: return res
        
        def dfs(node, row, col):
            if node == None: return
            if col in cache: cache[col].append([row, node.val])
            else: cache[col] = [[row, node.val]]
            self.min_col = min(self.min_col, col)
            self.max_col = max(self.max_col, col)
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
            
        for c in range(self.min_col, self.max_col + 1):
            col = sorted(cache[c], key = lambda i: (i[0], i[1])) # sort by row and by values if row numbers are the same
            col_sorted = []
            for p in col:
                col_sorted.append(p[1])
            res.append(col_sorted)
        
        return res


class Solution2:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def DFS(node, row, column):
            if node is not None:
                nonlocal min_column, max_column
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        # step 1). DFS traversal
        DFS(root, 0, 0)

        # step 2). extract the values from the columnTable
        ret = []
        for col in range(min_column, max_column + 1):
            # sort first by 'row', then by 'value', in ascending order
            ret.append([val for row, val in sorted(columnTable[col])])

        return ret

class Solution3:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def BFS(root):
            nonlocal min_column, max_column
            queue = deque([(root, 0, 0)])

            while queue:
                node, row, column = queue.popleft()

                if node is not None:
                    columnTable[column].append((row, node.val))
                    min_column = min(min_column, column)
                    max_column = max(max_column, column)

                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        # step 1). BFS traversal
        BFS(root)

        # step 2). extract the values from the columnTable
        ret = []
        for col in range(min_column, max_column + 1):
            # sort first by 'row', then by 'value', in ascending order
            ret.append([val for row, val in sorted(columnTable[col])])

        return ret