from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1
        
        def dfs(node, path, output):
            if node == end: res.append(path)
            
            for nxt in graph[node]:
                dfs(nxt, path + [nxt], res)
        
        res = []
        dfs(0, [0], res)
        return res