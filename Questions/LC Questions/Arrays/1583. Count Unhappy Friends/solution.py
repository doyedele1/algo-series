'''
    preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
    pairs = [[0, 1], [2, 3]]

    preferredDict = {
        0: {},
        1: {3,2},
        2: {},
        3: {1}
    }

    Then use the x prefers u over y and u prefers x over v for the nested loop

    TC: O(n^2). For each of the n people, we will walk through (up to) n-1 entries in their preferences
    SC: O(n^2). We will have n entries in the dictionary we create, and each one of those can have (up to) n-1 entries in the set
'''
from typing import List

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        preferredDict = {}

        for x, y in pairs:
            preferredDict[x] = set(preferences[x][:preferences[x].index(y)]) # arr.index(a) returns the index of value a in arr
            preferredDict[y] = set(preferences[y][:preferences[y].index(x)])

        res = 0
        for x in preferredDict:
            for y in preferredDict[x]:
                if x in preferredDict[y]:
                    res += 1
                    break
        return res