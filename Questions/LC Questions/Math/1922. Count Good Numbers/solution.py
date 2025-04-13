'''
    Explanation:
        If n = 1, we know that we can only have 5 options (from even numbers)
        If n = 2, we know that we can have 5 options (from even numbers) and 4 options (from odd numbers), making it 20

        So that means,
        even pattern = 5, 25, 125, ....
        odd pattern = 4, 16, 64, ....

        Using the patterns, we can conclude that:
        For even, expression = 5 ^ (n - n/2)
        For odd, expression = 4 ^ (n/2)

        With this, we can use binary exponentiation, to find the values of the two expressions in O(logn) time

        TC: O(logn)
        SC: O(1)
'''

class Solution:
    MOD = 10**9 + 7

    def binaryExponentiation(self, a: int, b: int) -> int:
        res = 1

        while b > 0:
            if b & 1:
                res = (res * a) % self.MOD
            a = (a * a) % self.MOD
            b //= 2
        return res

    def countGoodNumbers(self, n: int) -> int:
        return (self.binaryExponentiation(4, n // 2) * self.binaryExponentiation(5, n - n // 2)) % self.MOD