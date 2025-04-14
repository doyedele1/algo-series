'''
    Explanation I: Brute force
        3 nested loops and find the triplets that meet the conditions
        TC: O(n-cube)

    Explanation II
        TC: O(n-squared + n * M) where M is the maximum value in arr which can be 1000
        SC: O(M) which is 1000
'''

from typing import List

class Solution1:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if (
                        abs(arr[i] - arr[j]) <= a and
                        abs(arr[j] - arr[k]) <= b and
                        abs(arr[i] - arr[k]) <= c
                    ):
                        count += 1
        return count
    
class Solution2:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        prefix_count = [0] * 1001
        # prefix_count[x] -> count of nums <= x
        
        for j in range(n - 1):
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) <= b:
                    # how many values before j where abs conditions are met
                    r = min(arr[j] + a, arr[k] + c)
                    l = max(arr[j] - a, arr[k] - c)

                    l = max(l, 0)
                    r = min(r, 1000)

                    if l <= r:
                        count += prefix_count[r] - (0 if l == 0 else prefix_count[l - 1])
                        
            for index in range(arr[j], 1001):
                prefix_count[index] += 1
            
        return count