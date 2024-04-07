class Solution:
    def checkValidString(self, s: str) -> bool:
        star = []
        left = []
        for i in range(len(s)):
            if s[i]=='(':
                left.append(i)
            elif s[i]=='*':
                star.append(i)
            else:
                if len(left)>0:
                    left.pop()
                elif len(star)>0:
                    star.pop()
                else:
                    return False
        l,r = len(left)-1, len(star)-1
        # print(left)
        # print(star)
        if l>r:
            return False
        while l>=0 and l<=r and left[l]<star[r]:
            l-=1
            r-=1
        return True if l==-1 else False