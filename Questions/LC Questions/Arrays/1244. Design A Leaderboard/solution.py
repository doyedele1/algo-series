'''
    Explanation I: Using most_common() method in Collections Counter
        - TC: 
            - addScore() - O(1)
            - top() - O(n log K) where n is the number of players
            - reset() - O(1)
        - SC: O(n)
        
    Explanation II: Using a heap
'''

from collections import Counter, defaultdict
import heapq

class Leaderboard1:
    def __init__(self):
        self.counter = Counter()
        
    def addScore(self, playerId: int, score: int) -> None:
        self.counter[playerId] += score

    def top(self, K: int) -> int:
        return sum(map(lambda x: x[1], self.counter.most_common(K)))
        
    def reset(self, playerId: int) -> None:
        self.counter[playerId] = 0

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
        
# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)