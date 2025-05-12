from typing import List

# TC: O(n), SC: O(1)
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive_odd_count = 0

        for num in arr:
            if num % 2 == 1:
                consecutive_odd_count += 1
            else:
                consecutive_odd_count = 0
            
            if consecutive_odd_count == 3:
                return True
        return False