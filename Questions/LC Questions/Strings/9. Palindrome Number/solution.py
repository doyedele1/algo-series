class Solution1:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        reversed_str = ""
        
        for i in range(len(s) - 1, -1, -1):
            reversed_str += s[i]
        
        return reversed_str == s

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        rev_x = self.reverse(x)
        return x == rev_x

    def reverse(self, num):
        res = 0

        while num != 0:
            res = res * 10 + num % 10
            num //= 10
            
        return res

class Solution3:
    def isPalindrome(self, x: int) -> bool:
