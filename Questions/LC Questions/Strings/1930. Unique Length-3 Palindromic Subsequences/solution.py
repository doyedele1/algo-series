'''
    Explanation:
        
        Observation:
        For, "aabca", we can find the unique palindromes of length 3 by getting all the unique characters in between each character

        For example,
        0   1   2   3   4
        a   a   b   c   a
        For a, we have a at 0 and a at 4, the number of unique characters between them is 3 which is the number of unique palindromes that can be formed from aabca
        For b, no palindromes
        For c, no palindromes

        Another example,
        0   1   2   3   4   5   6
        b   b   c   b   a   b   a
        For b, we have b at 0 and b at 5, the number of unique characters between them is 3 which is the number of unique palindromes that can be formed from bbcbaba
        For c, we have no palindromes
        For a, we have a at 4 and a at 6, the number of unique characters between them is 1 which is the number of unique palindromes that can be formed from bbcbaba

        TC: O(n) where n is the length of s
        SC: O(1)
'''

class Solution:
    def count_palindromic_subsequence(self, s: str) -> int:
        str_map = {}
        count = 0

        for i, char in enumerate(s):
            if char not in str_map:
                str_map[char] = [i, i]
            else:
                str_map[char][1] = i
                
        for _, (start, end) in str_map.items():
            if start == end:
                continue
            count += len(set(s[start+1 : end]))
        return count