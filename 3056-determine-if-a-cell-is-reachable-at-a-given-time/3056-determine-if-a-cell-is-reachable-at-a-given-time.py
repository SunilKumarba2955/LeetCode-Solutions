class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        fx = abs(fx-sx)
        fy = abs(fy-sy)
        if t==1 and fx==0 and fy==0:
            return False
        return True if max(fx,fy)<=t else False


