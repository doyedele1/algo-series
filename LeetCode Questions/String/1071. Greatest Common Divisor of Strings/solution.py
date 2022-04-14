'''
    Explanation: divisor, common divisor, greatest common divisor
        Input: str1 = "ABABAB", str2 = "ABAB", output = "AB"
        Case 1: str1 + str2 == str2 + str1. If not equal, return ""
        Case 2: str1 == str2, return str1 or str2
        Case 3: str1 = "ABCABCABCABC", str2 = "ABCABC", remove continuously str2 from str1 to get common divisor = "ABCABC"
        Case 4: str1 = "AB AB AB AB AB AB AB AB AB", str2 = "ABAB", output = "AB"
        
        TC: O(n), SC: O(n)
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: return ""
        elif str1 == str2: return str1
        elif len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        else: return self.gcdOfStrings(str2[len(str1):], str1)