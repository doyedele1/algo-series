
'''
    Explanation:
        nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

        1   2   3   0   0   0               2   5   6
                p1          p                       p2
        
        First iteration:
            3 < 6, so set nums1[p=5] = 6 and move p2
        Second iteration:
            3 < 5, so set nums1[p=4] = 5 and move p2
        Third iteration:
            3 > 2, so set nums1[p=3] = 3 and move p1
        Fourth iteration:
            2 = 2, so set nums1[p=2] = 2 and move p1
        Fifth iteration:
            1 < 2, so set nums1[p=1] = 2 and move p2
        Sixth iteration:
            p2 is less than 0, so break out of the loop
        
        TC - O(m + n)
        SC - O(1)
'''

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1

        for p in range(m + n -1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1