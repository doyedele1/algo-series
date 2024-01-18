'''
    Note: Buy Low, Sell High

    Explanation I: TC: O(n), SC: O(1)
        - Use two pointers. Left starts from index 0, right starts from index 1. Left represents buy, right represents sell
        - Initialize maxProfit as 0
        - While the right pointer is in bounds,
            - If buy price < sell price, then we have a potential maximum profit
            - Else, move the left pointer to where the right pointer is
            - Also, continually move the right pointer
        - Return maxProfit


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
        left, right = 0, 1
        maxProfit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else: left = right    
            right += 1
        return maxProfit

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float("inf")
        
        for i in range(len(prices)):
            price = prices[i]
            if price < minPrice: # we are at loss here
                minPrice = price
            elif price - minPrice > maxProfit: # there is a potential profit
                maxProfit = price - minPrice
        return maxProfit