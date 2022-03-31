class Solution:
    def numSplits(self, s: str) -> int:
        
        dict_s = {}
        dict_q = {}
        
        no_of_good_splits = 0
        
        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else: dict_s[char] = 1

                
        for char in s:
            if char in dict_s:
                dict_s[char] -= 1
                if char in dict_q:
                    dict_q[char] += 1
                else: dict_q[char] = 1
                if dict_s[char] == 0:
                    dict_s.pop(char)
            if len(dict_s) == len(dict_q): no_of_good_splits += 1
        return no_of_good_splits