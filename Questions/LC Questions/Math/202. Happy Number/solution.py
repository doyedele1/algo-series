'''
    Explanation I: Using hash set to store seen numbers
        - n = 19 --> 82 --> 68 --> 100 --> 1
        n // 10 = firstDigit
        n % 10 = lastDigit
        
        - n = 2 --> 4 --> 16 --> 37 --> 58 --> 89 --> 145 --> 42 --> 20 --> 4
        Since we've seen 4 before, then we know that the number is not happy.
        
        - TC: O(log n) - finding the sum square for a given number has a cost of O(logn) because we are processing each digit in the number
        - SC: O(log n) - depends on what numbers are in the hash set. For n > 243, the most space will be taken by n itself

    Explanation I: Using linked list cycle idea
        - TC: O(log n)
        - SC: O(1)
'''

class Solution1:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            res = 0
            while n > 0:
                digit = n % 10
                res += digit ** 2
                n //= 10
            return res
        
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = sumOfSquares(n)
            
        return n == 1

class Solution2:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            res = 0
            while n > 0:
                digit = n % 10
                res += digit ** 2
                n //= 10
            return res
        
        slow = n
        fast = sumOfSquares(n)
        
        while fast != 1 and slow != fast:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))
            
        return fast == 1