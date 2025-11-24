# more efficient solution according to LeetCode runtime analysis
class Solution1:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        score = 0

        for i in range(n - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score
    
class Solution2:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        score = 0

        for i in range(1, n):
            score += abs(ord(s[i]) - ord(s[i - 1]))
        return score