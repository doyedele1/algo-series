'''
    Explanation: Dynamic Programming
        low = 2, high = 3, zero = 1, one = 2
        Let's build a dp array of size high
        dp = [1,0,0,0]
        dp[3] stands for the number of good strings of length 3

        Let's build the dp tree (which will be a binary tree)
                            ""
                  "0"                       "11"
            "00"       "011"           "110"    "1111"
        "000" "0011"

        At every length, we have 1 + (answer when we include 0) + answer when we include 1)

        Hence,
        At "000", return 1
        At "00", return 2 because "000" and "0011" return 1 and 0 respectively
        At "0", return 3 because "00" and "011" return 2 and 1 respectively
        At "11", return 2 because "110" will return 1 since "000" (of the same length 3) also returned 1
        At "", add up "0" and "11" = 3 + 2 = 5

        For the binary tree, TC should be O(2^n), but because we are solving the subproblems already, TC will then be O(n) where n is the length of the string
        
        TC: O(high)
        SC: O(high)
'''

class Solution:
    def __init__(self):
        self.dp = [-1] * 100001
        self.MOD = 1000000007

    def count_ways(self, low, high, zero, one, pos):
        if pos > high:
            return 0
        if self.dp[pos] != -1:
            return self.dp[pos]

        count = 0
        if pos >= low:
            count += 1
        count += self.count_ways(low, high, zero, one, pos + zero)
        count += self.count_ways(low, high, zero, one, pos + one)

        self.dp[pos] = count % self.MOD
        return self.dp[pos]

    def count_good_strings(self, low: int, high: int, zero: int, one: int) -> int:
        # to reset the dp array so that the results from other method do not interfere with the current count_good_strings method
        self.dp = [-1] * 100001
        return self.count_ways(low, high, zero, one, 0)