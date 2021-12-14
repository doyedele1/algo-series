class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        for i in range(len(s)):
            if i + 1 < len(s) and dict[s[i+1]] > dict[s[i]]:
                integer -= dict[s[i]]
            
            else:
                integer += dict[s[i]]
                
        return integer


        
    '''
    Thought process = 
        When the lower roman numeral comes before the higher one, we subtract the lower equivalent integer from the higher equivalent integer to get the result. 
        While, when the higher roman numeral comes before the lower one, we can add the quivalent integer of the higher roman numeral to the result.
    Complexity analysis =
        TC - O(n). We only need to iterate through the given string of roman numerals and perform the algorithm explained above.
        SC - O(1). The hashmap created uses a constant space. The length of the conversion from roman numerals to integer doesn't vary.
    '''