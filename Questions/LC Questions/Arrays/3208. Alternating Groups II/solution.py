'''
    Explanation:
        Case 1: No alternating window
        [0,0,1,0,0] 
        If k = 4, there is no alternating group
        If k = 3, there is only one alternating group which is window (0, 1, 0)


        Case 2: All alternating window
        [0,1,0,1,0,1]
        If k = 4, there are 6 alternating windows

        With these cases, we can come up with the following:
        We can only get valid window if the colors are alternating
        With two pointers (l and r), if (r - l) > k, then the number of valid windows is (r - l) - k + 1

        [0, 1, 0, 0, 1, 0, 1], k = 4
        l pointer:
            min = 0
            max = 6
        r pointer:
            min = 3
            max = n + k - 1 = 7 + 4 - 1 = 10 (stop at index 10 - cyclic)
        
        TC: O(n)
        SC: O(1)
'''
from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        count = 0
        l = 0
        limit = n + k - 1

        while l < n:
            r = l + 1
            while r < limit and colors[(r - 1) % n] != colors[r % n]:
                r += 1

            if r - l >= k:
                count += (r - l) - k + 1
            l = r

        return count