class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n==1: return n
        seen = {}
        for i in trust:
            if i[1] not in seen:
                seen[i[1]] = set()
            seen[i[1]].add(i[0])
        for i,j in seen.items():
            if len(list(j))==n-1:
                flag = 0
                for k in list(j):
                    if k in seen and i in seen[k]:
                        flag=1
                        break
                if flag==0:
                    return i
        # print(seen)
        return -1