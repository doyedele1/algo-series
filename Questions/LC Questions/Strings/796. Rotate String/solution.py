'''
    Explanation I:
        TC: O(m * n), SC: O(n)

    Explanation II:
    LPS: length of the longest prefix which is the same as suffix
    a -> b -> c -> a -> b -> y

        i = 0, j = 1 (initial, LPS = 0)
        a   b   c   a   b   y
        0   

        i = 0, j = 1, the characters are not equal
        a   b   c   a   b   y
        0   0

        i = 0, j = 2
        a   b   c   a   b   y
        0   0   0

        i = 0, j = 3, the characters are equal
        a   b   c   a   b   y
        0   0   0   1

        i = 1, j = 4, the characters are equal
        a   b   c   a   b   y
        0   0   0   1   2
        
        i = 2, j = 5, Check previous of goal[2], which is case b = 0, so check for where i = 0 which is char a. a is not equal to y
        a   b   c   a   b   y
        0   0   0   1   2   0

    KMP: Knuth-Morris-Pratt Algorithm
    i
    a -> b -> x -> a -> b -> c -> a -> b -> c -> a -> b -> y

    j
    a   b   c   a   b   y
    0   0   0   1   2   0

    i = 0, j = 0; same characters, update i, update j
    i = 1, j = 1; same characters, update i, update j
    i = 2, j = 2; different characters, Check previous of goal[2], which is case b = 0, so check for where j = 0 which is char a. a is not equal to x. Update i
    i = 3, j = 0, same characters, update i, update j
    i = 4, j = 1, same characters, update i, update j
    i = 5, j = 2, same characters, update i, update j
    i = 6, j = 3, same characters, update i, update j
    i = 7, j = 4, same characters, update i, update j
    i = 8, j = 5, different characters, Check previous of goal[5], which is case b = 2, so check for where j = 2 which char c. c is equal to c. Update i, update j
    i = 9, j = 3, same characters, update i, update j
    i = 10, j = 4, same characters, update i, update j
    i = 11, j = 5, same characters, update i, update j. Now j is 6 which is the length of goal

    TC: O(m + n) where m is the size of s and n is the size of goal
    SC: O(n) where n is the size of goal
'''

class Solution1:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s
    
class Solution2:
    def rotateString(self, s: str, goal: str) -> bool:
        def lps(pattern):
            n = len(pattern)
            lps = [0] * n
            i, j = 0, 1

            while j < n:
                if pattern[i] == pattern[j]:
                    lps[j] = i + 1
                    i += 1
                    j += 1
                elif i > 0:
                    i = lps[i - 1]
                else:
                    lps[i] = 0
                    j += 1
            return lps
        
        def kmp(text, pattern, lps):
            m, n = len(text), len(pattern)
            i, j = 0, 0

            while i < m:
                if text[i] == pattern[j]:
                    i += 1
                    j += 1
                if j == n:
                    return True
                if i < m and text[i] != pattern[j]:
                    if j > 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return False
        
        if len(s) != len(goal):
            return False
        
        text = s + s
        lps = lps(goal)
        return kmp(text, goal, lps)