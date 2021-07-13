class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while self.squareSum(n) not in seen:
            if self.squareSum(n) == 1:
                return True
            else:
                seen.add(self.squareSum(n))
                n = self.squareSum(n)
        return False
        
    def squareSum(self, n):
        res = 0
        
        while(n > 0):
            lastDigit = n % 10
            res = res + (lastDigit * lastDigit)
            n //= 10
        return res