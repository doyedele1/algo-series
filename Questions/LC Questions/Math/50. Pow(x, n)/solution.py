'''
    Explanation I: Simple Solution
        To get pow(x, n), we can multiply x in n times.

        TC: O(n)

    Explanation II: Binary Exponentiation
        We can say that 2^8 = 4^4 = 16^2 = 256

        The idea: square the base and half the exponent

        Example:
        2^8 = 4^4
        4^4 = 16^2
        16^2 = 256^1 = 256

        2^9 = 2^4 * 2^4 * 2^1 (2^1 is an extra and we can save it somewhere)
        4^4 = 16^2
        16^2 = 256^1 = 256
        Result = 256 * 2^1 = 512

        TC: O(logn) because the exponent n is getting halved
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        b = abs(n)
        res = 1.0

        while b > 0:
            if b % 2 == 1:
                res *= x
            x *= x
            b //= 2
        return 1 / res if n < 0 else res