'''
    Explanation III:
        1221
        - Reverse the last half of the input number. i.e. from 21 to 12
            - First iteration:
                res = 0, res = 1, x = 122
            - Second iteration:
                res = 1, res = 12, x = 12
        - We reverse the half and stop the loop when the original number x is less than or equal to reversed number res
        - When the length of the number is odd, we get rid of the middle digit by doing res // 10
            12321
                - First iteration:
                    res = 0, res = 1, x = 1232
                - Second iteration:
                    res = 1, res = 12, x = 123
                - Third iteration:
                    res = 12, res = 123, x = 12
                - We stop the loop since x < 123. We can then ignore the middle digit "3", by doing 123 // 10 = 12 and it's equal to x = 12
        - When the length of the number is even, we can always get x == res
        
        TC: O(log n) since we divide the input number x by 10 for every iteration
        SC: O(1)
'''

class Solution1:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        reversed_str = ""
        
        for i in range(len(s) - 1, -1, -1):
            reversed_str += s[i]
        
        return reversed_str == s

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        # edge cases - negative, x is not equal to 0 and x ends with 0
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
        # edge cases - negative, x is not equal to 0 and x ends with 0
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        res = 0

        while x > res:
            res = res * 10 + x % 10
            x //= 10
            
        return x == res or x == res // 10
