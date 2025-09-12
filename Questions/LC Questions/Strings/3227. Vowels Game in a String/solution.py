'''
    Explanation: Enumeration
        If vowels_count is 0, Bob wins
        If vowels_count is 1, Alice will pick that one and she wins
        If vowels_count is 2, Alice will pick one, and the remaining one can't be picked by Bob, so Alice still wins
        If vowels_count is 3, Alice will pick all three, and she wins
        If vowels_count is 4, Alice will pick three, and the remaining one can't be picked by Bob, so Alice still wins
        If vowels_count is 5, Alice will pick all five, and she wins

        TC: O(n), SC: O(1)
'''

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for c in s:
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                return True
        return False

        # or any(c in "aeiou" for c in s)