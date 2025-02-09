'''
    Explanation:
        We can't use an array to represent balls, because maximum length of limit is 10^9. And we know an array stores 4 bytes of data. Hence total space is 4 * 10^9 = 4GB

        We can use two hashmaps
        First hashmap: key = ball, value = color
        Second hashmap: key = color, value = frequency

        Dry run
        queries = [[1,4],[2,5],[1,3],[3,4], [4,5], [2,1]]

        [1,4]
        ball_color = {1:4}
        color_freq = {4:1}
        number of distinct colors = len(color_freq) = 1

        [2,5]
        ball_color = {1:4, 2:5}
        color_freq = {4:1, 5:1}
        number of distinct colors = len(color_freq) = 2

        [1,3]
        ball_color = {1:3, 2:5}
        color_freq = {5:1, 3:1}
        number of distinct colors = len(color_freq) = 2

        [3,4]
        ball_color = {1:3, 2:5, 3:4}
        color_freq = {5:1, 3:1, 4:1}
        number of distinct colors = len(color_freq) = 3

        [4,5]
        ball_color = {1:3, 2:5, 3:4, 4:5}
        color_freq = {5:2, 3:1, 4:1}
        number of distinct colors = len(color_freq) = 3

        [2,1]
        ball_color = {1:3, 2:1, 3:4, 4:5}
        color_freq = {5:1, 3:1, 4:1, 1:1}
        number of distinct colors = len(color_freq) = 4

        TC: O(Q) where Q is the size of queries
        SC: O(Q)
'''
from typing import List
from collections import defaultdict

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}
        color_freq = defaultdict(int)
        result = []

        for query in queries:
            ball, color = query[0], query[1]

            if ball in ball_color:
                prev_color = ball_color[ball]
                color_freq[prev_color] -= 1
                if not color_freq[prev_color]:
                    del color_freq[prev_color]
            
            ball_color[ball] = color
            color_freq[color] += 1

            result.append(len(color_freq))

        return result