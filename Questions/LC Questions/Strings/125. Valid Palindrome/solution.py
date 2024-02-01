# alphanumeric characters - A to Z, a to z, 0 to 9

# TC: O(n), SC: O(n) [newStr and the reveresed newStr space]
class Solution1:   
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(c):
            return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
        
        s = s.lower()
        newStr = ""

        for c in s:
            if isAlphaNum(c):
                newStr += c
        return newStr == newStr[::-1]

# TC: O(n), SC: O(1)
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        def isAlphaNum(c):
            return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))   

        while i < j:
            # skip if it is a special character
            while i < j and not isAlphaNum(s[i]):
                i += 1
            
            # skip if it is a special character
            while j > i and not isAlphaNum(s[j]):
                j -= 1

            # if characters are both ends are not the same, just return False
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True