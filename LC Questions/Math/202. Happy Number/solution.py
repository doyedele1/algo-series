'''
    Explanation:
        - n = 19 --> 82 --> 68 --> 100 --> 1
        n // 10 = firstDigit
        n % 10 = lastDigit
        
        - n = 2 --> 4 --> 16 --> 37 --> 58 --> 89 --> 145 --> 42 --> 20 --> 4
        Since we've seen 4 before, then we know that the number is not happy.
        
        Time Complexity: O(log n) - finding the sum square for a given number has a cost of O(logn) because we are processing each digit in the number, and the number of digits in a number is given by (log n): For n > 243, O(243 * 3 + log n + log log n + ....) = O(log n)
        Space: O(log n) - depends on what numbers are in the hash set. For n > 243, the most space will be taken by n itself
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        checkCycle = set()
        
        while self.squareSum(n) not in checkCycle and n != 1:
            checkCycle.add(n)
            n = self.squareSum(n)
        return n == 1
        
    def squareSum(self, n):
        resultNumber = 0
        while n > 0:
            lastDigit = n % 10
            resultNumber = resultNumber + (lastDigit ** 2)
            n //= 10
        return resultNumber