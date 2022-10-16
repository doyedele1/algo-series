'''
    Explanation I: DFS Recursion
        Input: [[1,2],[3],[3],[]]
        Output: [[0,1,3],[0,2,3]]
    
                            f(0, 3)
                        /             \
                    f(1,3)          f(2,3)
                        |              |
                    f(3,3)           f(3,3)
                    
        - TC: O(n * 2^n)
        - SC: O(n)

    Explanation II: DFS Iteration
        - TC: O(E + K*V) where K is the number of paths (number of visits to the leaf/end node)
'''

from typing import List

class Solution1:
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
            
            if node == len(graph) - 1: res.append(path)
                
            for neighbors in nodeMap[node]:
                stack.append((neighbors, path + [neighbors]))
                '''
                    print(stack)   ==>  [(1, [0, 1])]
                                        [(1, [0, 1]), (2, [0, 2])]
                                        [(1, [0, 1]), (3, [0, 2, 3])]
                                        [(3, [0, 1, 3])]
                '''
        return res