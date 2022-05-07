# alphanumeric characters - A to Z, a to z, 0 to 9

# TC: O(n), SC: O(n) [newStr and the reveresed newStr space]
class Solution1:
    def checkAlphanumeric(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9'))
    
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newStr = ""
        for char in s:
            if self.checkAlphanumeric(char):
                newStr += char
        return newStr == newStr[::-1]

# TC: O(n) where n is the length of the input string, SC: O(1)
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            while not self.checkAlphanumeric(s[left]) and left < right: # left < right - the left pointer doesn't pass the right pointer and it doesn't go out of bounds
                left += 1
            while not self.checkAlphanumeric(s[right]) and left < right:
                right -= 1
            if s[left].lower() != s[right].lower(): return False
            left += 1
            right -= 1
        return True