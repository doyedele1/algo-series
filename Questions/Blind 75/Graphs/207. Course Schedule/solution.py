from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course in pre_map
        pre_map = { i: [] for i in range(numCourses) }
        for course, pre in prerequisites:
            pre_map[course].append(pre)
    
        # visit_set that includes all courses along the curr DFS path
        visit_set = set()
        def dfs(course):
            # when we detect a loop
            if course in visit_set:
                return False
            
            # if preq is empty list
            if pre_map[course] == []:
                return True
            
            visit_set.add(course)
            for pre in pre_map[course]:
                # if one of the courses can't be completed
                if not dfs(pre):
                    return False
            visit_set.remove(course)
            # when we run DFS again
            pre_map[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        
    '''
        Explanation:
        [[0,1], [0,2], [1,3], [1,4], [3,4]]
            - Using DFS
            - Create a picture of the pair representing as edges. [0,1] means 0 --> 1
            - The next question to ask is for each of the nodes, can we complete this course or not?
                - If there are no prerequisites for the base case
            - Adjacency list. Hashmaps to represent the prerequisites
                i.e. course = 0, pre = [1,2] and so on
            - We run DFS on the order of [0, n-1]
                - Run DFS recursively on the first neighbors
                - Course 4 can be completed because it has an empty prerequisite list, so we can have a check mark
                - Course 3 had one prerequisite and we were able to complete that. From the prerequisite list for 3, we can remove 4 and have an empty list
            - When 0 has an empty list of prerequisite, we know 0 can also be completed
            - Since we were able to complete every single course, then we can return true
            
            
            - TC - O(n + p) where n is the number of nodes in the graph and p is the number of prerequisites
            - SC - O(|E| + |V|) for the graph we built. The pre_map and visited_set consume 2 |V| space. The recursive call stack in the worst case would pile up |V| times. Hence the SC - O(|E| + 4|V|) = O(|E| + |V|)
            
            - Detecting a loop
                - We will use a set that will contain the list of courses we visit along our DFS
                - [0,1], [1,2], [2,0] --> visitSet (course) = [0,1,2]
                - For the course 2, we are going back to 0, but since 0 is in the visitSet, we can easily return False
    ''' 