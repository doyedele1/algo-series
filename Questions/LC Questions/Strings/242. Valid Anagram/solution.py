'''
    Explanation: 
        TC - solutions 2 to 4 --> O(s + t) where s and t are the lengths of the strings s and t
'''

from collections import Counter

class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        dictS, dictT = {}, {}
        
        for i in range(len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i], 0) # If s[i] doesn't exist, we return value to be 0
            dictT[t[i]] = 1 + dictT.get(t[i], 0) # If t[i] doesn't exist, we return value to be 0
        
        for char in dictS:
            if dictS[char] != dictT.get(char, 0):
                return False
        return True

class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
            
        dictS = {}
        
        for i in s:
            if i in dictS: dictS[i] += 1
            else: dictS[i] = 1
                
        for x in t:
            if x in dictS: dictS[x] -= 1
            else: return False
            
        for c in dictS:
            if dictS[c] != 0: return False
        return True

class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# print(isAnagram("cat", "tac")) # return True
# print(isAnagram("listen", "silent")) # return True
# print(isAnagram("program", "function")) # return False