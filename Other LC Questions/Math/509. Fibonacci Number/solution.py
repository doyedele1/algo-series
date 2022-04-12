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
        
    Explanation II: Bottom-up using tabulation
        - We can iteratively compute and store the values, only returning once we reach the result
        
        - If n <= 1, return n
        - Loop through n, store each computed answer in an array
        - Use the array as a reference to the 2 previous numbers to calculate the current Fibonacci number
        - Once we've reached the last number, return its Fibonacci number
        
        - TC: O(n)
        - SC: O(n), where n is the size of the cache array
    
'''


class Solution1:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        else: return self.fib(n-1) + self.fib(n-2)