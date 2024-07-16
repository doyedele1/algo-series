'''
    Explanation:
        Observations
            1. Eliminating for the first time of input 2n is the same when eliminating for the first time of input 2n + 1
            2. Given 2n (even),
                1   2   3   4   5   6   7   8   9   10
                After the first elimination, we have, 2   4   6   8   10 which is 2 * (1  2   3   4   5)
                After the second elimination, we have, 4    8
                After the third elimination, we have 8

            First iteration: 
                remain = 10 (which is even), start = 1, step = 1, move = left
                After first elimination, remain = 5, start = 2, step 2, move = right
            Second:
                remain = 5 (which is odd), start = 2, step = 2, move = right
                After second elimination, remain = 2, start = 4, step 4, move = left
            Third: 
                remain = 2 (which is even), start = 4, step = 4, move = left
                After third elimination, remain = 1, start = 8, step 8, move = right
    
        TC: O(logn), SC: O(1)
'''

class Solution:
    def lastRemaining(self, n: int) -> int:
        start = 1
        remain = n
        left = True
        step = 1

        while remain > 1:
            if left or remain % 2 == 1:
                start += step
            remain //= 2
            step *= 2
            left = not left
        return start