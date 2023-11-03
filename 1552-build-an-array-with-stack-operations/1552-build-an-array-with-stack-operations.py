class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        j = 0
        for i in range(1, n+1):
            if j==len(target):
                break
            res.append('Push')
            if target[j] != i:
                res.append('Pop')
                j-=1
            j+=1
        return res