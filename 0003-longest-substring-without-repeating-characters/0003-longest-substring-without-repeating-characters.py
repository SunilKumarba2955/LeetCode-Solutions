class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res,start = 0,0
        for i in range(len(s)):
            start = seen[s[i]]+1 if s[i] in seen and start<=seen[s[i]] else start
            res = max(res, i-start+1)
            seen[s[i]] = i
        return res
                