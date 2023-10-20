'''
    Explanation:
        - First, talk about the case where you don't half the prices of non-adjacent prices

        - Important inputs
            n = number of nodes
            edges.length = n - 1
            edgeA >= 0, edgeB <= n - 1
            tripA >= 0, tripB <= n - 1
            price.length = n

        - Important questions
            - Is price[i] an even integer? Answer should be yes
            - How big can a price[i] be? Answer should be 1 - 1000
            - How big can the trips array be? Answer should be 100

        - Use BFS to get the path and frequency of each node
            - path = [0,1,3], [2,1], [2,1,3]
            - freq = {0: 1, 1: 3, 3: 2, 2: 2}
        
        - Use DP to recursively run through the tree
            - dp(node, parent, shouldHalf)
            - Use memoization to cache your calculated values from the recursive function
'''


import collections
from typing import List

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:

        def bfs(src, dest):
            q = collections.deque([(src, [src])])
            visited = set()

            while q:
                node, path = q.popleft()

                if node == dest:
                    return path
                
                visited.add(node)
                for nei in graph[node]:
                    if nei not in visited:
                        q.append((nei, path + [nei]))

        graph = collections.defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        freq = collections.defaultdict(int)
        for src, dest in trips:
            path = bfs(src, dest)
            for node in path:
                freq[node] += 1
            print(freq)

        def dp(node, parent, shouldHalf):
            if (node, parent, shouldHalf) in cache:
                return cache[(node, parent, shouldHalf)]
            if shouldHalf:
                cost = freq[node] * (price[node] // 2)
            else:
                cost = freq[node] * price[node]
            
            for nei in graph[node]:
                # so we don't go back to the parent node
                if nei != parent:
                    if shouldHalf:
                        neiCost = dp(nei, node, False)
                    else:
                        neiCost = min(dp(nei, node, False), dp(nei, node, True))
                    cost += neiCost
            
            cache[(node, parent, shouldHalf)] = cost
            return cost
        
        cost = float("inf")
        cache = {}
        for node in range(n):
            cost = min(cost, dp(node, None, False), dp(node, None, True))
        return cost