# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
   
from collections import deque
from typing import List

# DFS
class Solution1:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nested_list, depth):
            res = 0
            for item in nested_list:
                if item.isInteger():
                    res += item.getInteger() * depth
                else:
                    res += dfs(item.getList(), depth + 1)
            return res
        
        return dfs(nestedList, 1)

# BFS
class Solution2:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        q = deque(nestedList)
        res, depth = 0, 1

        while q:
            for _ in range(len(q)):
                item = q.popleft()

                if item.isInteger():
                    res += item.getInteger() * depth
                else:
                    for elem in item.getList():
                        q.append(elem)
            depth += 1
        return res