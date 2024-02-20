'''
    Explanation:
        - When the lower roman numeral comes before the higher one, we subtract the lower equivalent from the result
        - When the higher roman numeral comes before the lower one, we add the higher equivalent to the result
        
        MCMXCIV
        First iteration: M and C. We add 1000 to the result, res = 1000
        Second iteration: C and M. We subtract 100 from the result, res = 900
        Third iteration: M and X. We add 1000 to the result, res = 1900
        Fourth iteration: X and C. We subtract 10 from the result, res = 1890
        Fifth iteration: C and I. We add 100 to the result, res = 1990
        Sixth iteration: I and V. We subtract 1 from the result, res = 1989
        Seventh iteration: V. We add 5 to the result, res = 1994

        TC - O(n). We only need to iterate through the given string of roman numerals and perform the algorithm explained above.
        SC - O(1). The hashmap created uses a constant space
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        mapping = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        
        for i in range(len(s)):
            if i + 1 < len(s) and mapping[s[i]] < mapping[s[i + 1]]:
                res -= mapping[s[i]]
            else:
                res += mapping[s[i]]
        return res