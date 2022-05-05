'''
    Explanation:
        - Use a hashmap
            key - the card value
            value - 
            
        - TC: O(n), SC: O(1)
'''


from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hashMap  = {}
        ans = float("inf")
        
        for currentIndex, card in enumerate(cards):
            if card not in hashMap: 
                hashMap[card] = currentIndex
            else:
                ans = min(ans, currentIndex - hashMap[card] + 1)
                hashMap[card] = currentIndex
                
        if ans == float('inf'): return -1
        else: return ans