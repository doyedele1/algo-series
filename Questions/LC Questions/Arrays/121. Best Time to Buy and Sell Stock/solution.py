'''
    BUY LOW, SELL HIGH
    [7,1,5,3,6,4]

    Explanation: TC: O(n), SC: O(1)
        Visualizing first
            .
                            .
                    .
                                .
                        .

                .

        First iteration:
            Is 1 < 7, yes, then start = 1
            res = 0
        Second iteration,
            Is 5 < 1, no
            res = 4
        Third iteration,
            Is 3 < 1, no
            res = 4
        Fourth iteration,
            Is 6 < 1, no
            res = 5
        Fifth iteration,
            Is 4 < 1, no
            res = 5

    Another possible solution:
        - Initialize res variable as 0
        - Initialize min_price as infinity which is the largest price there can ever be
        - Ensure you know what the min_price is at every iteration
        - And compare the price with previous min_price to get the profit
        
        [7,1,5,3,6,4]

        First iteration,
            Is 7 < infinity, yes, then minPrice = 7
        Second iteration,
            Is 1 < 7, yes, then minPrice = 1
        Third iteration,
            Is 5 < 1, no.
            Is 5 - 1 > 4, yes, res = 4
        Fourth iteration,
            Is 3 < 1, no
            Is 3 - 1 > 4, no
        Fifth iteration,
            Is 6 < 1, no
            Is 6 - 1 > 4, yes, res = 5
        Sixth iteration,
            Is 4 < 1, no
            Is 4 - 1 > 5, no
'''

from typing import List

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        res = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[start]:
                start = i
            res = max(res, prices[i] - prices[start])
        return res

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = float("inf")
        
        for i in range(len(prices)):
            price = prices[i]
            if price < minPrice: # we are at loss here
                minPrice = price
            elif price - minPrice > res: # there is a potential profit
                res = price - minPrice
        return res