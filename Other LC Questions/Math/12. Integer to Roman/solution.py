'''
    Explanation:
        - Note: Knowing which representation is the correct one for a particular number can be difficult. There are many possible ways of representing the number 120 for instance.
        
        - So if num = 9, X and I are needed. Rule of roman numeral goes from largest to smallest. However, there are some special rules where the symbol with a smaller value can go before the symbol with a larger value.
        
        - If there are no special rules, when num = 1500,
            - We can divide 1500/M. i.e. 1500//1000 = 1. 1 tells us how many Ms in our final result.
            - Then 1500 % 1000 = 500
            - 500 // 500 = 1. 1D in the final result
            - 500 % 500 = 0, now we can stop since we've found the result
        - Since there are special rules, we could have those special rules appended in our symbol-value table, and perform the above steps
        - We converted the symbol-value table to a nested list because we need to iterate through the items in a sorted reverse order

    TC - O(1) since there are constant set of roman numerals. In the worst case, when we have number 3888, roman equivalent is MMMDCCCLXXXVIII which is 15.
    SC - O(1) since the dictList doesn't change with the size of the input
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        dictList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        
        res = ""
        
        for symbol, value in reversed(dictList):
            if num // value:
                frequency = num // value
                res += symbol * frequency
                num %= value
        return res