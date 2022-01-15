




'''
    Explanation - Topological Sort:
        - Return the ordering of courses
        - Starting at every node, we run dfs on the node
            - We create an adjacency list pre_map
            - We go through each node and look for the course that does not have any prerequisite after taking a path
                - If we find a course that does not have any prerequisite, we add it to the result, and we cross out that course so we never visit the node again
            
'''