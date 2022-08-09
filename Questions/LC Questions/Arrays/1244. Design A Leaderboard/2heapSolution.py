'''
    Explanation I: Min heap
        - top() - Store the values of the hashmap in a min heap
                - Loop over the first k values in the hashmap and add them to the heap
                - For the rest of n-k values, add a new value to the heap and pop the smallest value from the heap to maintain the heap size to k.
                - Since the remaining values in the heap will be the largest k values left, then add up all the corresponding values.
                - TC: O(k) + O(nlogk) = O(nlogk). O(k) to construct the first k elements in the heap and then to add and remove the rest of the n-k elements, we perform (n-k)logk.
        
    Explanation II: Using nlargest() method in heapq. The method returns the largest k elements in the heap
        - top(). TC: O(nlogk)
        - SC: O(n+k). n for the playersToScores dictionary and k for the heap
'''

from collections import defaultdict
import heapq

class Leaderboard1:
    def __init__(self):
        # map: key: playerId, value: score
        self.playersToScores = defaultdict(int)
        
    def addScore(self, playerId: int, score: int) -> None:
        self.playersToScores[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        
        for score in self.playersToScores.values():
            heapq.heappush(heap, score)
            if len(heap) > K: heapq.heappop(heap)
        
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res
        
    def reset(self, playerId: int) -> None:
        del self.playersToScores[playerId]

class Leaderboard2:
    def __init__(self):
        # map: key: playerId, value: score
        self.playersToScores = defaultdict(int)
        
    def addScore(self, playerId: int, score: int) -> None:
        self.playersToScores[playerId] += score

    def top(self, K: int) -> int:
        return sum(heapq.nlargest(K, self.playersToScores.values()))
        
    def reset(self, playerId: int) -> None:
        del self.playersToScores[playerId]