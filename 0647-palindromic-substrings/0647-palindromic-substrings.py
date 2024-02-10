class Solution:
    def isPal(self, s, left, right):
        while left<right:
            if s[left]!=s[right]: return False
            left+=1
            right-=1
        return True
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if self.isPal(s,i,j): ans+=1
        return ans