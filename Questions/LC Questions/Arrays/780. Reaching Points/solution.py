class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == ty: break
            elif tx > ty:
                if ty > sy: tx %= ty
                else:
                    if (tx - sx) % ty == 0: return True
                    else: return False
            else:
                if tx > sx: ty %= tx
                else:
                    if (ty - sy) % tx == 0: return True
                    else: return False

        if tx == sx and ty == sy: return True
        else: return False