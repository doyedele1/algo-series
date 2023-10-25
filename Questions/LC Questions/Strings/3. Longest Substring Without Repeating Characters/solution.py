'''
    Explanation I: Naive Solution
        - Enumerate the string and check all the substrings. Check the longest substring that have no repeating characters
        - Update the result to the count of the longest substring with no repeating characters
            abcabcbb
            - From a, we check the substring starting from a
            - From b, we check the substring starting from b
        
            abcabcbb
            abca --> has repeating characters. We do not need to check the next substring, which is abcab because we already have duplicates from the previous iteration. 
            We can just move to the next character b and enumerate to get its substrings. Also here bc has already been checked, so we can check bca instead.
        
        TC - O(n-cube) where n is the size of the input string
        SC - O(min(n,m)) where n is the size of the input string and m is the size of the charset table

        
    Explanation II: Sliding Window Solution
        - We need two pointers. left --> to contract the window and right --> to extend the window
        left, right = 0, 0
        - abcabcbb
            - abca --> has repeating characters. We do not need to check the next substring, which is abcab because we already have duplicates from the previous iteration. We can just move to the next character b and enumerate to get its substrings
        - We don't need to check for bc again since we already know it does not have repeating characters from the first step. Then we move to bca and then bcab. Since bcab has repeating characters, we can move on the next character which is c
        
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
        
        TC - O(2n) --> depends on the number of times we extend and contract the window (e.g. aaaaaa). We need to extend the window once and contract once at the same time
        SC - O(m) where m is the size of the charset table

        
    Explanation III: Using hashmap to map the characters to its index
    pwwkew
         * At the second w, when contracting, if we can record the index of previous w, the left pointer can directly jump the first w to the second w
        
    Another example:
        abcdeafbdgcbb
            When res = 0, i = 0, j = 0, seen = {}
            res = 1, i = 0, j = 0, seen = {a:1}

            When res = 1, i = 0, j = 1, seen = {a:1}
            res = 2, i = 0, j = 1, seen = {a:1, b:2}

            When res = 2, i = 0, j = 2, seen = {a:1, b:2}
            res = 3, i = 0, j = 2, seen = {a:1, b:2, c:3}

            When res = 3, i = 0, j = 3, seen = {a:1, b:2, c:3}
            res = 4, i = 0, j = 3, seen = {a:1, b:2, c:3, d:4}
            
            When res = 4, i = 0, j = 4, seen = {a:1, b:2, c:3, d:4}
            res = 5, i = 0, j = 4, seen = {a:1, b:2, c:3, d:4, e:5}
            
            When res = 5, i = 0, j = 5, seen = {a:1, b:2, c:3, d:4, e:5} -- there are duplicates of a
            i = max(0,1) = 1, j = 5, res = 5, seen = {a:6, b:2, c:3, d:4, e:5}
            
            When res = 5, i = 1, j = 6, seen = {a:6, b:2, c:3, d:4, e:5}
            res = 6, i = 1, j = 6, seen = {a:6, b:2, c:3, d:4, e:5, f:7}
            
            When res = 6, i = 1, j = 7, seen = {a:6, b:2, c:3, d:4, e:5, f:7} -- there are duplicates of b
            i = max(1,2) = 2, j = 7, res = 6, seen = {a:6, b:8, c:3, d:4, e:5, f:7}

            When res = 6, i = 2, j = 8, seen = {a:6, b: 8, c:3, d:4, e:5, f:7} -- there are duplicates of d
            i = max(2, 4) = 4, j = 8, res = max(6,5) = 6, seen = {a:6, b:8, c:3, d:9, e:5, f:7}

            When res = 6, i = 4, j = 9, seen = {a:6, b:8, c:3, d:9, e:5, f:7}
            res = 6, i = 4, j = 9, seen = {a:6, b:8, c:3, d:9, e:5, f:7, g:10}

            When res = 6, i = 4, j = 10, seen = {a:6, b:8, c:3, d:9, e:5, f:7, g:10} -- there are duplicates of c
            i = max(4,3) = 4, j = 10, res = 7, seen = {a:6, b:8, c:11, d:9, e:5, f:7, g:10}

            When res = 7, i = 4, j = 11, seen = {a:6, b:8, c:11, d:9, e:5, f:7, g:10} -- there are duplicates of b
            i = max(4,8) = 8, j = 11, res = max(7,4) = 7, seen = {a:6, b:12, c:11, d:9, e:5, f:7, g:10}

            When res = 7, i = 8, j = 12, seen = {a:6, b:12, c:11, d:9, e:5, f:7, g:10} -- there are duplicates of b
            i = max(8,12) = 12, j = 12, res = max(7,1) = 7, seen = {a:6, b:13, c:11, d:9, e:5, f:7, g:10}
        
        TC - O(n). index j will iterate n times
        SC - O(min(m,n)) for the hashmap where m is the size of the charset and n is the size of the string
'''
from collections import Counter, defaultdict

class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def checkHelper(start, end):
            chars = set()
            for i in range(start, end + 1):
                c = s[i]
                if c in chars:
                    return False
                chars.add(c)
            return True

        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if checkHelper(i, j):
                    res = max(res, j - i + 1)
        return res
    
# Using counter as the hashmap
class Solution2a:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()
        
        left, right, res = 0, 0, 0
        
        while right < len(s):
            rightChar = s[right]
            chars[rightChar] += 1
            
            while chars[rightChar] > 1:
                leftChar = s[left]
                chars[leftChar] -= 1
                left += 1
                
            res = max(res, right - left + 1)
            right += 1
        
        return res

# Using a charset array table as the hashmap - faster solution than 2a
class Solution2b:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128
        
        left, right, res = 0, 0, 0
        
        while right < len(s):
            rightChar = s[right]
            index = chars[ord(rightChar)]
            
            if index is not None and left <= index < right: left = index + 1
            
            res = max(res, right - left + 1)
            
            chars[ord(rightChar)] = right
            right += 1
        
        return res

class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict() # to store the current index of a character
        res, i = 0, 0
        
        for j in range(len(s)):
            if s[j] in seen:
                i = max(i, seen[s[j]])
                
            res = max(res, j - i + 1)
            seen[s[j]] = j + 1
        
        return res