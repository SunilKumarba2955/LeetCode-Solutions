class Solution:
    def myAtoi(self, s: str) -> int:
        dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,'8':8, '9':9}
        sign,res = 1,0
        start = 0
        for i in range(len(s)):
            if s[i]==' ' and start!=0:
                return res*sign
            elif s[i] == ' ' and res==0:
                continue
            elif s[i]==' ' and res!=0:
                return res*sign
            elif s[i]>='0' and s[i]<='9':
                res = res*10+dic[s[i]]
                start+=1
            elif s[i]=='-' and res==0 and start==0:
                sign = -1
                start=1
            elif s[i]=='+' and res==0 and start==0:
                start=1
                continue
            else:
                break
        res*=sign
        if res<-2**31: return -2**31
        elif res>2**31-1: return 2**31-1
        else: return res