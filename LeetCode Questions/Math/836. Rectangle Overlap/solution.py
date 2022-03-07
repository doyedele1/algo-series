'''
    Explanation:
        (x1, y1) ==> bottom-left
        (x2, y2) ==> top-right
        
        * if the area of their intersaction is positive, then two rectangles overlap
        * two rectangles that touch at edges - do not overlap
        
        
        
        return not (left or bottom or right or top)
        left => condition rec1 to the left of rec2 = rec1[2] <= rec2[0]
'''

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
        
        return not (rec1[2] <= rec2[0] or rec1[3] <= rec2[1] or rec1[0] >= rec2[2] or rec1[1] >= rec2[3])