'''
    Explanation I: DFS Recursion (Backtracking)
        Input: [[1,2],[3],[3],[]]
        Output: [[0,1,3],[0,2,3]]
    
                            f(0, 3)
                        /             \
                    f(1,3)          f(2,3)
                      |                |
                    f(3,3)           f(3,3)
                    
        graph = [[1,2],[3],[3],[]]
        dfs(0, 3, [0])
        path = [0,1]
        dfs(1, 3, [0,1])
        path = [0,1,3]
        dfs(3, 3, [0,1,3])
        res = [[0,1,3]]

        path = [0]
        dfs(0, 3, [0])
        path = [0,2]
        dfs(2, 3, [0,2])
        path = [0,2,3]
        dfs(3, 3, [0,2,3])
        res = [[0,1,3], [0,2,3]]

        TC: O(n * 2^n)
        SC: O(n)

    Explanation II: DFS Iteration
        graph = [[1,2],[3],[3],[]]
        nodeMap = {
            0: [1,2]
            1: [3]
            2: [3]
            3: []    
        }

        res = []
        stack = [(0, [0])]

        node = 0, path = [0]
        stack = [(1, [0,1]), (2, [0,2])]

        node = 2, path = [0,2]
        stack = [(1, [0,1]), (3, [0,2,3])]

        node = 3, path = [0,2,3]
        stack = [(1, [0,1])]
        res = [[0,2,3]]

        node = 1, path = [0,1]
        stack = [(3, [0,1,3])]
        res = [[0,2,3], [0,1,3]]

        TC: O(E + K*V) where K is the number of paths (number of visits to the leaf/end node)
        SC: O(E + V)
'''

from typing import List

class Solution1:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []

        def dfs(node, end, path):
            if node == end:
                res.append(path.copy())
            for neighbour in graph[node]:
                path.append(neighbour)
                dfs(neighbour, end, path)
                path.pop()

        dfs(0, n - 1, [0])
        return res

class Solution2:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph: return []
        
        nodeMap = {}
        for i in range(len(graph)):
            nodeMap[i] = graph[i]
        
        res = []
        stack = [(0, [0])]
        
        while stack:
            node, path = stack.pop()
            
            if node == len(graph) - 1: 
                res.append(path)
            
            for neighbors in nodeMap[node]:
                stack.append((neighbors, path + [neighbors]))
        return res