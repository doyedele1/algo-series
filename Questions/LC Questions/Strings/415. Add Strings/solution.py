# Brute-force solution
class Solution1:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))

# Another solution - TC - O(max(n,m)), SC - O(max(n,m))
class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1) - 1, len(num2) - 1
        carry = 0
        res = ""
        
        while m >=0 or n >= 0:
            i, j = 0, 0
            if m >= 0:
                i = ord(num1[m]) - ord('0') # 0 --> 48
                m -= 1
            if n >= 0:
                j = ord(num2[n]) - ord('0')
                n -= 1
            temp = (i + j + carry) % 10
            if temp > 9:
                carry = 1
            else: carry = 0
            res += str(temp)
        
        if carry == 1: res += "1"
        return res