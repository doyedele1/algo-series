'''
    Explanation:

        TC: O(n + k) where n is the size of the string and k is the size of shifts array
        SC: O(n) to store arr which is the difference array
'''
from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0] * (n + 1)

        for shift in shifts:
            start, end, direction = shift[0], shift[1], shift[2]
            if direction == 1:
                arr[start] += 1
                arr[end + 1] -= 1
            else:
                arr[start] -= 1
                arr[end + 1] += 1

        for i in range(1, n + 1):
            arr[i] += arr[i - 1]

        res = []
        for i in range(n):
            shift = arr[i] % 26
            if shift < 0:
                shift += 26 # just here to ensure non-negative shift

            new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            res.append(new_char)

        return ''.join(res)