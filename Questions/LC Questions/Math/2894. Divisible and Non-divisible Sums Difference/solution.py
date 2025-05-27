'''
    Explanation I: Brute-Force (Traverse)
        Find num1 and num2, then find the difference
        
        TC: O(n), SC: O(1)

    Explanation II: Mathematical Way
        We know that num1 = totalSum - num2
        Substituting the above to num1 - num2, we have
        num1 - num2 = totalSum - num2 - num2 = totalSum - 2(num2)

        Also, we know that n = k*m where k is 1, 2, ...., m is our divisor and k*m <= n

        With these observations, we have our solution

        TC: O(1), SC: O(1)
'''

class Solution1:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0

        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        return num1 - num2

class Solution2:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2

        k = n // m
        
        sum_divisible_by_m = m * (k * (k + 1) // 2)

        return total_sum - 2 * sum_divisible_by_m