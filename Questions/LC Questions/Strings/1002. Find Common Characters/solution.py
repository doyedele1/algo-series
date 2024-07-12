'''
    Explanation:
        ["bella", "label", "roller"]
        * If there is only one occurence of e in bella, that means there could be zero or one e in the other words

        commonCharacterCount = {b: 1, e: 1, l: 2, a: 1}
        bella   label   roller
        a: 1    a: 1    e: 1
        b: 1    b: 1    l: 2
        e: 1    e: 1    o: 1
        l: 2    l: 2    r: 2

        TC: O(n * k) where k is the length of the longest word
        SC: O(1)
'''

from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        N = len(words)
        res = []

        commonCharacterCount = Counter(words[0])

        for i in range(1, N):
            currentCharacterCount = Counter(words[i])

            for char in commonCharacterCount:
                commonCharacterCount[char] = min(commonCharacterCount[char], currentCharacterCount[char])

        for char in commonCharacterCount:
            for i in range(commonCharacterCount[char]):
                res.append(char)
        return res