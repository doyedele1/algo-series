from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = { c: [] for c in range(numCourses) }
        
        for course, pre in prerequisites:
            pre_map[course].append(pre)
            
            # A course has 3 possible states
            # visited --> course has been added to the output
            # visiting --> course is not added to output, but it is added to cycle
            # unvisited --> course has not been added to output or cycle
            
        res = []
        visit, cycle = set(), set()
        
        def dfs(course):
            if course in cycle: return False
            if course in visit: return True
            
            cycle.add(course)
            for pre in pre_map[course]:
                if not dfs(pre): return False
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True
            
        for course in range(numCourses):
            if not dfs(course): return []
        return res
        
'''
    Explanation - Topological Sort:
        - Return the ordering of courses
        - Starting at every node, we run dfs on the node
            - We create an adjacency list pre_map
            - We go through each node and look for the course that does not have any prerequisite after taking a path
                - If we find a course that does not have any prerequisite, we add it to the result, and we cross out that course so we never visit the node again
            - The topological sort is not unique
            - When we detect a cycle, we return an empty list

            TC - O(|E| + |V|) = O(p) + O(n)
'''