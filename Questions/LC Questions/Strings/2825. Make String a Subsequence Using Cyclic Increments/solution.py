'''
    Explanation:
        s1 = abc, s2 = ad, return True
        s1 = abd, s2 = ad, return True
        s1 = abd, s2 = cd, return True
        s1 = abd, s2 = bcd, return True
        s1 = abc, s2 = abca, return False
        s1 = abc, s2 = ec, return False

        Observation: Greedy Match - Two pointer
        s1 = abxcdxy, s2 = xy. We need to match with the first x and not the second x
        s1 = abxcdxy, s2 = xd. If we had matched with the second x, then the char d will not be matched
        s1 = abxcdxy, s2 = cd. s2 could already be a subsequence of s1
        s1 = abxyc, s2 = cd. For every character in s2, we check if it is equal to the char in s1 or the next char of s1

        How to get the next character cyclically
            - If the character is c, (c - 'a' + 1) = 3. But to get d, we do 3 + 'a'
            - If the character is z, (z - 'a' + 1) = 26. But to get a, we do (26 % 26) + 'a'

        Example Walkthrough:
        s1 = bzayc, s2 = azc
        First iteration: i = 0, j = 0, b and a are not cyclically equal, move i
        Second iteration: i = 1, j = 0, z and a are cyclically equal, move i and j
        Third iteration: i = 2, j = 1, a and z are not cyclically equal, move i
        Fourth iteration: i = 3, j = 1, y and z are cyclically equal, move i and j
        Fifth iteration: i = 4, j = 2, c and c are cyclically equal, move i and j

        If length of s2 is the same as j, then return True, else return False

        TC: O(m + n)
        SC: O(1)
'''

class Solution:
    def getNextCharacter(self, char):
        intOfTheNextChar = ord(char) - ord('a') + 1
        return chr((intOfTheNextChar % 26) + ord('a'))

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m, n = len(str1), len(str2)
        j = 0

        if m < n:
            return False

        for i in range(m):
            if j < n and (str1[i] == str2[j] or self.getNextCharacter(str1[i]) == str2[j]):
                j += 1
        
        return j == n