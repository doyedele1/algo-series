'''
    Explanation: Using SortedDict - Balanced BST
        NOTE: Since there's no reverse SortedDict in Python, we will negate the scores before adding to the SortedDict so that the inorder traversal would give us the scores in descending order
        - Initialize a hashmap: key - playerId, value - score
        - Initialize a sorted map. key - score, value - number of players that have that score
        
        - addScore()
            - Note old score for the player
            - Update the old score in the sorted map. If the value is 0, remove the score entry
            - Update the dictionary with the new player score
            - Add the updated value to the sorted map as well as incrementing the value by 1. i.e. one more player has this score
            - If player doesn't exist, initialize score to score
                    
        - top() 
            - Loop over all the keys in the sorted map. Since the sorted map is a BST, then an inorder traversal of the keys would return the scores in a sorted order.
                - Pick the first k values
                    - For each key, multiply (key * value) and add it to the total sum
                    - Reduce the counter counting down to k by value
        - reset()
            - Note the old score for the player
            - Update the value of old score in the sorted map. If the value is 0, remove the score entry
            - Delete the entry containing the playerId
'''

from collections import defaultdict
from sortedcontainers import SortedDict

class Leaderboard:
    def __init__(self):
        self.playersToScores = {}
        self.sortedScores = SortedDict()
        
    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.playersToScores:
            self.playersToScores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        
        else:
            oldScore = self.playersToScores[playerId]
            value = self.sortedScores.get(-oldScore)
            
            if value == 1: del self.sortedScores[-oldScore]
            else: self.sortedScores[-oldScore] = value - 1
            
            newScore = oldScore + score
            self.playersToScores[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1

    def top(self, K: int) -> int:
        count, res = 0, 0
        
        for key, value in self.sortedScores.items():
            times = self.sortedScores.get(key)
            for _ in range(times):
                res += -key
                count += 1
                if count == K: break
            if count == K: break
                
        return res
        
    def reset(self, playerId: int) -> None:
        oldScore = self.playersToScores[playerId]
        if self.sortedScores[-oldScore] == 1: del self.sortedScores[-oldScore]
        else: self.sortedScores[-oldScore] -= 1
        del self.playersToScores[playerId]