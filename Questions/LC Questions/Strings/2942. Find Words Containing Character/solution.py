from typing import List

# TC: O(nm) where m is the maximum length of a word, SC: O(1)
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n = len(words)
        res = []

        for i in range(n):
            word = words[i]
            if x in word:
                res.append(i)
        return res