# alphanumeric characters - A to Z, a to z, 0 to 9

# TC - O(n), SC - O(n) [newStr and the reveresed newStr space]
class Solution:
    def checkAlphanumeric(self, char):
        if (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 48 and ord(char) <= 57): return True
        return False
    
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newStr = ""
        for i in s:
            if self.checkAlphanumeric(i):
                newStr += i
        return newStr == newStr[::-1]

# Another solution
def isPalindrome(s):
    s = s.lower()
    new_str = ''
    for i in s:
        if i.isalnum():
            new_str += i
    
    i = 0
    j = len(new_str) - 1

    while (i < j):
        if(new_str[i] != new_str[j]):
            return False
        i += 1
        j -= 1

    return True

# TC: O(n) where n is the length of the string, SC - O(1)
class Solution3:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        while i < j:
            while not self.checkAlphanumeric(s[i]) and i < j:
                i += 1
            while not self.checkAlphanumeric(s[j]) and i < j:
                j -= 1
            if s[i] == s[j] or s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else: return False
        return True

# print(valid_palindrome("level"))
# print(valid_palindrome("algorithm"))
# print(valid_palindrome("A man, a plan, a canal: Panama."))
# print(valid_palindrome("0P"))