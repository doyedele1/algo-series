'''
    Explanation:
        [3,4,2,3,4,7]
        - Use a hashmap
            key - the card value
            value - index occurence of the card value
        
        hashamp = {}, ans = Infinity
        
        hashmap = {3: 0}
        
        hashmap = {3: 0, 4: 1}
        
        hashmap = {3: 0, 4: 1, 2: 2}
        
        3 is in the hashmap, ans = min(Infinity and 3-0+1) = 4
        hashmap = {3: 3, 4: 1, 2: 2}

        4 is in the hashmap, ans = min(4, 4-1+1) = 4
        hashmap = {3: 3, 4: 4, 2: 2}

        hashmap = {3: 3, 4: 4, 2: 2, 7: 5}
            
        TC: O(n), SC: O(n)
'''


from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hashMap  = {}
        res = float("inf")
        
        for currentIndex, card in enumerate(cards):
            if card not in hashMap: 
                hashMap[card] = currentIndex
            else:
                res = min(res, currentIndex - hashMap[card] + 1)
                hashMap[card] = currentIndex
                
        if res == float('inf'): return -1 # We've not found matching cards
        else: return res