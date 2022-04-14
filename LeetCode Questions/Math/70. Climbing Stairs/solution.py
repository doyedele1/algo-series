'''
    Explanation I: Brute-force solution
        - We take all possible step combinations (1 and 2) at every step
        - climbStairs(i, n) = climbStairs(i + 1, n) + climbStairs(i + 2, n)
        - i is the current step and n is the destination step
        
        - base case if i > n: return 0 and if i == n, return 1
        - recursively call helper(i + 1, n) + helper(i + 2, n)   
        - TC: O(2^n), SC: O(n)
    
    Explanation II: Recursion with Memoization
        - In the brute-force approach, we are redundantly calculating the result for every step
        - Instead, we store the result at each step in memo array and return it when the function is called
        - This way, we are reducing the size of recursion tree up to n
        - TC: O(n), SC: O(n)
'''
class Solution1:
    def climbStairs(self, n: int) -> int:
        def helper(i, n):
            if i > n: return 0
            if i == n: return 1

            return helper(i + 1, n) + helper(i + 2, n)
        return helper(0, n)

class Solution2:
    def climbStairs(self, n: int) -> int:
        def helper(i, n, memo):
            if i > n: return 0
            if i == n: return 1
            if memo[i] > 0: return memo[i]
            memo[i] = helper(i + 1, n, memo) + helper(i + 2, n, memo)
            return memo[i]
        
        memo = [0] * (n + 1)
        return helper(0, n, memo)