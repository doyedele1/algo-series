'''
    The Fibonacci sequence: 1,1,2,3,5,8,13,21,34,55.....
    Explanation I: Recursion
        - fib(5) = fib(4) + fib (3)
        - fib(4) = fib(3) + fib(2)
        - fib(3) = fib(2) + fib(1)
        - fib(2) = fib(1) + fib(0)
        - We can draw a recursion tree for the equations
        
        - If n <= 1, return n
        - Else, recursively call fib(n) = fib(n-1) + fib(n-2)
        - Do until all numbers have been computed, return the result
        
        - TC: O(2^n), the amount of operations needed for each level of recursion grows exponentially as the depth approached to n
        - SC: O(n) to account for the maximum size of the stack. Potential StackOverflow error might occur if the solution recurses too deeply
        
    Explanation II: Bottom-up using tabulation
        - We can iteratively compute and store the values, only returning once we reach the result
        
        - If n <= 1, return n
        - Loop from 2 through n, store each computed answer in an array
        - Use the array as a reference to the 2 previous numbers to calculate the current Fibonacci number and once we've reached the last number, return its Fibonacci number
        
        - TC: O(n), we loop from 2 up to n and access in O(1)
        - SC: O(n), size of the cache array to store the Fibonacci numbers
        
    Explanation III: Top-down using memoization
        - We can use memoization to store the pre-computed answers, then return the answer for n
        - We won't repeat calculating for the existing values
        
        - Create a map with 0-->0 and 1-->1
        - Recursively call fib(n) function
            - At every recursive call, if n exists in the map, return the cached value for n
            - Else, set the key n in map to the value of fib(n-1) + fib(n-2) and return the result
            
        - TC: O(n), we loop from 2 up to n and access in O(1)
        - SC: O(n), size of the recursive stack and the cache map
        
    Explanation IV: Iterative bottom-up
        - Instead of evaluating the results of fib(n-1) and fib(n-2) to get fib(n), we can only store the value of the two previous numbers and update them as we iterate to n
        
        - If n <=1, return n
        - We need three variables:
            - current = 0
            - previous1 = 1 for fib(n-1)
            - previous2 = 0 for fib(n-2)
            
        - Loop from 2 up to n, 
            - Set the current to previous1 + previous2
            - Set the previous2 to previous1
            - Set the previous1 to current
            
        - Return the current
        
        - TC: O(n)
        - SC: O(1)
'''

class Solution1:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        else: return self.fib(n-1) + self.fib(n-2)


class Solution2:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        
        cache = [0] * (n + 1)
        cache[1] = 1
        
        for i in range(2, n + 1):
            cache[i] = cache[i-1] + cache[i-2]
        
        return cache[n]

class Solution3:
    cache = {0: 0, 1: 1}
    
    def fib(self, n: int) -> int:
        if n in self.cache: return self.cache[n]
        else: self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n]

class Solution4:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        
        current = 0
        previous1 = 1
        previous2 = 0
        
        for i in range(2, n + 1):
            current = previous1 + previous2
            previous2 = previous1
            previous1 = current
        return current        