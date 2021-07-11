# TC - O(2n), SC - O(n)
def valid_palindrome1(s):
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
def valid_palindrome(s):
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


def check_alphanumeric(self, c):
    if (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 48 and ord(c) <= 57):
        return True
    return False

def isPalindrome(self, s: str) -> bool:
    i = 0
    j = len(s) - 1

    while (i < j):
        while not self.check_alphanumeric(s[i]) and i < j:
            i += 1
        while not self.check_alphanumeric(s[j]) and i < j:
            j -= 1
        if s[i] == s[j] or s[i].lower() == s[j].lower():
            i += 1
            j -= 1
        else:
            return False
    return True
        


# print(valid_palindrome("level"))
# print(valid_palindrome("algorithm"))
# print(valid_palindrome("A man, a plan, a canal: Panama."))
# print(valid_palindrome("0P"))