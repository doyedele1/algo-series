from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashMap = {}

        for idx, word in enumerate(list1):
            hashMap[word] = idx
        
        res = []
        minSum = float("inf")

        for idx, word in enumerate(list2):
            if word in hashMap:
                sumOfIndexes = idx + hashMap[word]
                if sumOfIndexes < minSum:
                    minSum = sumOfIndexes
                    res = [] # we clear our res array as soon as we see another word with lower index sum
                    res.append(word)
                elif sumOfIndexes == minSum:
                    res.append(word)
        return res