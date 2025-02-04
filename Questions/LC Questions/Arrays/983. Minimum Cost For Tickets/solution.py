from typing import List

class Solution:
    def __init__(self):
        self.dp = {}
    
    def solve(self, days: List[int], costs: List[int], pos: int, reachability: int) -> int:
        if pos > len(days) - 1:
            return 0
        if reachability >= days[pos]:
            return self.solve(days, costs, pos + 1, reachability)
        if pos in self.dp:
            return self.dp[pos]

        one = costs[0] + self.solve(days, costs, pos + 1, days[pos])
        seven = costs[1] + self.solve(days, costs, pos + 1, days[pos] + 6)
        month = costs[2] + self.solve(days, costs, pos + 1, days[pos] + 29)

        result = min(one, seven, month)
        self.dp[pos] = result
        return result

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return min(
            costs[0] + self.solve(days, costs, 0, days[0]),
            costs[1] + self.solve(days, costs, 0, days[0] + 6),
            costs[2] + self.solve(days, costs, 0, days[0] + 29)
        )