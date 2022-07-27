'''
    Explanation II: Using a heap
'''

from collections import defaultdict
import heapq

class Leaderboard:
    def __init__(self):
        # map: key: playerId, value: score
        self.playersToScores = defaultdict(int)
        
    def addScore(self, playerId: int, score: int) -> None:
        self.playersToScores[playerId] += score

    def top(self, K: int) -> int:
        return sum(heapq.nlargest(K, self.playersToScores.values()))
        
    def reset(self, playerId: int) -> None:
        del self.playersToScores[playerId]