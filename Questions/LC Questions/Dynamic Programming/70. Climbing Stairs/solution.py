'''
                                0
                1                       2
            2       3               3       4
    3       4       4       5    4       5   5       6
4       5 5     6  5    6  6  7 5   6   6 7 6 7    7  8
5
    Explanation I: Brute-force solution
        - We take all possible step combinations (1 and 2) at every step
        - climbStairs(i, n) = climbStairs(i + 1, n) + climbStairs(i + 2, n)
        - i is the current step and n is the destination step
        
        - base case if i > n: return 0 and if i == n, return 1
        - recursively call helper(i + 1, n) + helper(i + 2, n)   
        TC: O(2^n)
        SC: O(n)
    
    Explanation II: Recursion with Memoization/Caching
        - In the brute-force approach, we are redundantly calculating the result for every step
        - Instead, we store the result at each step in memo array and return it when the function is called - we are storing the result of each of the subproblem
        - This way, we are reducing the size of recursion tree up to n
        TC: O(n)
        SC: O(n)
        
    Explanation III: Fibonacci Number
        - fib(n) = fib(n-1) + fib(n-2)
        - fib(1) = 1, fib(2) = 2
        
        - So we can use the three pointers (first, second, third) to solve the problem
        TC: O(n)
        SC: O(1)
    
    Explanation IV: Bottom-up Dynamic Programming Approach
        - From the tree, let's start at the bottom, solve the base case and work our way up to 0
            0   1   2   3   4   5 - We represent this on an histogram
        dp =   [                1    1]. This contains the number of different ways we can get to the result n from the position above
        dp =   [8   5   3   2    1    1]. For position 3, we can get to "5" 1 + 1 different ways.
                                one   two
        - The resulting array looks like a Fibonacci sequence
        - We don't need an extra dp array which would cost O(n) space
            - If we initialize one and two as 1, we can see that we only need to compute 4 other positions which is n - 1
        
        TC: O(n), 
        SC: O(1)
'''

class Solution1:
    def climb_stairs(self, n: int) -> int:
        def helper(i, n):
            if i > n: return 0
            if i == n: return 1

            return helper(i + 1, n) + helper(i + 2, n)
        return helper(0, n)

class Solution2:
    def climb_stairs(self, n: int) -> int:
        def helper(i, n, memo):
            if i > n: return 0
            if i == n: return 1
            if memo[i] > 0: return memo[i]
            memo[i] = helper(i + 1, n, memo) + helper(i + 2, n, memo)
            return memo[i]
        
        memo = [0] * (n + 1)
        return helper(0, n, memo)

class Solution3:
    def climb_stairs(self, n: int) -> int:
        if n == 1: return 1

        first, second = 1, 2
        
        for _ in range(3, n + 1):
            third = first + second
            first = second
            second = third

        return second

class Solution4:
    def climb_stairs(self, n: int) -> int:
        one, two = 1, 1
        
        for _ in range(n - 1):
            one, two = two, one + two
            
        return two