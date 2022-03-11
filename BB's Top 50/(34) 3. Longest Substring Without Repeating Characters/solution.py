'''
    Explanation I: Naive Solution
        1. We can enumerate all the substrings 
        2. Check the substring that have no repeating characters and check the longest substring
        3. Update the result to the count of the longest substring with no repeating characters
        - abcabcbb
        - From a, we check the substring starting from a
        - From b, we check the substring starting from b
        
        TC - O(n-cube) where n is the size of the input string
        SC - O(m) where m is the size of the direct access table to check the substrings. m is 128, which is the possible problem's charset
        
        abcabcbb
        abca --> has repeating characters. We do not need to check the next substring, which is abcab because we already have duplicates from the previous iteration. We can just move to the next character b and enumerate to get its substrings
'''

'''
    Explanation II: Sliding Window Solution
        - We need two pointers. left --> to contract the window and right --> to extend the window
        left, right = 0, 0
        - abcabcbb
            - abca --> has repeating characters. We do not need to check the next substring, which is abcab because we already have duplicates from the previous iteration. We can just move to the next character b and enumerate to get its substrings
        - We don't need to check for bc again since we already know it does not have repeating characters from the first step. Then we move to bca a dn then bcab. Since bcab has repeating characters, we can move on the next character which is c
        
        - p     w       w       k       e      w
        l 0
        r 0
        - p     w       w       k       e      w
        l 0
        r       0
        - p     w       w       k       e      w --> since there are duplicates, we need to contract the window until there's no duplicate
        l 0
        r               0
        - p     w       w       k       e      w
        l               0
        r               0
        - p     w       w       k       e      w
        l               0
        r                       0
        - p     w       w       k       e      w
        l               0
        r                               0
        - p     w       w       k       e      w --> since there are duplicates, we need to contract the window until there's no duplicate
        l               0
        r                                      0
        - p     w       w       k       e      w
        l                       0
        r                                      0
        
        TC - O(2n) --> depends on the number of times we extend and contract the window (e.g. aaaaaa)
        SC - O(m) --> we need to maintain a window and check whether the substring in the window has duplicates. We use a direct access table
'''

'''
    Explanation III: Previous Sliding Window Solution slightly improved
        pwwkew
         * At the second w, when contracting, if we can record the index of previous w, the left pointer can directly jump the first w to the second w
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        length = anchor = 0
        for i, c in enumerate(s):
            if c in seen and seen[c] >= anchor:
                anchor = seen[c] + 1
            else:
                length = max(length, i + 1 - anchor)
            seen[c] = i
        return length