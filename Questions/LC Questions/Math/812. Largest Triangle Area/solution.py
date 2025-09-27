'''
    Explanation: Math/Geometry
        Formula for finding area of any polygon when you know the coordinates of its vertices
        
        Area = 0.5 * |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|


        TC: O(n-cube) where n is the number of points
        SC: O(1)
'''

from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        res = 0.0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    p = points[i]
                    q = points[j]
                    r = points[k]

                    area = 0.5 * abs(p[0] * (q[1] - r[1]) + q[0] * (r[1] - p[1]) + r[0] * (p[1] - q[1]))
                    res = max(res, area)

        return res