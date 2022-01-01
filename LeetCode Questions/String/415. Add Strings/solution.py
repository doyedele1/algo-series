class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Brute-force solution
        return str(int(num1) + int(num2))
    
        # Another solution - TC - O(max(n,m)), SC - O(max(n,m))
        n, m = len(num1), len(num2)
        a, b = n-1, m-1
        carry = 0
        res = ""
        
        while a >=0 or b >= 0:
            i,j = 0, 0
            if a >= 0:
                i = ord(nums1[a])-48
                a -= 1
            if b >= 0:
                j = ord(num2[b])-48
                b-=1
            temp = i+j+carry
            if temp > 9:
                carry = 1
            else: carry = 0
            res = str(temp[-1]) + res
        
        if carry: res = "1" + res
        return res