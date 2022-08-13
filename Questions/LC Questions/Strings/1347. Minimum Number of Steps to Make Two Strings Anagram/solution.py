'''
    Explanation: Using a hashmap
'''

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        dictS = dict()
        
        for char in s:
            if char in dictS: dictS[char] += 1
            else: dictS[char] = 1
        
        for char in t:
            if char in dictS and dictS[char] > 0:
                dictS[char] -= 1
            else: res += 1
        return res