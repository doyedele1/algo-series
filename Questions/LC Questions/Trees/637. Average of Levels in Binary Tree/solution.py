'''
    Explanation I: DFS
                                4
                        2               6
                    3       5               7
        - Create two dictionaries sum_of_each_level and count_of_each_level
        - At every level, use recursive dfs to get the sum and count of each level
            sum_of_each_level = [4, 8, 15]
            count_of_each_level = [1, 2, 3]
        - Then with the two dictionaries, calculate the averages

        TC: O(n) where n refers to the total number of nodes in a binary tree
        SC: O(h) where h os the height of the tree. O(h) because sum_of_each_level and count_of_each_level are of size h

    Explanation II: BFS
        - 
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sum_of_each_level = defaultdict(float)
        count_of_each_level = defaultdict(int)

        def dfs(node, height):
            if not node:
                return
            
            dfs(node.left, height + 1)
            dfs(node.right, height + 1)
            sum_of_each_level[height] += node.val
            count_of_each_level[height] += 1
        
        dfs(root, 0)

        return [sum_of_each_level[i] / count_of_each_level[i] for i in range(len(count_of_each_level))]

class Solution2:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque([root])

        if root == None:
            return res

        while q:
            level_sum = 0
            len_q = len(q)

            for _ in range(len_q):
                curr = q.popleft()

                level_sum += curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(level_sum/len_q)
        return res
