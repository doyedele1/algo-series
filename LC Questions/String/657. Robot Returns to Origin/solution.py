'''
    Explanation I:
        - Initially the robot is at (0,0)
        - If the robot goes up, y -= 1, etc
        - If x = y = 0, return True
        - TC: O(n), SC: O(1)

	Explanation II:
		- If count of L and R is the same, and count of U and D is the same, return true
		- Else return False
		- TC: O(n), SC: O(1)
'''

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        
        for move in moves:
            if move == "L": x -= 1
            elif move == "R": x += 1
            elif move == "U": y -= 1
            elif move == "D": y += 1
        return x == y == 0


class Solution2:
    def judgeCircle(self, moves: str) -> bool:
        if (moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")): return True
        else: return False