'''
    Explanation I: Using built-in split and reverse
        - It is an in-space algorithm in Python
        - Linear space complexity
        
        TC: O(n) where n is the number of characters in the string
        SC: O(n), to store the result of split by spaces
        
    Explanation II: 
        "  leetcode is  fun "
        - Trim the spaces
            "leetcode is fun"
        - Convert string to array
        - Reverse the whole array
            "nuf si edocteel"
        - Reverse each word
            "fun is leetcode"
        - Join the array to a string
        
        TC: O(n)
        SC: O(n)
        
    Explanation III: 
        "  leetcode is  fun "
        - Trim the leading and trailing spaces
            "leetcode is  fun"
        - Push word by word in front of the queue
            "fun is leetcode"
        - Join the items in the queue
            "fun is leetcode"
            
        TC: O(n)
        SC: O(n)
'''

import collections

class Solution1:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

class Solution2:
    def reverseWords(self, s: str) -> str:
        def trimSpaces(s):
            i, j = 0, len(s) - 1
            # Remove leading spaces
            while i <= j and s[i] == " ":
                i += 1
            
            # Remove trailing spaces
            while i <= j and s[j] == " ":
                j -= 1
                
            # Reduce multiple spaces to a single space
            res = []
            while i <= j:
                if s[i] != " ": res.append(s[i])
                elif res[-1] != " ": res.append(s[i])
                i += 1
            return res
        
        def reverseArr(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
                
        def reverseEachWord(s):
            i = j = 0
            
            while i < len(s):
                # Go to the end of the word
                while j < len(s) and s[j] != " ":
                    j += 1
                # Reverse the word
                reverseArr(s, i, j - 1)
                # Move to the next word
                i = j + 1
                j += 1
        
        l = trimSpaces(s)
        reverseArr(l, 0, len(l) - 1)
        reverseEachWord(l)
        return "".join(l)

class Solution3:
    def reverseWords(self, s: str) -> str:
        i, j = 0, len(s) - 1
        
        # Remove leading spaces
        while i <= j and s[i] == " ":
            i += 1
        
        # Remove trailing spaces
        while i <= j and s[j] == " ":
            j -= 1
            
        q = collections.deque()
        word = []
        # Push word by word in front of the queue
        while i <= j:
            if s[i] == " " and word:
                q.appendleft("".join(word))
                word = []
            elif s[i] != " ":
                word.append(s[i])
            i += 1
        # to append the last word
        q.appendleft("".join(word))
        
        return " ".join(q)