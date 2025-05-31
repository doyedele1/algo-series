'''
    Explanation: Multisource BFS
        No need to build an adjacency list as it's been given from the input - edges

        Examples:
        1 -> 2 <- 0
             3
        node1 = 0, node2 = 1
        node1 (0) can only go from 0 to 2 to 3
        node2 (1) can only go from 1 to 2 to 3

        So, at 2, distance from (node1, node2) is (1, 1)
        At 3, distance from (node1, node2) is (2, 2)
        Maximum at 2 is 1
        Maximum at 3 is 2
        So pick the minimum between maximum at 2 and maximum at 3 which will be 1.

        Another example:
        0 -> 1 -> 2 -> 3 <- 6 <- 7
                       4
                       5
        node1 = 0, node2 = 7
        node1 (0) can only go from 0 to 1 to 2 to 3 to 4 to 5
        node2 (7) can only go from 7 to 6 to 3 to 4 to 5

        So, at 3, distance from (node1, node2) is (3, 2)
        At 4, distance from (node1, node2) is (4, 3)
        At 5, distance from (node1, node2) is (5, 4)
        Maximum at 3 is 3
        Maximum at 4 is 4
        Maximum at 5 is 5
        So pick the minimum between maximum at 3, maximum at 4 and maximum at 5 which will be 3

        Another example:
        0 -> 1 -> 2 -> 3
        node1 = 0, node2 = 2
        node1 (0) can only go from 0 to 1 to 2 to 3
        node2 (2) can only go from 2 to 3

        So, at 2, distance from (node1, node2) is (2, 0)
        At 3, distance from (node1, node2) is (3, 1)
        Maximum at 2 is 2
        Maximum at 3 is 3
        So pick the minimum between maximum at 2 and maximum at 3 which will be 2

        Another example:
        0 -> 1              3 -> 4
             2
        node1 = 0, node2 = 3
        node1 (0) can only go from 0 to 1 to 2
        node2 (3) can only go from 3 to 4

        So, at 0, distance from (node1, node2) is (0, -1)
        At 1, distance from (node1, node2) is (1, -1)
        At 2, distance from (node1, node2) is (2, -1)
        At 3, distance from (node1, node2) is (-1, 0)
        At 4, distance from (node1, node2) is (-1, 1)
        Note: -1 here represents that the node can't be reachable

        Since in the distances, we don't have both as non-negative (i.e. no common node), then we return -1

        With these observations, we can come up with two steps for our solution:
            Step 1: Find the distance for all the nodes from both nodes
            Step 2: Minimize the maximum meeting point distance
        
        Dry run:
            edges = [4, 4, 1, 1, 2, 4, 4, -1]

            We need a distance matrix of n by 2 and prefill that with -1
            We also need a queue and we can use (node, type) where type is the node_type (0 or 1)

            To then get our result, we need a minimum_meeting_distance and meeting_point

        TC: O(n)
        SC: O(n)
'''
from typing import List
from collections import deque

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist = [[-1, -1] for _ in range(n)]
        dist[node1][0] = 0
        dist[node2][1] = 0

        q = deque()
        q.append((node1, 0))
        q.append((node2, 1))

        while q:
            curr, typ = q.popleft()
            neighbor = edges[curr]
            if neighbor != -1 and dist[neighbor][typ] == -1:
                dist[neighbor][typ] = dist[curr][typ] + 1
                q.append((neighbor, typ))
        
        meeting_point = -1
        min_distance = float('inf')

        for i in range(n):
            if dist[i][0] != -1 and dist[i][1] != -1:
                curr_distance = max(dist[i][0], dist[i][1])
                if curr_distance < min_distance:
                    min_distance = curr_distance
                    meeting_point = i
        return meeting_point