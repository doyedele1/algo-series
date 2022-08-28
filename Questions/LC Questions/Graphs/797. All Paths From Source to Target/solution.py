'''
    Explanation:
        Input: [[1,2],[3],[3],[]]
        Output: [[0,1,3],[0,2,3]]
    
                            f(0, 3)
                        /             \
                    f(1,3)          f(2,3)
                        |              |
                    f(3,3)           f(3,3)
                    
    - TC: O(n * 2^n)
    - SC: O(n)
'''

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        
        def dfs(path, currNode):
            if currNode == target: res.append(path + [currNode])
            
            else:
                for nextNode in graph[currNode]:
                    dfs(path + [currNode], nextNode)
        
        dfs([], 0)
        return res