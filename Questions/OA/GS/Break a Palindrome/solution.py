def breakPalindrome(palindromeStr):
    for i in range(len(palindromeStr) // 2):
        if palindromeStr[i] != 'a':
            return palindromeStr[:i] + 'a' + palindromeStr[i + 1:]
    
    return "IMPOSSIBLE"