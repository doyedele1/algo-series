class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqCount = {}
        
        for char in s:
            if(char in freqCount):
                freqCount[char] += 1
            else:
                freqCount[char] = 1
        
        for i in range(len(s)):
            if(freqCount[s[i]] == 1):
                return i
        return -1