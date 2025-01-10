'''
    Explanation:
        Three steps
        1. Get the frequency count of words2
        2. Only get the maximum frequency of every character in words2. For example, [ee, o, eeeoo] should be e:3, o:2
        3. Check every word in words1 and check if they are universal

    TC: O(ma + nb) where m is the length of words1 and n is the length of words2. 
    a is the average length of a word in words1 and b is the average length of a word in words2

    SC: O(1)
'''
from typing import List

class Solution:
    def getFreqCount(self, word):
        freq = [0] * 26
        for char in word:
            freq[ord(char) - ord('a')] += 1
        return freq

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2_max_freq = [0] * 26

        for word in words2:
            for i, count in enumerate(self.getFreqCount(word)):
                words2_max_freq[i] = max(words2_max_freq[i], count)
        
        res = []
        for word in words1:
            if(all(x >= y for x, y in zip(self.getFreqCount(word), words2_max_freq))):
                res.append(word)
        return res