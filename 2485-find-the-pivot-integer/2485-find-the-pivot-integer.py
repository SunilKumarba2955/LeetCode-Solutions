class Solution:
    def pivotInteger(self, n: int) -> int:
        sm = (n*(n+1))//2
        for i in range(1, n+1):
            l = (i*(i+1))//2
            r = sm-l+i
            # print(l,r)
            if l==r:
                return i
            if l>r:
                break
        return -1