from collections import defaultdict
from collections import deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for vertices, value in zip(equations, values):
            graph[vertices[0]].append([vertices[1], value])
            graph[vertices[1]].append([vertices[0], 1/value])

        def calculateProduct(query):
            letter1, letter2 = query

            if letter1 not in graph or letter2 not in graph: return -1.0

            q = deque([(letter1, 1.0)])
            visited = set()

            while q:
                letter, currProduct = q.popleft()

                if letter == letter2: return currProduct
                visited.add(letter)

                for neighbor, value in graph[letter]:
                    if neighbor not in visited:
                        q.append((neighbor, currProduct * value))
            return -1.0
    
        return [calculateProduct(q) for q in queries]