'''
    Explanation:
        Let's say we have amount of stocks [15, 10, 5, 20, 40]
            0   1   2   3   4
            15  10  5   20  40
        queries: invest(1, 3, 10); invest(1, 4, 5)

        We can find the relative stocks.
            0   1   2   3   4
            15  -5  -5  15  20  0 (dummy value)

        For every query, we do r[i] += q, r[j + 1] -= q
        
        First query: invest(1, 3, 10)
            0   1   2   3   4
            15  5  -5   15  10  0 (dummy value)

        Second query: invest(1, 4, 5)
            0   1    2   3   4
            15  10  -5   15  10  5 (dummy value)
        
        Return [15, 25, 20, 35, 45]
        
        TC: O(n + k). Each of the k update operations takes O(1) time. Performing the cumulative sum at the end to get the result takes O(n) time
        SC: O(1)
'''
from typing import List

class Solution:
    def get_modified_array(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * (length + 1)

        for tuple in updates:
            start, end, inc = tuple[0], tuple[1], tuple[2]

            arr[start] += inc

            if end + 1 < len(arr):
                arr[end + 1] -= inc
            
        for i in range(1, length):
            arr[i] += arr[i - 1]
        
        return arr[:-1]