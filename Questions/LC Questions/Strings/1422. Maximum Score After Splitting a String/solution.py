class BruteForceSolution:
    def max_score(self, s: str) -> int:
        n = len(s)
        r = 1
        score = 0

        for l in range(1, n):
            leftSubStr = s[0:l]
            rightSubStr = s[r:n]

            zeros = leftSubStr.count("0")
            ones = rightSubStr.count("1")
            score = max(score, zeros + ones)

            r += 1
        return score
    
class Solution:
    def max_score(self, s: str) -> int:
        n = len(s)
        ones = s.count("1")
        zeros = 0
        score = 0

        for i in range(n - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
            
            score = max(score, zeros + ones)
        
        return score