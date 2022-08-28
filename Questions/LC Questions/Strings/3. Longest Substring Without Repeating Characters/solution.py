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
        SC - O(m) where m is the size of the direct access table to check the substrings. m is 128, which is the possible problem's character set (digits, special characters, lowercases)
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
        
        TC - O(2n) --> depends on the number of times we extend and contract the window (e.g. aaaaaa). We need to extend the window once and contract once at the same time
        SC - O(m) --> m is the size of the table. We need to maintain a window and check whether the substring in the window has duplicates. We use a direct access table to check the substrings. OR O(min(m,n)) where m = size of the charset table and n is the size of the string.
'''

'''
    Explanation III: Previous Sliding Window Solution slightly improved
        pwwkew
         * At the second w, when contracting, if we can record the index of previous w, the left pointer can directly jump the first w to the second w
        
        TC - O(n)
        SC - O(m) for the direct access table OR O(min(m,n))
'''

'''
    Explanation IV: Using hashmap to map the characters to its index
        abcdeafbdgcbb
            res = 1, i = 0, j = 0
            seen = {a: 1}
            
            res = 2, i = 0, j = 1
            seen = {a: 1, b: 2}
            
            res = 3, i = 0, j = 2
            seen = {a: 1, b: 2, c: 3}
            
            res = 4, i = 0, j = 3
            seen = {a: 1, b: 2, c: 3, d: 4}
            
            res = 5, i = 0, j = 4
            seen = {a: 1, b: 2, c: 3, d: 4, e: 5}
            
            res = 5, i = 1, j = 5
            seen = {a: 6, b: 2, c: 3, d: 4, e: 5}
            
            res = 6, i = 1, j = 6
            seen = {a: 6, b: 2, c: 3, d: 4, e: 5, f: 7}
            
            res = 6, i = 2, j = 7
            seen = {a: 6, b: 8, c: 3, d: 4, e: 5, f: 7}
            
            res = 6, i = 4, j = 8
            seen = {a: 6, b: 8, c: 3, d: 9, e: 5, f: 7}
            
            res = 6, i = 4, j = 9
            seen = {a: 6, b: 8, c: 3, d: 9, e: 5, f: 7, g: 10}
            
            res = 7, i = 4, j = 10
            seen = {a: 6, b: 8, c: 11, d: 9, e: 5, f: 7, g: 10}
            
            res = 7, i = 8, j = 11
            seen = {a: 6, b: 12, c: 11, d: 9, e: 5, f: 7, g: 10}
            
            res = 7, i = 12, j = 12
            seen = {a: 6, b: 13, c: 11, d: 9, e: 5, f: 7, g: 10}
        
        TC - O(n). index j will iterate n times
        SC - O(min(m,n)) for the hashmap where m is the size of the charset and n is the size of the string
'''

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        
        leftPointer = 0
        rightPointer = 0
        res = 0
        
        while rightPointer < len(s):
            rightChar = s[rightPointer]
            chars[ord(rightChar)] += 1
            
            while chars[ord(rightChar)] > 1:
                leftChar = s[leftPointer]
                chars[ord(leftChar)] -= 1
                leftPointer += 1
                
            res = max(res, rightPointer - leftPointer + 1)
            rightPointer += 1
        
        return res

class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        
        leftPointer = 0
        rightPointer = 0
        res = 0
        
        while rightPointer < len(s):
            rightChar = s[rightPointer]
            index = chars[ord(rightChar)]
            
            if index != None and index >= leftPointer and index < rightPointer:
                leftPointer = index + 1
                
            res = max(res, rightPointer - leftPointer + 1)
            chars[ord(rightChar)] = rightPointer
            rightPointer += 1
        
        return res
        
class Solution4:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict() # to store the current index of a character
        res = i = 0
        
        for j in range(len(s)):
            if s[j] in seen:
                i = max(i, seen[s[j]])
                
            res = max(res, j - i + 1)
            seen[s[j]] = j + 1
        
        return res