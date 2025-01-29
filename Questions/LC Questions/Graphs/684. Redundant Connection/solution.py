'''
    Explanation: Disjoint Set / Union Find
        * A redundant edge is anything that is part of the cycle

        Example:
        edges = [[1,3],[1,2],[3,4],[1,4]]

        We create a dsuf of length n + 1
         0   1   2   3   4
        [-1, -1, -1, -1, -1]

        First iteration: [1,3]
        What is the absolute parent of 1? It is 1 itself because dsuf[1] = -1
        What is the absolute parent of 3? It is 3 itself because dsuf[3] = -1
        Since the absolute parents are different, that means they belong to two different sets and we can make 1 point to 3
        dsuf = [-1, 3, -1, -1, -1]

        Second iteration: [1,2]
        What is the absolute parent of 1? It is 3 because dsuf[1] = 3
        What is the absolute parent of 2? It is 2 itself because dsuf[2] = -1
        Since the absolute parents are different, that means they belong to two different sets and we can make 2 point to 3
        dsuf = [-1, 3, 3, -1, -1]

        Third iteration: [3,4]
        What is the absolute parent of 3? It is 3 itself because dsuf[3] = -1
        What is the absolute parent of 4? It is 4 itself because dsuf[4] = -1
        Since the absolute parents are different, that means they belong to two different sets and we can make 3 point to 4
        dsuf = [-1, 3, 3, 4, -1]

        Fourth iteration: [1,4]
        What is the absolute parent of 1? It is 4 because dsuf[dsuf[1]] = dsuf[3] = 4
        What is the absolute parent of 4? It is 4 itself because dsuf[4] = -1
        Since the absolute parents are the same, that means we found the redundant edge and we can return that edge

        TC: O(E A(V)) where A(V) is the inverse Ackermann function which is used to find by path compression
        Since E = V, TC: O(V A(V))
        A(V) can be so small and reach 1, hence TC: O(V)

        * A(V) = 4 for N = 10^18

        SC: O(V)
'''

from typing import List

class Solution:
    def find(self, dsuf, v):
        if dsuf[v] == -1:
            return v
        dsuf[v] = self.find(dsuf, dsuf[v]) # Path Compression
        return dsuf[v]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsuf = [-1] * (n + 1)

        for edge in edges:
            parent_a = self.find(dsuf, edge[0])
            parent_b = self.find(dsuf, edge[1])

            if parent_a == parent_b:
                return edge
            else:
                dsuf[parent_a] = parent_b
            
        return [0, 0]