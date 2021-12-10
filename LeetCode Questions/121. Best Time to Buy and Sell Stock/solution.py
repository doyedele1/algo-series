from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        
        for i in range(len(prices)):
            price = prices[i]
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
                    
    '''
        TC - O(N) where N is the size of prices list
        SC - O(1) since there is no extra space used in the computer memory. The two variables do not take              much space in the memory
        Explanation:
        [7,1,5,3,6,4]
        - Initialize max_profit variable as 0
        - Initialize min_price as infinity which is the largest price there can ever be
        
        - Iterations:
            - Ensure you know what the min_price is at every iteration
            - And compare the price with previous min_price to get the profit
            - The iteration with the largest profit should be obtained and returned     
    '''