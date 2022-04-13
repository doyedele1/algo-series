'''
    Explanation:
        two operations: multiply by 2, or subtract 1 from startValue
        We can instead perform the following:
            - divide by 2 if target number is even
            - add 1 to target number if odd

        Hence,
            - While target is larger than startValue,
                - If target is odd, add 1 to target
                - Else, divide target by 2
            - Then we need to do startValue - target additions to reach startValue

        Example 1: startValue = 2, target = 3

        res = 1
        target = 4

        res = 2
        target = 2
        answer = 2 + 2 - 2 = 2

        Example 3: startValue = 3, target = 10
        res = 1
        target = 5

        res = 2
        target = 6

        res = 3
        target = 3
        answer = 3 + 3 - 3 = 3

        TC - O(log target)
        SC - O(1)
'''

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0
        while target > startValue:
            res += 1
            if target % 2 == 1:
                target += 1
            else:
                target //= 2

        return res + startValue - target