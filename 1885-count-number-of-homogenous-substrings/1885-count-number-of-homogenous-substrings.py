class Solution:
    def countHomogenous(self, s: str) -> int:
        i = 1
        sub = s[0]
        count = 0
        while i<len(s):
            if s[i-1]==s[i]:
                sub+=s[i]
            else:
                count+=( len(sub)*(len(sub)+1)//2 )
                sub = s[i]
            i+=1
        count+=( len(sub)*(len(sub)+1)//2 )
        return count%(10**9+7)