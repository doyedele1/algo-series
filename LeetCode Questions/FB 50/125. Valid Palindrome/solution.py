# Naive solution: TC - O(2n), SC - O(n)
def isPalindrome1(s):
    s = s.lower()
    new_str = ''
    for i in s:
        if i.isalnum():
            new_str += i
    reversed_str = new_str[::-1]

    if (new_str == reversed_str):
        return True
    return False

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

# Another solution
class Solution:
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
        
        
    def checkAlphanumeric(self, char):
        if (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 48 and ord(char) <= 57):
            return True
        return False
    
    
    '''
        TC - O(n) where n is the length of the string
        SC - O(1)
    '''

# print(valid_palindrome("level"))
# print(valid_palindrome("algorithm"))
# print(valid_palindrome("A man, a plan, a canal: Panama."))
# print(valid_palindrome("0P"))