'''
    BUY LOW, SELL HIGH

    Explanation I: TC: O(n), SC: O(1)
        - Use two pointers. Left starts from index 0, right starts from index 1. Left represents buy, right represents sell
        - Initialize res as 0
        - 
        - Return res

    Explanation II: TC: O(n), SC: O(1)
        [7,1,5,3,6,4]
        - Initialize max_profit variable as 0
        - Initialize min_price as infinity which is the largest price there can ever be
        
        - Iterations:
            - Ensure you know what the min_price is at every iteration
            - And compare the price with previous min_price to get the profit
            - The iteration with the largest profit should be obtained and returned
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