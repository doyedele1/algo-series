'''
    Example 1:
    abcde
    First iteration: start = 0, i = 1; res = 1a
    Second iteration: start = 1, i = 2; res = 1b
    Third iteration: start = 2, i = 3; res = 1c
    Fourth iteration: start = 3, i = 4; res = 1d
    Fifth iteration: start = 4, i = 5, the loop stops here

    Example 2:
        b   b   a   a   a   a   a   a   a   a   a   a   a   c   d   d
    s   0        
    i       1

    s=0, i=1, increment i
    s=0, i=2, append 2-0 = 2 and append word[start] = b; res = [2b]
    s=2, i=3, increment i
    s=2, i=4, increment i
    s=2, i=5, increment i
    s=2, i=6, increment i
    s=2, i=7, increment i
    s=2, i=8, increment i
    s=2, i=9, increment i
    s=2, i=10, increment i
    s=2, i=11, increment i
    s=2, i=12, i-s = 10, so decrement i. Then i=11. append 11-2 = 9 and append word[start] = a; res = [2b, 9a]
    s=11, i=12, increment i
    s=11, i=13, append 13-11 = 2 and append word[start] = a, res = [2b, 9a, 2a]
    s=13, i=14, append 14-13 = 1 and append word[start] = c, res = [2b, 9a, 2a, 1c]
    s=14, i=15, increment i
    s=14, i=16, append 16-14 = 2 and append word[start] = d, res = [2b, 9a, 2a, 1c, 2d]

    TC: O(n)
    SC: O(n) for the res array
'''

class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        start = 0
        i = 1
        res = []

        while i < n:
            while i < n and word[i] == word[i-1] and (i - start) < 10:
                i += 1
            
            if (i - start) == 10:
                i -= 1
            
            res.append(str(i - start))
            res.append(word[start])

            start = i
            i += 1

        # for case "abcde"
        if start == n - 1:
            res.append(str(i - start))
            res.append(word[start])
        
        return "".join(res)