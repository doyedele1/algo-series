from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        
        def dfs(currNode, path):
            if currNode == target: res.append(path)
            
            for nextNode in graph[currNode]:
                dfs(nextNode, path + [nextNode])
        
        dfs(0, [0])
        return res