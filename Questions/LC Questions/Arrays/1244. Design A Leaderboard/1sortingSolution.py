'''
    Explanation I: Sorting
        - addScore() - Create a hashmap that stores playerId to score
            - TC: O(1)
        - top() - Store the values of the hashmap in a scores array
                - Sort the scores array
                - Loop through the scores array and get the first k scores and add the scores to your result
                - TC: O(nlogn)
        - reset() - Pop the playerId from the hashmap
            - TC: O(1)
            
        - SC: O(n) used by the hashmap and the scores array
    
    Explanation II: Using most_common() method in Collections Counter
        - addScore() - TC: O(1)
        - top() - Counter() returns a dictionary which is unordered
                - most_common() returns the sorted dictionary based on the count specified
                - TC: O(nlogK) where n is the number of players
        - reset() - TC: O(1)
        
        - SC: O(n) used by the counter
'''

from collections import Counter, defaultdict

class Leaderboard1:
    def __init__(self):
        # map: key: playerId, value: score
        self.playersToScores = defaultdict(int)
        
    def addScore(self, playerId: int, score: int) -> None:
        self.playersToScores[playerId] += score

    def top(self, K: int) -> int:
        scores = []
        
        for key in self.playersToScores:
            scores.append(self.playersToScores[key])
        scores.sort(reverse=True) # sorts scores in descending order
        
        res, i = 0, 0
        while i < K:
            res += scores[i]
            i += 1
        return res
        
    def reset(self, playerId: int) -> None:
        self.playersToScores.pop(playerId)

class Leaderboard2:
    def __init__(self):
        self.playersToScores = Counter()
        
    def addScore(self, playerId: int, score: int) -> None:
        self.playersToScores[playerId] += score

    def top(self, K: int) -> int:
        return sum(map(lambda x: x[1], self.playersToScores.most_common(K)))
        
    def reset(self, playerId: int) -> None:
        self.playersToScores.pop(playerId)
        
# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)