class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        t = []
        for i in range(len(dist)):
            t.append((dist[i] + speed[i] -1 )//speed[i])
        t = sorted(t)
        print(t)
        res = 0
        cur = 0
        for i in t:
            if cur>=i:
                return res
            res+=1
            cur+=1
        return res