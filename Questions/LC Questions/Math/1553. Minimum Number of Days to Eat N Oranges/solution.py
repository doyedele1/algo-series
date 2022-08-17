'''
    Explanation: Memoization
        - There are three choices to make
            - Eating one orange won't make us reduce the n oranges drastically
            - So, let's focus on the last two choices
                - If divisible by 2, remainingOranges = n - (n/2). i.e. remainingOranges = n/2
                - If divisible by 3, remainingOranges = n - 2n/3. i.e. remaining = n/3
            - Choose the most minimal choice out of the two and store it in your cache hashmap
        
        - Example: n = 10
            choice1 = 0 + getMinDays(5)
        - TC: 
        - SC: O(n) where n is the size of the cache
'''

class Solution:
    def minDays(self, n: int) -> int:
        cache = {}
        
        def getMinDays(remainingOranges):
            if remainingOranges == 0 or remainingOranges == 1: return remainingOranges
            
            if remainingOranges in cache: return cache[remainingOranges]
            
            choice1 = remainingOranges % 2 + getMinDays(remainingOranges // 2)
            choice2 = remainingOranges % 3 + getMinDays(remainingOranges // 3)
            # print(choice1, choice2)
            
            cache[remainingOranges] = 1 + min(choice1, choice2)
            # print("cache", cache)
            return cache[remainingOranges]
            
        return getMinDays(n)