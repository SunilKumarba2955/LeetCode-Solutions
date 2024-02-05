class Solution:
    def frequencySort(self, s: str) -> str:
        s = collections.Counter(s)
        t = dict(sorted(s.items(), key=lambda s: s[1]))
        res = ""
        for i,j in t.items(): res+=i*j
        return res[::-1]