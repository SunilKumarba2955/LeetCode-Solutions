class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        res = 0
        while n>0:
            if n&1==1:
                res+=1
            n>>=1
        return True if res==1 else 0