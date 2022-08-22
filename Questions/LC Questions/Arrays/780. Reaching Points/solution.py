'''
    Explanation: Work backwards (using modulo)
            (2,5) to (19,12)
                    2,5
                    /\
                7,5   2,7
                /\
            12,5  7,12
                    /\                
                19,12 7,19
    - If final x is greater than final y, then it means we've used (x+y, y) to get to that target point
                
        if tx > ty:
            tx -= ty (i.e. 19 - 12 = 7 as the new x value)
        elif ty > tx:
            ty -= tx
    
    - The above approach is however not optimal. e.g. in the case of (1,9) to (100,9)
                    1,9
                    /\
                10,9   1,10
                /\
            19,9  10,19
             /\                
        28,9  19,28
        ..
        ..
        82,9
         /\
      91,9 82,90
       /\
   100,9
   - We could skip all these steps to get from (100,9) to (1,9) using a modulo
        if tx > ty:
            tx %= ty (i.e. 100 % 9 = 1 as the new x value)
        elif ty > tx:
            ty %= tx
            
    - An edge case where the modulo might not work:
                    (3,3) to (21,9)
                            3,3
                            / \
                         6,3   3,6
                               / \
                           9,6     3,9
                           / \     /   \                
                        15,6 9,15  12,9 3,12
                                    / \
                                 21,9 12,21
            x = 21, y = 9. 21 % 9 = 3
            x = 3, y = 9. 9 % 3 = 0. 0 is not the right answer because we want to go from (3,9) to (3,6) or (3,3)
            
            - However, we want to do is:
                - if tx = sx, for (3,3) and (3,9), we want to do 9-3 = 6 and check if 6 is divisible by tx which is 3. If it is, then we return true
                
        - TC: O(log(max(tx,ty))). We assume that the modulo operation can be done in O(1) time
        - SC: O(1)
'''

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == ty: break
            elif tx > ty:
                if ty > sy: tx %= ty
                else: return (tx - sx) % ty == 0
            else:
                if tx > sx: ty %= tx
                else: return (ty - sy) % tx == 0
        return tx == sx and ty == sy